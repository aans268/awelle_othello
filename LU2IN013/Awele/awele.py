#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("..")
import game

def initialiseJeu():
    jeu=[0,0,0,0,0]
    plateau=[[4,4,4,4,4,4],[4,4,4,4,4,4]]
    jeu[0]= plateau
    jeu[1]= 1
    jeu[3]=[]
    jeu[4]= [0,0]
    return jeu


def finJeu(jeu):
    if len(jeu[3])>100:
        #print("NOMBRE DE TOURS LIMITES ATTEINT")
        return True
    if jeu[1]==1:
        for i in range(6):
            if estValide(jeu,[0,i]):
                return False
    if jeu[1]==2:
        for i in range(6):
            if estValide(jeu,[1,i]):
                return False
    return True

def estAffame(jeu,Joueur):
    return sum(jeu[0][jeu[1]-1],0)==0

def estValide(jeu,coup,checkNourrit=False):
    if not(coup[0]==(jeu[1]-1)):
        return False
    g=jeu[0][coup[0]][coup[1]]
    if g==0 :
        return False
    if checkNourrit:
        if coup[0]==0:
            #vérifie si on a suffisamment de graines dans la case jouée pour nourrir notre adversaire
            return g>coup[1]
        if coup[0]==1:
            #pareil mais pour l'autre joueur
            return (g>(5-coup[1]))
    return True

def listeCoupsValides(jeu):
    affame=estAffame(jeu,3-jeu[1])
    liste=[]
    for c in range(0,6):
        if estValide(jeu,[jeu[1]-1,c],affame):
            liste.append([jeu[1]-1,c])
    return liste


def nextCase(pos,antihoraire=True):
    if antihoraire:
        if(pos[0]==0):
            if pos[1]==0:
                return [1,0]
            return [0,pos[1]-1]
        if pos[1]==5:
            return [0,5]
        return [1,pos[1]+1]
    #SENS HORAIRE 
    if(pos[0]==0):
        if pos[1]==5:
            return [1,5]
        return [0,pos[1]+1]
    if pos[1]==0:
        return [0,0]
    return [1,pos[1]-1]
    

def joueCoup(jeu, coup):
    jeu[3].append(coup)
    nbgrainesinitial=jeu[0][coup[0]][coup[1]]
    pos=[coup[0],coup[1]]
    jeu[0][coup[0]][coup[1]]=0
    #on egraine
    for c in range(nbgrainesinitial):
        pos=nextCase(pos)
        if pos==coup:
            pos=nextCase(pos)
        jeu[0][pos[0]][pos[1]]=jeu[0][pos[0]][pos[1]]+1

    jeuclone= game.getCopieJeu(jeu)
    nbgraines=0
    streak=True
    #on mange pendant la streak
    while (streak and pos[0]==jeuclone[1]%2):
        if (jeuclone[0][pos[0]][pos[1]]==2 or jeuclone[0][pos[0]][pos[1]]==3):
            nbgraines = nbgraines + jeuclone[0][pos[0]][pos[1]]
            jeuclone[0][pos[0]][pos[1]] = 0
            pos = nextCase(pos,False)
        else:
            streak=False
    #si on a mange sans l'affame alors c'est bon sinon juste on egraine
    if(not estAffame(jeuclone,3-jeu[1])):
        jeu[0]=jeuclone[0]
        jeu[1]=jeuclone[1]
        jeu[2]=jeuclone[2]
        jeu[3]=jeuclone[3]
        jeu[4]=jeuclone[4]
        jeu[4][jeu[1]-1]=jeu[4][jeu[1]-1]+nbgraines
    #print("PROC DU CHANGE JOUEUR DE AWELE.PY")
    game.changeJoueur(jeu)
    #print("ouui",game.getJoueur(jeu))
    #return jeu