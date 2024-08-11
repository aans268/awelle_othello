#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import othello
import sys
sys.path.append("..")
import game
game.game=othello
sys.path.append("./Joueurs")
import joueur_humain
import joueur_aleatoire
import joueur_alpha_beta
import joueur_alpha_beta_bis
import joueur_min_max
import random


def unepartie(affiche=False,test=False):
    game.joueur1=joueur_alpha_beta
    game.joueur2=joueur_min_max

    jeu=game.initialiseJeu()
    print(jeu[1])
    if test:
        game.changeJoueur(jeu)
        print(jeu[1])
    
    for i in range(4):
       liste=game.getCoupsValides(jeu)
       coup = random.choice(liste)
       game.joueCoup(jeu,coup)
    
    game.affiche(jeu)
    while not game.finJeu(jeu):
       coup= game.saisieCoup(jeu)
       game.joueCoup(jeu,coup)
       if (jeu[1]==1 and game.joueur1==joueur_humain) or (jeu[1]==2 and game.joueur2==joueur_humain):
           game.affiche(jeu)
    game.affiche(jeu)
    if game.getGagnant(jeu)==1:
       print('\033[92m',"\n-------------------------\n")
       print("FELICITATIONS AU JOUEUR 1")
       print("\n-------------------------",'\033[0m')
    elif game.getGagnant(jeu)==2:
       print('\033[91m',"\n-------------------------\n")
       print("FELICITATIONS AU JOUEUR 2")
       print("\n-------------------------",'\033[0m')
    else:
       print("\n-------------------------\n")
       print("EGALITE")
       print("\n-------------------------")

    return game.getGagnant(jeu)

def nparties(n,affiche=True) :
    n1=0
    n2=0
    nul=0
    for i in range (0,n) :
        test=False
        if i%2 == 0:
            test=True
        win=unepartie(affiche,test)
        if (win==1):
            n1+=1
        elif (win==2):
            n2+=1
        else :
            nul+=1
    print("J1 gagne ", n1,"/",n," fois. J2 gagne ",n2,"/",n," fois.",nul,"/",n," nuls\n")
    return

start = time.time()
nparties(20,False)
stop = time.time()
print("time : ",round(stop-start,2))