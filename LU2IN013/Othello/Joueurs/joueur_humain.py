#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("../..")
import game

def saisieCoup(jeu):
    """ jeu -> coup
        Retourne un coup a jouer
    """
    print(game.getCoupsValides(jeu))
    posx =int(input("Veuillez entrer la coordonnée x de votre coup :   "))
    posy =int(input("Veuillez entrer la coordonnée y de votre coup :   "))

    return [posx,posy]

    
