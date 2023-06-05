# -*- coding: utf-8 -*-
from random import choice,random
from time import sleep
import pygame
from pygame.locals import *
import os.path


#changer "param" l. 218 pour autoriser des jonctions entre couloirs plus fréquemment


class Case:
    def __init__(self,mur=True):
        self.mur=mur

class Laby:
    def __init__(self,cases=[[]]):
        self.nb_lignes=len(cases)
        self.nb_colonnes=len(cases[0])
        self.cases=cases

    def __repr__(self):
        s=''
        for j in range(self.nb_lignes):
            for i in range(self.nb_colonnes):
                if self.cases[j][i].mur:
                    s+='%'
                else:
                    s+=' '
            s+='\n'
        return s

class Pile():
    def __init__(self,sommet=None,base=None):
        #sommet est une valeur, base est une pile
        self.sommet=sommet
        self.base=base

    def est_vide(self):
        return self.sommet==None

    def empile(self,v):
        self.base=Pile(self.sommet,self.base)
        self.sommet=v

    def depile(self):
        tmp=self.sommet
        if self.base!=None:
            self.sommet=self.base.sommet
            self.base=self.base.base
        else:
            self.sommet=None
        return tmp

    def est_present(self,elt):
        Q=Pile()
        result=False
        while (not P.est_vide()) and (not result):
            tmp=P.depile()
            Q.empile(tmp)
            if tmp==elt:
                result=True
        while not Q.est_vide():
            P.empile(Q.depile())
        return result

    def __repr__(self):
        Q=Pile()
        s=""
        while self.sommet!=None:
            tmp=self.depile()
            s+="\t"+str(tmp)+"\n"
            Q.empile(tmp)
        while Q.sommet!=None:
            self.empile(Q.depile())
        return s

Labyrinthe=Laby([[Case() for j in range(15)] for i in range(17)])



w_B = 40 #largeur d'un bloc elle doit etre multiple de 10 (pour des besoins de quotient par 2 et 5)

#les proportions verticales d'un bloc sont evaluees a partir de l'image :
#              0.5 (zone transparente) 0.8 (case de jeu) et 0.4 (socle) si on considere 1 en largeur
h_B = 4*w_B/5 #hauteur finale d'un bloc
h_off=w_B/2 # hauteur partie transparente

pygame.init()
fenetre = pygame.display.set_mode((800, 600))


#GESTION DES OBJETS GRAPHIQUES ET LEUR TAILLE
#remarque : les surfaces creees (et les listes de surfaces pour les objets et les arbres) sont utilisees comme variables globales dans le reste du programme
#blocs :
grass_block = pygame.image.load(os.path.join("images", "Grass Block.png")).convert_alpha()

water_block = pygame.image.load(os.path.join("images", "Water Block.png")).convert_alpha()
grass_block = pygame.transform.smoothscale(grass_block, (w_B,int(grass_block.get_height()*w_B/grass_block.get_width())))
water_block = pygame.transform.smoothscale(water_block, (w_B,int(grass_block.get_height()*w_B/grass_block.get_width())))
grass_block_colored = pygame.image.load(os.path.join("images", "Grass Block.png")).convert_alpha()
grass_block_colored = pygame.transform.smoothscale(grass_block_colored, (w_B,int(grass_block.get_height()*w_B/grass_block.get_width())))

water_block = water_block.subsurface((0,h_off,w_B,h_B))
grass_block = grass_block.subsurface((0,h_off,w_B,h_B))
grass_block_colored = grass_block_colored.subsurface((0,h_off,w_B,h_B))
for i in range(grass_block_colored.get_height()): # colorisation du pnj en mode traque
    for j in range(grass_block_colored.get_width()):
        temp=grass_block_colored.get_at((j,i))
        temp[1]=0
        temp[2]=0
        grass_block_colored.set_at((j,i),temp)

centre_block=[w_B/2,9*w_B/10] #le centre de la case de jeu

#personnage
centre_player=[w_B/2,13*w_B/10] #evaluee a partir de l'image (il est donc deja centre horizontalement)
h_off_player=centre_block[1]-centre_player[1] #pour le centrage vertical

player = pygame.image.load(os.path.join("images", "Character Horn Girl.png")).convert_alpha()
player = pygame.transform.smoothscale(player, (w_B,int(player.get_height()*w_B/player.get_width())))

PV=3 #nombre de points de vie initial du joueur
gagne=[0,0] #initialisaiton des coordonnees de la sortie sur une case inatteignable


nombre_pnj=2 #non utilise dans cette version

pnj = pygame.image.load(os.path.join("images", "Character Cat Girl.png")).convert_alpha()
pnj = pygame.transform.smoothscale(pnj, (w_B,int(pnj.get_height()*w_B/pnj.get_width())))

pnj_aggro = pygame.image.load(os.path.join("images", "Character Cat Girl.png")).convert_alpha()
pnj_aggro = pygame.transform.smoothscale(pnj_aggro, (w_B,int(pnj_aggro.get_height()*w_B/pnj_aggro.get_width())))


for i in range(pnj_aggro.get_height()): # colorisation du pnj en mode traque
    for j in range(pnj_aggro.get_width()):
        temp=pnj_aggro.get_at((j,i))
        temp[0]=0
        pnj_aggro.set_at((j,i),temp)


aggro=1 #initialisation du mode traque du pnj : 1 prend en compte la distance au joueur, 0 non

#objets
nombre_item=25 #total objets

coef_item=0.5 #coef agrandissement/reduction, choisie a partir de l image
centre_item=[int(0.5*w_B*coef_item),int(1.2*w_B*coef_item)] #evaluee a partir de l'image. tient compte de la reduction
w_off_item=centre_block[0]-centre_item[0]
h_off_item=centre_block[1]-centre_item[1]

item_laby = pygame.image.load(os.path.join("images", "Gem Orange.png")).convert_alpha()
item_laby = pygame.transform.smoothscale(item_laby, (int(w_B*coef_item),int(item_laby.get_height()*(w_B*coef_item)/item_laby.get_width())))

item2_laby = pygame.image.load(os.path.join("images", "Enemy Bug.png")).convert_alpha()
item2_laby = pygame.transform.smoothscale(item2_laby, (int(w_B*coef_item),int(item2_laby.get_height()*(w_B*coef_item)/item2_laby.get_width())))

liste_item_laby=[item_laby,item2_laby]

sortie = pygame.image.load(os.path.join("images", "Selector.png")).convert_alpha()
sortie = pygame.transform.smoothscale(sortie, (int(w_B*coef_item),int(sortie.get_height()*(w_B*coef_item)/sortie.get_width())))
#coffres et cles :
#memes parametres d'affichage que les items

chest_closed_laby = pygame.image.load(os.path.join("images", "Chest Closed.png")).convert_alpha()
chest_closed_laby = pygame.transform.smoothscale(chest_closed_laby, (int(w_B*coef_item),int(chest_closed_laby.get_height()*(w_B*coef_item)/chest_closed_laby.get_width())))

chest_open_laby = pygame.image.load(os.path.join("images", "Chest Open.png")).convert_alpha()
chest_open_laby = pygame.transform.smoothscale(chest_open_laby, (int(w_B*coef_item),int(chest_open_laby.get_height()*(w_B*coef_item)/chest_open_laby.get_width())))


key_laby = pygame.image.load(os.path.join("images", "Key.png")).convert_alpha()
key_laby = pygame.transform.smoothscale(key_laby, (int(w_B*coef_item),int(key_laby.get_height()*(w_B*coef_item)/key_laby.get_width())))

#arbres et rochers
centre_tree=[int(0.5*w_B),int(1.3*w_B)]
h_off_tree=centre_block[1]-centre_tree[1]


tree_laby = pygame.image.load(os.path.join("images", "Tree Tall.png")).convert_alpha()
tree_laby = pygame.transform.smoothscale(tree_laby, (w_B,int(tree_laby.get_height()*w_B/tree_laby.get_width())))

rock_laby = pygame.image.load(os.path.join("images", "Rock.png")).convert_alpha()
rock_laby = pygame.transform.smoothscale(rock_laby, (w_B,int(rock_laby.get_height()*w_B/rock_laby.get_width())))

liste_tree_laby=[tree_laby,rock_laby]

########################
def affiche_laby(L,P):
    """L : class Labyrinthe P: class pile (i,j)"""
    for event in pygame.event.get():
        if event.type==QUIT:
            return True
        elif event.type==MOUSEBUTTONDOWN:
            stop=True
            while stop:
                for event in pygame.event.get():
                    if event.type==QUIT:
                        return True
                    elif event.type==MOUSEBUTTONDOWN:
                        stop=False


    for i in range(Labyrinthe.nb_colonnes):
        for j in range(Labyrinthe.nb_lignes):
            if Labyrinthe.cases[j][i].mur:
                fenetre.blit(water_block,(i*w_B,j*h_B))
            else:
                if P.est_present((i,j)):
                    fenetre.blit(grass_block_colored,(i*w_B,j*h_B))
                else:
                    fenetre.blit(grass_block,(i*w_B,j*h_B))
    pygame.display.flip()


P=Pile((1,1))
param=0.8
pause=0.1
stop=False
affiche_laby(Labyrinthe,P)
while not P.est_vide() and not stop:
    i,j=P.depile()
    Labyrinthe.cases[j][i].mur=False
    stop=affiche_laby(Labyrinthe,P)
    sleep(pause)
#    print(i,j)
#    print(Labyrinthe)
#    sleep(0.5)
    directions=[]
    for (x,y) in [(-1,0),(1,0),(0,-1),(0,1)]:
#        print(x,y)
        if 0<i+2*x<Labyrinthe.nb_colonnes-1 and 0<j+2*y<Labyrinthe.nb_lignes-1:
#            print(Labyrinthe.cases[j+2*y][i+2*x].mur)
            if Labyrinthe.cases[j+2*y][i+2*x].mur==True:
                directions.append((x,y))
            elif random()>param:
#                print(i+x,j+x)
                Labyrinthe.cases[j+y][i+x].mur=False
                if not stop:
                    stop=affiche_laby(Labyrinthe,P)
#                print(Labyrinthe)
#                sleep(0.5)
#    print(directions)
    if directions!=[]:
        (x,y)=choice(directions)
        P.empile((i,j))
        P.empile((i+2*x,j+2*y))
#        print(i+x,j+x)
        Labyrinthe.cases[j+y][i+x].mur=False
        if not stop:
            stop=affiche_laby(Labyrinthe,P)
        sleep(pause)
#        print(Labyrinthe)
#        sleep(0.5)



pygame.quit()
