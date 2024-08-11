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
    liste=game.getCoupsValides(jeu)
    cp= liste[random.randint(0,len(liste)-1)]
    posx=cp[0]
    posy=cp[1]

    return [posx,posy]