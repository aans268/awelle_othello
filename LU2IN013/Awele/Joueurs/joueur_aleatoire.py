#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("../..")
import game
import random

def saisieCoup(jeu):
    """ jeu -> coup
        Retourne un coup a jouer
    """
    #posx=jeu[1]-1
    liste=game.getCoupsValides(jeu)
    #posy=liste[random.randint(0,len(liste)-1)][1]

    return random.choice(liste)