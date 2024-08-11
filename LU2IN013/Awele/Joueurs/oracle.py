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
    #print(listecv)
    if joueur == 1:
        bestone=listecv[0]
    else: 
        bestone=listecv[-1]
    
    est_list = []
    alpha=0
    beta=0
    for coup in listecv:
        val=estimation(jeu,coup,3,alpha,beta)
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

def estimation(jeu,coup,profondeur,alpha,beta):
    jeuclone=game.getCopieJeu(jeu)
    game.joueCoup(jeuclone,coup)
    if profondeur==0:
        return evaluation(jeu)
    if game.finJeu(jeu):
        if jeu[4][joueur-1]>jeu[4][2-joueur]:
            return 100000 #bcp psq win condition
        if jeu[4][joueur-1]<jeu[4][2-joueur]:
            return -100000 #loose
        if jeu[4][joueur-1]==jeu[4][2-joueur]:
            return 0 #draw
    if jeuclone[1]==1:
        return minValue(jeuclone,profondeur,alpha,beta)
    else :
        return maxValue(jeuclone,profondeur,alpha,beta)


def maxValue(jeu,profondeur,alpha,beta):
    liste=game.getCoupsValides(jeu)
    #print("liste:",liste)
    m=-100000
    for c in liste:
        if(m>beta):
            return m
        #jeuclone=game.getCopieJeu(jeu)
        m = max(m,estimation(jeu,c,profondeur-1,alpha,beta))     
        alpha=max(m,alpha)
    return m

def minValue(jeu,profondeur,alpha,beta):
    liste=game.getCoupsValides(jeu)
    #print("liste:",liste)
    m=100000
    for c in liste:
        if(m<alpha):
            return m
        #jeuclone=game.getCopieJeu(jeu)
        m = min(m,estimation(jeu,c,profondeur-1,alpha,beta))
        beta=min(m,beta)
    return m

def evaluation(jeu):
    return diffscore(jeu)#+puit(jeu)+nbcases_mangeable(jeu)

def diffscore(jeu):
    score_joueur = jeu[4][joueur-1]
    score_advers = jeu[4][2-joueur]
    #ipdb.set_trace()
    return score_joueur-score_advers

def puit(jeu):
    for i in range(2):
        for j in range(6):
            if jeu[0][i][j]>=12:
                return 2
    return 0

def nbcases_mangeable(jeu):
    res=0
    for i in range(6):
        if jeu[0][joueur-1][i]<=2:
            res-=0.5
        if jeu[0][2-joueur][i]<=2:
            res+=0.5
    return res


def get_est_list(jeu,listecv):
    max_score=-1000000000000000000000
    
    if joueur == 1:
        bestone=listecv[0]
    else: 
        bestone=listecv[-1]
    
    est_list = []
    alpha=0
    beta=0
    for coup in listecv:
        val=estimation(jeu,coup,5,alpha,beta)
        est_list.append(val)
        #print(coup,val)
        if val>max_score:
            max_score=val
            bestone=coup
    return est_list