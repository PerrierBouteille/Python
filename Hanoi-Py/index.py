#=== Import des modules
import pygame
from pygame.locals import *
from random import *
from src.solver import *
from src.MainConstructor import *
from src.MainTower import *

#

Prefix = "Hanoï"

#

class TextProgress:
    def __init__(self, font, message, color, bgcolor):
        self.font = font
        self.message = message
        self.color = color
        self.bgcolor = bgcolor
        self.offcolor = [c^40 for c in color]
        self.notcolor = [c^0xFF for c in color]
        self.text = font.render(message, 0, (255,0,0), self.notcolor)
        self.text.set_colorkey(1)
        self.outline = self.textHollow(font, message, color)
        self.bar = pygame.Surface(self.text.get_size())
        self.bar.fill(self.offcolor)
        width, height = self.text.get_size()
        stripe = Rect(0, height/2, width, height/4)
        self.bar.fill(color, stripe)
        self.ratio = width / 100.0

    def textHollow(self, font, message, fontcolor):
        base = font.render(message, 0, fontcolor, self.notcolor)
        size = base.get_width() + 2, base.get_height() + 2
        img = pygame.Surface(size, 16)
        img.fill(self.notcolor)
        base.set_colorkey(0)
        img.blit(base, (0, 0))
        img.blit(base, (2, 0))
        img.blit(base, (0, 2))
        img.blit(base, (2, 2))
        base.set_colorkey(0)
        base.set_palette_at(1, self.notcolor)
        img.blit(base, (1, 1))
        img.set_colorkey(self.notcolor)
        return img

    def render(self, percent=50):
        surf = pygame.Surface(self.text.get_size())
        if percent < 100:
            surf.fill(self.bgcolor)
            surf.blit(self.bar, (0,0), (0, 0, percent*self.ratio, 100))
        else:
            surf.fill(self.color)
            global finished
            finished = 1
            global Menu
            Menu = 1

        surf.blit(self.text, (0,0))
        #surf.blit(self.outline, (-1,-1))
        surf.set_colorkey(self.notcolor)
        return surf

entry_info = '/////////////////////////'
ch = 0

if __name__ == '__main__':
    import random
    pygame.init()
    pygame.display.set_caption(Prefix)
    screen = pygame.display.set_mode((500, 600))

    font = pygame.font.Font(None, 60)
    font2 = pygame.font.SysFont('Comic Sans MS,Arial', 24)
    white = 0, 225, 0
    renderer = TextProgress(font, entry_info, white, (40, 40, 40))
    text = renderer.render(0)

    screen.blit(text, (115, 330))
    bar1 = font.render(' ____________ ', True, (255,255,255))
    bar2 = font.render('|____________|', True, (255,255,255))
    author = font2.render('Chargement en cours..', True, (255,255,255))
    screen.blit(author, (130,280))
    screen.blit(bar1, (105,290))
    screen.blit(bar2, (105,330))

    pygame.display.flip()

    progress = 1

    finished = 0
    while not finished:
        dly = randint(160,640)
        pygame.time.delay(120)
        ch += 1
        for event in pygame.event.get():
            if event.type in (QUIT,KEYDOWN,MOUSEBUTTONDOWN):
                finished = 1

        progress = (progress + random.randint(0,3)) % 120
        text = renderer.render(progress)
        screen.blit(text, (115, 330))
        pygame.display.flip()

#▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬

Menu = 1

screen = pygame.display.set_mode((500,600))

n = 3

#▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
while True:
    while Menu:
        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if 50 <= mouse[0] <= 500 and 350 <= mouse[1] <= 500:
                    Menu = 0
                    Play = 1
                    Creation(n)
        screen.fill((5,5,5))
        cadre = Draw_rect().gen((0, 0, 0),((50,350),(400,100)),screen)
        cadre = Draw_rect().gen((0, 25, 0),((55,355),(395,95)),screen)
        textMenu = Texte('Start', 75, (10,200,10), (cadre.centerx,cadre.top + 45), 'ressources/04B_30__.TTF').affiche(screen)
        pygame.display.flip()
    while Play:
        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                print(mouse)
                if 375 <= mouse[0] <= 505 and 500 <= mouse[1] <= 575:
                    RunSolver(n)
        screen.fill((5,5,5))
        cadre = Draw_rect().gen((0, 0, 0),((370,500),(120,75)),screen)
        cadre = Draw_rect().gen((0, 25, 0),((375,505),(115,70)),screen)
        textMenu = Texte('Solver', 20, (10,200,10), (cadre.centerx,cadre.top + 35), 'ressources/04B_30__.TTF').affiche(screen)
        for i in range(n):
            print(str(Affichage(n)))
            ToH = Texte(str(Affichage(n)), 45, (250,250,250), (150,50), 'ressources/04B_30__.TTF').affiche(screen)
        pygame.display.flip()