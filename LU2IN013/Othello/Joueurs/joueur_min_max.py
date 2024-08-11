#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("../..")
import game
#import ipdb
import random

def saisieCoup(jeu):
    """ jeu -> coup
        Retourne un coup a jouer
    """
    global joueur
    joueur = game.getJoueur(jeu)
    liste=game.getCoupsValides(jeu)
    cp=decision(jeu,liste)
    #print("cp:",cp)
    if (cp==[]):
        return []

    return cp

def decision(jeu,listecv):
    max_score=-1000000000000000000000
    
    if joueur == 1:
        bestone=listecv[0]
    else: 
        bestone=listecv[-1]
    
    est_list = []

    for coup in listecv:
        val=estimation(jeu,coup,1)
        est_list.append(val)
        #print(coup,val)
        if val>max_score:
            max_score=val
            bestone=coup

    best_list = []
    for i in range(len(listecv)):
        if est_list[i] == max_score:
            best_list.append(listecv[i])
    #print("BESTONE : ",score)
    return random.choice(best_list)

def estimation(jeu,coup,profondeur):
    jeuclone=game.getCopieJeu(jeu)
    game.joueCoup(jeuclone,coup)
    if profondeur==0:
        return evaluation(jeuclone)
    if game.finJeu(jeuclone):
        if jeuclone[4][joueur-1]>jeuclone[4][2-joueur]:
            return 100000 #bcp psq win condition
        if jeuclone[4][joueur-1]<jeuclone[4][2-joueur]:
            return -100000 #loose
        if jeuclone[4][joueur-1]==jeuclone[4][2-joueur]:
            return -1000 #draw
    if game.getJoueur(jeuclone) == joueur:
        return maxValue(jeuclone,profondeur)
    else :
        return minValue(jeuclone,profondeur)


def maxValue(jeu,profondeur):
    liste=game.getCoupsValides(jeu)
    m=-100000
    for c in liste:
        #jeuclone=game.getCopieJeu(jeu)
        m = max(m,estimation(jeu,c,profondeur-1))
    return m

def minValue(jeu,profondeur):
    liste=game.getCoupsValides(jeu)
    m=100000
    for c in liste:
        #jeuclone=game.getCopieJeu(jeu)
        m = min(m,estimation(jeu,c,profondeur-1))
    return m

def evaluation(jeu):
    return diffscore(jeu)

def diffscore(jeu):
    score_joueur = jeu[4][joueur-1]
    score_advers = jeu[4][2-joueur]
    #ipdb.set_trace()
    return score_joueur-score_advers