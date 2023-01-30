import pygame
from pygame.locals import *
from random import *
from time import *


pygame.init()
screen = pygame.display.set_mode((400,400))
pygame.display.set_caption("Cubex v1.0.0 | Beta Dev")
class Texte :
    '''______Afficher un texte_____
       les attributs :
       - texte
       - taille de la font
       - couleur - position
       @ -la police sera celle par défaut , sa suffira bien ^^
    '''
    def __init__(self, texte, taille, couleur, position):
        self.texte = texte
        self.taille = taille
        self.couleur = couleur
        self.position = position


    def affiche (self):

        font = pygame.font.Font(None, self.taille)
        text = font.render(self.texte, 1, self.couleur)
        text_pos = text.get_rect()
        text_pos.center = (self.position)

        screen.blit(text, text_pos)

#
nav_x,nav_y=200,200
minicube = 0
mine = 0
tx,ty=0,0
menu,play=1,0
over=0
overc=0
haut,bas,droite,gauche=0,0,0,0

while True:
    while menu:
        textMenu = Texte('Entrée pour jouer', 50, (0,250,0), (200,200 + 45)).affiche()
        for event in pygame.event.get():
            if event.type == KEYDOWN :
                menu,play=0,1
                screen.fill((0,0,0))
        pygame.display.flip()
    while play:
        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                exit()
            if (event.type == KEYDOWN and over==0) :
                if event.key == K_UP:

                    haut,bas,droite,gauche=1,0,0,0
                if event.key == K_DOWN:

                    haut,bas,droite,gauche=0,1,0,0
                if event.key == K_LEFT:

                    haut,bas,droite,gauche=0,0,0,1
                if event.key == K_RIGHT:

                    haut,bas,droite,gauche=0,0,1,0
        if(over==0):
            if(haut==1):
                pygame.draw.rect(screen, (0,0,0), Rect((nav_x,nav_y),(10+tx,10+ty)))
                sleep(0.1)
                nav_y -=5

            if(bas==1):
                pygame.draw.rect(screen, (0,0,0), Rect((nav_x,nav_y),(10+tx,10+ty)))
                sleep(0.1)
                nav_y += 5

            if(droite==1):
                pygame.draw.rect(screen, (0,0,0), Rect((nav_x,nav_y),(10+tx,10+ty)))
                sleep(0.1)
                nav_x +=5

            if(gauche==1):
                pygame.draw.rect(screen, (0,0,0), Rect((nav_x,nav_y),(10+tx,10+ty)))
                sleep(0.1)
                nav_x -=5

        if(minicube == 0):
            minicube = 1
            x = randint(100,300)
            y = randint (100,300)
            pygame.draw.rect(screen, (0,250,0), Rect((x,y),(5,5)))
        if(x+10+tx > nav_x > x-10-tx and y+10+ty> nav_y > y-10-ty):
            pygame.draw.rect(screen, (0,0,0), Rect((x,y),(5,5)))
            minicube = 0
            x=-10000
            y=-10000
            tx+=2
            ty+=2
        else:
            pygame.draw.rect(screen, (0,250,0), Rect((x,y),(5,5)))
        if(mine == 0):
            mine = 1
            xm = randint(100,300)
            ym = randint(100,300)
            pygame.draw.rect(screen, (0,0,250), Rect((xm,ym),(5,5)))
        if(xm+10+tx > nav_x > xm-10-tx and ym+10+ty > nav_y > ym-10-ty):
            pygame.draw.rect(screen, (0,0,0), Rect((xm,ym),(5,5)))
            xm=-10000
            xy=-10000
            over = 1
        else:
            pygame.draw.rect(screen, (0,0,250), Rect((xm,ym),(5,5)))
        if(over==1):
            overc+=1
            pygame.draw.rect(screen, (250,5,5), Rect((nav_x,nav_y),(10+tx,10+ty)))
            pygame.display.flip()
            pygame.draw.rect(screen, (250,185,5), Rect((nav_x,nav_y),(10+tx,10+ty)))
            pygame.display.flip()
            pygame.draw.rect(screen, (0,0,0), Rect((nav_x,nav_y),(10+tx,10+ty)))
            textMenu = Texte('Game Over', 50, (0,250,0), (200,200 + 25)).affiche()
            textMenu = Texte('Score: ' + str(tx//2)+ "", 25, (0,250,0), (200,200 + 45)).affiche()
            pygame.display.flip()
            if(overc>=250):
                pygame.quit()
                exit()
                break

        #print(x, " | ",y)
        #print(nav_x," | ",nav_y)
        pygame.draw.rect(screen, (250,5,5), Rect((nav_x,nav_y),(10+tx,10+ty)))
        pygame.draw.rect(screen, (0,0,0), Rect((0,0),(75,25)))
        score = Texte('Score: ' + str(tx//2) + "", 20, (255,255,255), (35,15)).affiche()
        pygame.display.flip()
        #(46,52,54),((0,200),(500,275)
