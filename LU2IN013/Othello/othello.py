#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("..")
import game
import copy
def initialiseJeu():
    jeu=[0,0,0,0,0]
    plateau=[[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,1,2,0,0,0],
        [0,0,0,2,1,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0]]
    jeu[0]= plateau
    jeu[1]= 1
    jeu[3]=[]
    jeu[4]= [2,2]
    return jeu

def finJeu(jeu):
    #print(len(jeu[3]))
    return listeCoupsValides(jeu)==[] or len(jeu[3])>50
    
    #for i in range(8):
    #    for j in range(8):
    #        if estValide(jeu,[i,j]):
    #            return False
    #return True

def estValide(jeu,coup):
    if jeu[0][coup[0]][coup[1]]!=0: #si c'est pas une case vide c'est pas bon
        return False
    jeuclone=[0,0,0,0,0]
    jeuclone[0]=copy.deepcopy(jeu[0])
    jeuclone[1]=jeu[1]
    jeuclone[2]=jeu[2]
    jeuclone[3]=jeu[3]
    jeuclone[4]=copy.deepcopy(jeu[4])

    #test gauche
    if coup[1]-1>0: 
        if jeuclone[0][coup[0]][coup[1]-1]==3-jeuclone[1]: #si il y a un ennemi a proximite
            analyseCase(jeuclone,coup[0],coup[1]-1,0,-1) #on analyse dans sa direction
            if jeuclone[0][coup[0]][coup[1]-1]==jeuclone[1]: #si il est mange : c'est bon / sinon : on continue sur les autres cases
                return True

    #test haut gauche
    if coup[0]-1>0 and coup[1]-1>0:
        if jeuclone[0][coup[0]-1][coup[1]-1]==3-jeuclone[1]:
            analyseCase(jeuclone,coup[0]-1,coup[1]-1,-1,-1)
            if jeuclone[0][coup[0]-1][coup[1]-1]==jeuclone[1]:
                return True

    #test bas gauche
    if coup[0]+1<7 and coup[1]-1>0:
        if jeuclone[0][coup[0]+1][coup[1]-1]==3-jeuclone[1]:
            analyseCase(jeuclone,coup[0]+1,coup[1]-1,+1,-1)
            if jeuclone[0][coup[0]+1][coup[1]-1]==jeuclone[1]:
                return True

    #test haut
    if coup[0]-1>0:  
        if jeuclone[0][coup[0]-1][coup[1]]==3-jeuclone[1]:
            analyseCase(jeuclone,coup[0]-1,coup[1],-1,0)
            if jeuclone[0][coup[0]-1][coup[1]]==jeuclone[1]:
                return True

    #test bas
    if coup[0]+1<7: 
        if jeuclone[0][coup[0]+1][coup[1]]==3-jeuclone[1]:
            analyseCase(jeuclone,coup[0]+1,coup[1],+1,0)
            if jeuclone[0][coup[0]+1][coup[1]]==jeuclone[1]:
                return True

    #test haut droite
    if coup[0]-1>0 and coup[1]+1<7:
        if jeuclone[0][coup[0]-1][coup[1]+1]==3-jeuclone[1]:
            analyseCase(jeuclone,coup[0]-1,coup[1]+1,-1,+1)
            if jeuclone[0][coup[0]-1][coup[1]+1]==jeuclone[1]:
                return True

    #test droite
    if coup[1]+1<7:
        if jeuclone[0][coup[0]][coup[1]+1]==3-jeuclone[1]:
            analyseCase(jeuclone,coup[0],coup[1]+1,0,+1)
            if jeuclone[0][coup[0]][coup[1]+1]==jeuclone[1]:
                return True

    #test bas droite
    if coup[0]+1<7 and coup[1]+1<7: 
        if jeuclone[0][coup[0]+1][coup[1]+1]==3-jeuclone[1]:
            analyseCase(jeuclone,coup[0]+1,coup[1]+1,+1,+1)
            if jeuclone[0][coup[0]+1][coup[1]+1]==jeuclone[1]:
                return True

    return False

def listeCoupsValides(jeu):
    liste=[]
    for i in range(8):
        for j in range(8):
            if estValide(jeu,[i,j]):
                liste.append([i,j])
    return liste

def analyseCase(jeu,posx,posy,dirx,diry):
    if posx<0 or posx>7 or posy<0 or posy>7: #on se stop aux bordures
        return False
    if jeu[0][posx][posy]==game.getJoueur(jeu): #si c'est un allie on mange toute la ligne
        return True
    if jeu[0][posx][posy]==0: #si c'est vide on stop
        return False
    if analyseCase(jeu,posx+dirx,posy+diry,dirx,diry): #vrai si plus loin il y a un allie (donc encercle)
        if jeu[0][posx][posy]==3-game.getJoueur(jeu): #si c'est un ennemi
            jeu[4][jeu[1]-1]=jeu[4][jeu[1]-1]+1 #modif score
            jeu[4][2-jeu[1]]=jeu[4][2-jeu[1]]-1 #modif score
        if jeu[0][posx][posy]==0: #si c'est vide
            jeu[4][jeu[1]-1]=jeu[4][jeu[1]-1]+1 #modif score
        jeu[0][posx][posy]=game.getJoueur(jeu) #on change la couleur de la case
        return True
    return False




def joueCoup(jeu,coup):
    jeu[3].append(coup)
    jeu[0][coup[0]][coup[1]]=game.getJoueur(jeu)
    jeu[4][jeu[1]-1]=jeu[4][jeu[1]-1]+1
    if coup[0]-1>0 and coup[1]-1>0:                 #Analyse la case en haut à gauche
        analyseCase(jeu,coup[0]-1,coup[1]-1,-1,-1)
    if coup[0]-1>0:                                 #à gauche
        analyseCase(jeu,coup[0]-1,coup[1],-1,0)
    if coup[0]-1>0 and coup[1]+1<7:                 #en bas à gauche
        analyseCase(jeu,coup[0]-1,coup[1]+1,-1,1)
    if coup[1]+1<7:                                 #en bas
        analyseCase(jeu,coup[0],coup[1]+1,0,1)
    if coup[1]-1>0:                                 #en haut
        analyseCase(jeu,coup[0],coup[1]-1,0,-1)
    if coup[0]+1<7 and coup[1]+1<7:                 #en bas à droite
        analyseCase(jeu,coup[0]+1,coup[1]+1,1,1)
    if coup[0]+1<7:                                 #à droite
        analyseCase(jeu,coup[0]+1,coup[1],1,0)
    if coup[0]+1<7 and coup[1]-1>0:                 #en haut à droite
        analyseCase(jeu,coup[0]+1,coup[1]-1,1,-1)
    game.changeJoueur(jeu)
    #return jeu