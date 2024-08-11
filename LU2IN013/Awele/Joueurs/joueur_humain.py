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
    posx =jeu[1]-1
    posy =int(input("Veuillez entrer la case de votre coup :   "))

    return [posx,posy]
