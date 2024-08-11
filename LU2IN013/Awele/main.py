#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import awele
import sys
sys.path.append("..")
import game
game.game=awele
sys.path.append("./Joueurs")
import joueur_humain
import joueur_aleatoire
import jab
import jtest
import oracle
import joueur_min_max
import random
import copy

#game.joueur1=joueur_aleatoire
#game.joueur2=joueur_aleatoire
#jeu=game.initialiseJeu()
#for i in range(4):
#    coup= game.saisieCoup(jeu)
#    game.joueCoup(jeu,coup)
#game.joueur1=joueur_min_max
#game.joueur2=joueur_aleatoire
#game.affiche(jeu)
#while not game.finJeu(jeu):
#    coup= game.saisieCoup(jeu)
#    game.joueCoup(jeu,coup)
#    if (jeu[1]==1 and game.joueur1==joueur_humain) or (jeu[1]==2 and game.joueur2==joueur_humain):
#        game.affiche(jeu)
#game.affiche(jeu)
#if game.getGagnant(jeu)==1:
#    print('\033[92m',"\n-------------------------\n")
#    print("FELICITATIONS AU JOUEUR 1")
#    print("\n-------------------------",'\033[0m')
#elif game.getGagnant(jeu)==2:
#    print('\033[91m',"\n-------------------------\n")
#    print("FELICITATIONS AU JOUEUR 2")
#    print("\n-------------------------",'\033[0m')
#else:
#    print("\n-------------------------\n")
#    print("EGALITE")
#    print("\n-------------------------")
def unepartie(affiche=False,test=False,j1=None,j2=None):
    if j1 is None:
        game.joueur1=jab
    else:
        game.joueur1=j1
    if j2 is None:
        game.joueur2=oracle
    else:
        game.joueur2=j2

    jeu=game.initialiseJeu()
    #print(jeu[1])
    if test:
        game.changeJoueur(jeu)
        #print(jeu[1])
    
    for i in range(4):
       liste=game.getCoupsValides(jeu)
       coup = random.choice(liste)
       game.joueCoup(jeu,coup)
    
    #game.affiche(jeu)
    while not game.finJeu(jeu):
       coup= game.saisieCoup(jeu)
       game.joueCoup(jeu,coup)
       if (jeu[1]==1 and game.joueur1==joueur_humain) or (jeu[1]==2 and game.joueur2==joueur_humain):
           game.affiche(jeu)
    #game.affiche(jeu)
    #if game.getGagnant(jeu)==1:
    #   print('\033[92m',"\n-------------------------\n")
    #   print("FELICITATIONS AU JOUEUR 1")
    #   print("\n-------------------------",'\033[0m')
    #elif game.getGagnant(jeu)==2:
    #   print('\033[91m',"\n-------------------------\n")
    #   print("FELICITATIONS AU JOUEUR 2")
    #   print("\n-------------------------",'\033[0m')
    #else:
    #   print("\n-------------------------\n")
    #   print("EGALITE")
    #   print("\n-------------------------")

    return game.getGagnant(jeu)

def nparties(n,affiche=True,j1=None,j2=None) :
    n1=0
    n2=0
    nul=0
    for i in range (0,n) :
        test=False
        if i%2 == 0:
            test=True
        win=unepartie(affiche,test,j1,j2)
        if (win==1):
            n1+=1
        elif (win==2):
            n2+=1
        else :
            nul+=1
    print("J1 gagne ", n1,"/",n," fois. J2 gagne ",n2,"/",n," fois.",nul,"/",n," nuls\n")
    return n1/n

def nentrainements() :
    res=jab.w
    epsilon=0.99
    best=0
    while(True):    
        modif_w(epsilon) #on prend une nvelle valeur de w[i]
        epsilon=epsilon/1.5 #on affine epsilon
        if epsilon<0.001:
            epsilon=0.99
        winrate=nparties(30,False)
        print(winrate)
        if winrate>best: #on compare les taux de victoires pour stocker la meilleure valeur
            best=winrate
            res=copy.deepcopy(jab.w)
        print("epsilon:",epsilon)
        print("w:",jab.w)
        print("res:",res)
    return

def training_oracle():
    game.joueur1=jab
    game.joueur2=oracle
    epsilon=1
    print("debut:w=",jab.w)
    stats=0
    while epsilon>0.001:
        print("Nouvelle partie, epsilon : ",epsilon)
        jeu=game.initialiseJeu()
        jab.joueur = game.getJoueur(jeu)
        oracle.joueur = 3-game.getJoueur(jeu)
        for i in range(4):
            liste=game.getCoupsValides(jeu)
            coup = random.choice(liste)
            game.joueCoup(jeu,coup)
        while(not game.finJeu(jeu)):
            #game.affiche(jeu)
            if game.getJoueur(jeu)==jab.joueur :
                liste=game.getCoupsValides(jeu)
                o=oracle.get_est_list(jeu,liste)
                opt=max(o)
                coup_opt=0
                for c in range(len(o)):
                    if o[c] == opt:
                        coup_opt=liste[c]
                        break
                jeuclone1=game.getCopieJeu(jeu)
                game.joueCoup(jeuclone1,coup_opt)
                a = jab.evaluation(jeuclone1)
                #a=jab.estimation(jeu,coup_opt,5,0,0)
                for c in range(len(o)):
                #pour plus tard, faire courbe entre le nb de test et le nb de fois où les joueurs sont d'accord
                    if o[c]<opt:
                        jeuclone2=game.getCopieJeu(jeu)
                        game.joueCoup(jeuclone2,liste[c])
                        s = jab.evaluation(jeuclone2)
                        #s=jab.estimation(jeu,liste[c],1,0,0)
                        if (a-s)<1:
                            scj_opt=jab.scores(jeuclone1)
                            scj_c=jab.scores(jeuclone2)
                            for i in range(len(jab.w)):
                                jab.w[i]=jab.w[i]-epsilon*(scj_c[i]-scj_opt[i])
                            print("modification de w : ",jab.w)
            coup=game.saisieCoup(jeu)
            game.joueCoup(jeu,coup)
        print("FIN de la partie")

        # toute les n parties -> stats moi vs oracle
        epsilon=epsilon*0.8
        new_stats=nparties(20,True,game.joueur1,game.joueur2)
        if new_stats>stats:
            print("EN PROGRESSION : ",new_stats," > ",stats)
            stats=new_stats
    print("w = ",jab.w)


def modif_w(epsilon):
    jab.w[0]=jab.w[0]+random.uniform(-1,1)*epsilon
    jab.w[1]=jab.w[1]+random.uniform(-1,1)*epsilon
    jab.w[2]=jab.w[2]+random.uniform(-1,1)*epsilon
    jab.w[3]=jab.w[3]+random.uniform(-1,1)*epsilon

start = time.time()

#res: [1.6626411662030158, 1.8492668126862077, 1.0821912930059137, 0.07271407716855591]
#res(apres 1h):[0.858815540342964, -0.4937784334738966, 0.15575670269315436, 0.28592949554147273]

nparties(20,False,jab,joueur_min_max)
#nentrainements()
#training_oracle()
stop = time.time()
print("time : ",round(stop-start,2))