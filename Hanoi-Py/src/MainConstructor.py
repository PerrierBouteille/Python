#=== Import des modules
from cProfile import run
import pygame
from pygame.locals import *
from random import *
import yaml
from operator import itemgetter
from time import *



def Image(image):
    '''____Fonction de chargement d'image___
       - nom de l'image
       - attribut alpha : Bool
    '''

    x =pygame.image.load(image).convert_alpha()
    return x

class Draw_rect :
    '''______Création de rectange(s)______
       - 2 méthodes possibles :
             1 - gen -> dessine 1 carré
                     - couleur
                     - position
             2 - gen_bg -> dessine les 4 carrés formant le fond
    '''
    def __init__(self):
        pass

    def gen(self,couleur,position,screen):
        x = pygame.draw.rect(screen, couleur, Rect(position))
        return x

    def gen_bg(self):
        n = 0
        while n != len(couleur_sombre):
            x = pygame.draw.rect(screen, couleur_sombre[n], Rect(liste_pos[n]))
            n += 1

class Texte :
    '''______Afficher un texte_____
       les attributs :
       - texte
       - taille de la font
       - couleur - position
       @ -la police sera celle par défaut , sa suffira bien ^^
    '''
    def __init__(self, texte, taille, couleur, position, texture):
        self.texte = texte
        self.taille = taille
        self.couleur = couleur
        self.position = position
        self.texture = texture


    def affiche (self,screen):

        font = pygame.font.Font(self.texture, self.taille)
        text = font.render(self.texte, 1, self.couleur)
        text_pos = text.get_rect()
        text_pos.center = (self.position)

        screen.blit(text, text_pos)