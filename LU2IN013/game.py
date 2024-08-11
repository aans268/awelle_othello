#!/usr/bin/env python
# -*- coding: utf-8 -*-

# plateau: List[List[nat]]
# liste de listes (lignes du plateau) d'entiers correspondant aux contenus des cases du plateau de jeu

# coup:[nat nat]
# Numero de ligne et numero de colonne de la case correspondante a un coup d'un joueur

# Jeu
# jeu:[plateau nat List[coup] List[coup] List[nat nat]]
# Structure de jeu comportant :
#           - le plateau de jeu
#           - Le joueur a qui c'est le tour de jouer (1 ou 2)
#           - La liste des coups possibles pour le joueur a qui c'est le tour de jouer
#           - La liste des coups joues jusqu'a present dans le jeu
#           - Une paire de scores correspondant au score du joueur 1 et du score du joueur 2

import copy

game=None #Contient le module du jeu specifique: awele ou othello
joueur1=None #Contient le module du joueur 1
joueur2=None #Contient le module du joueur 2


#Fonctions minimales 

def getCopieJeu(jeu):
    """ jeu->jeu
        Retourne une copie du jeu passe en parametre
        Quand on copie un jeu on en calcule forcement les coups valides avant
    """
    getCoupsValides(jeu)
    #jeuclone = copy.deepcopy(jeu)
    jeuclone=initialiseJeu()
    jeuclone[0]=copy.deepcopy(jeu[0])
    jeuclone[1]=copy.deepcopy(jeu[1])
    jeuclone[2]=copy.deepcopy(jeu[2])
    jeuclone[3]=copy.deepcopy(jeu[3])
    jeuclone[4]=copy.deepcopy(jeu[4])  
    return jeuclone

def finJeu(jeu):
    """ jeu -> bool
        Retourne vrai si c'est la fin du jeu
    """
    return game.finJeu(jeu)

def saisieCoup(jeu):
    """ jeu -> coup
        Retourne un coup a jouer
        On suppose que la fonction n'est appelee que si il y a au moins un coup valide possible
        et qu'elle retourne obligatoirement un coup valide
    """
    joueur=joueur1
    if (jeu[1]==2):
        joueur=joueur2
    coup=joueur.saisieCoup(jeu)
    i=0
    while(not coupValide(jeu,coup)):
        if(i==3):
            print("Vous avez saisi trop de coups invalides à la suite.\n --FIN DU JEU--")
            return [-10000,-10000]
        print("Coup non-valide, recommencez!",jeu[1])
        coup=joueur.saisieCoup(jeu)
        i=i+1
    return coup

def getCoupsValides(jeu):
    """ jeu  -> List[coup]
        Retourne la liste des coups valides dans le jeu passe en parametre
        Si None, alors on met � jour la liste des coups valides
    """
    if jeu[2] is None: 
        jeu[2]=game.listeCoupsValides(jeu)
    return jeu[2]

def coupValide(jeu,coup):
    """jeu*coup->bool
        Retourne vrai si le coup appartient a la liste de coups valides du jeu
   """
    if (coup==[]):
            return False
    for c in getCoupsValides(jeu):
        if (c!=[]):
            if (c[0]==coup[0] and c[1]==coup[1]):
                return True
    return False

def joueCoup(jeu,coup):
    """jeu*coup->void
        Joue un coup a l'aide de la fonction joueCoup defini dans le module game
        Hypothese:le coup est valide
        Met tous les champs de jeu à jour (sauf coups valides qui est fixée à None)
    """
    game.joueCoup(jeu,coup)
    #print("dans game.py ",getJoueur(jeu))
    jeu[2]=None  
    #return jeu
    

def initialiseJeu():
    """ void -> jeu
        Initialise le jeu (nouveau plateau, liste des coups joues vide, liste des coups valides None, scores a 0 et joueur = 1)
    """
    jeu= game.initialiseJeu()
    jeu[2]=game.listeCoupsValides(jeu)
    return jeu

def getGagnant(jeu):
    """jeu->nat
    Retourne le numero du joueur gagnant apres avoir finalise la partie. Retourne 0 si match nul
    """
    #game.finalisePartie(jeu)
    if(jeu[4][0]<jeu[4][1]):
        return 2
    if(jeu[4][0]>jeu[4][1]):
        return 1
    return 0

def affiche(jeu):
    """ jeu->void
        Affiche l'etat du jeu de la maniere suivante :
                 Coup joue = <dernier coup>
                 Scores = <score 1>, <score 2>
                 Plateau :

                         |       0     |     1       |      2     |      ...
                    ------------------------------------------------
                      0  | <Case 0,0>  | <Case 0,1>  | <Case 0,2> |      ...
                    ------------------------------------------------
                      1  | <Case 1,0>  | <Case 1,1>  | <Case 1,2> |      ...
                    ------------------------------------------------
                    ...       ...          ...            ...
                 Joueur <joueur>, a vous de jouer
                    
         Hypothese : le contenu de chaque case ne depasse pas 5 caracteres
    """
    print("\nNOUVEAU COUP")
    print("Coups joues = ", jeu[3])
    print("Scores = ", jeu[4][0], ",", jeu[4][1])
    print("Plateau :")
    print("       |",end='')
    for i in range (len(jeu[0][0])):
        print("  ",i,"  |",end='')
    print("")
    for i in range (len(jeu[0])):
        print("--------",end='')
        for j in range (len(jeu[0][i])):
            print("--------",end='')
        print("")
        for j in range (len(jeu[0][i])):
            if (j==0):
                print("  ",i,"  |",end='')
            if len(jeu[0])==2:
                if i==0:
                    print(" ",'\033[92m',jeu[0][i][j],'\033[0m'," |",end='')
                if i==1:
                    print(" ",'\033[91m',jeu[0][i][j],'\033[0m'," |",end='')
            else:
                if jeu[0][i][j]==1:
                    print(" ",'\033[92m',jeu[0][i][j],'\033[0m'," |",end='')
                elif jeu[0][i][j]==2:
                    print(" ",'\033[91m',jeu[0][i][j],'\033[0m'," |",end='')
                else:
                    print("  ",jeu[0][i][j],"  |",end='')
        print("")
    if jeu[1]==1:
        print('\033[92m',"\nA vous de jouer joueur",jeu[1],'\033[0m')
    else:
        print('\033[91m',"\nA vous de jouer joueur",jeu[1],'\033[0m')


# Fonctions utiles

def getPlateau(jeu):
    """ jeu  -> plateau
        Retourne le plateau du jeu passe en parametre
    """
    return jeu[0]

def getCoupsJoues(jeu):
    """ jeu  -> List[coup]
        Retourne la liste des coups joues dans le jeu passe en parametre
    """
    return jeu[3]



def getScores(jeu):
    """ jeu  -> Pair[nat nat]
        Retourne les scores du jeu passe en parametre
    """
    return jeu[4]

def getJoueur(jeu):
    """ jeu  -> nat
        Retourne le joueur a qui c'est le tour de jouer dans le jeu passe en parametre
    """
    return jeu[1]



def changeJoueur(jeu):
    """ jeu  -> void
        Change le joueur a qui c'est le tour de jouer dans le jeu passe en parametre (1 ou 2)
    """
    jeu[1]=3-jeu[1] 

def getScore(jeu,joueur):
    """ jeu*nat->int
        Retourne le score du joueur
        Hypothese: le joueur est 1 ou 2
    """
    return jeu[4][joueur-1]

def getCaseVal(jeu, ligne, colonne):
    """ jeu*nat*nat -> nat
        Retourne le contenu de la case ligne,colonne du jeu
        Hypothese: les numeros de ligne et colonne appartiennent bien au plateau  : ligne<=getNbLignes(jeu) and colonne<=getNbColonnes(jeu)
    """
    return jeu[0][ligne][colonne]
    
    




