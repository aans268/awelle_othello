#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("../..")
import game

def saisieCoup(jeu):
    """ jeu -> coup
        Retourne un coup a jouer
    """
    liste=game.getCoupsValides(jeu)
    cp=decision(jeu,liste)
    #print("cp:",cp)
    
    posx=cp[0]
    posy=cp[1]

    return cp

def decision(jeu,listecv):
    score=-1000000000000000000000
    bestone=listecv[0]
    alpha=0
    beta=0
    for coup in listecv:
        val=estimation(coup,jeu,coup,2,jeu[1],alpha,beta)
        if val>score:
            score=val
            bestone=coup
    return bestone

def estimation(coupdebase,jeu,coup,profondeur,joueur,alpha,beta):
    jeuclone=game.getCopieJeu(jeu)
    game.joueCoup(jeuclone,coup)
    if profondeur==0:
        return evaluation(coupdebase,jeu,joueur)
    if game.finJeu(jeu):
        if jeu[4][joueur-1]>jeu[4][2-joueur]:
            return 100000 #bcp psq win condition
        if jeu[4][joueur-1]<jeu[4][2-joueur]:
            return -100000 #loose
        if jeu[4][joueur-1]==jeu[4][2-joueur]:
            return 0 #draw
    if jeuclone[1]==1:
        return minValue(coup,jeuclone,profondeur,joueur,alpha,beta)
    else :
        return maxValue(coup,jeuclone,profondeur,joueur,alpha,beta)


def maxValue(coupdebase,jeu,profondeur,joueur,alpha,beta):
    liste=game.getCoupsValides(jeu)
    #print("liste:",liste)
    m=-100000
    for c in liste:
        if(m>beta):
            return m
        #jeuclone=game.getCopieJeu(jeu)
        m = max(m,estimation(coupdebase,jeu,c,profondeur-1,joueur,alpha,beta))     
        alpha=max(m,alpha)
    return m

def minValue(coupdebase,jeu,profondeur,joueur,alpha,beta):
    liste=game.getCoupsValides(jeu)
    #print("liste:",liste)
    m=100000
    for c in liste:
        if(m<alpha):
            return m
        #jeuclone=game.getCopieJeu(jeu)
        m = min(m,estimation(coupdebase,jeu,c,profondeur-1,joueur,alpha,beta))
        beta=min(m,beta)
    return m

def evaluation(coupdebase,jeu,joueur):
    return diffscore(jeu,joueur)*2+bordure(coupdebase)+bandeau(coupdebase,jeu,joueur)+centre(jeu,joueur)+mobilite(jeu)+presque_bordure(coupdebase)

def diffscore(jeu, joueur):
    score_joueur = jeu[4][joueur-1]
    score_advers = jeu[4][2-joueur]
    #ipdb.set_trace()
    return score_joueur-score_advers

def bordure(coupdebase):
    score=0
    if coupdebase[0]==0 or coupdebase[0]==7:
        score=score+1
    if coupdebase[1]==0 or coupdebase[1]==7:
        score=score+1
    return score

def bandeau(coupdebase,jeu,joueur):
    val=joueur+1
    score=0
    for i in range(8):
        if jeu[0][coupdebase[0]][i]!=val:
            break
    if  i==7:
        score=score + 1

    for i in range(8):
        if jeu[0][i][coupdebase[1]]!=val:
            break
    if i==7:
        score=score+1

    return score

def centre(jeu,joueur):
    score=0
    if jeu[0][3][3]==joueur+1:
        score=score+0.5
    if jeu[0][3][4]==joueur+1:
        score=score+0.5
    if jeu[0][4][3]==joueur+1:
        score=score+0.5
    if jeu[0][4][4]==joueur+1:
        score=score+0.5
    return score

def mobilite(jeu):
    l=len(game.getCoupsValides(jeu))
    jeu[2]=None
    return l

def presque_bordure(coupdebase):
    if (coupdebase[0]==1 or coupdebase[0]==6 or coupdebase[1]==1 or coupdebase[1]==6):
        return -0.5
    return 0