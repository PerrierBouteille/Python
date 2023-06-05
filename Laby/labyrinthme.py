import os
import sys
import random
import pygame


MUR = 1
VIDE = 0

def fabrique_labyrinthe(largeur, hauteur):

    assert(largeur % 2 == 1)
    assert(hauteur % 2 == 1)
    # Valeur minimale:
    assert(largeur >= 3)
    assert(hauteur >= 3)

    largeur_reelle = (largeur - 1) / 2
    hauteur_reelle = (hauteur - 1) / 2

    laby = []
    for n in range(hauteur):
        ligne = [MUR]*largeur
        laby.append(ligne)

    debut = (1, 1) # La première case à creuser
    compteur = hauteur_reelle*largeur_reelle # Le nombre de cases à
                                             # creuser en tout.
    pile = [debut]
    while compteur > 0:
        # On récupère le dernier élément de la pile. Il est toujours
        # sous la forme (ligne, colonne), ou encore (y, x) avec des
        # notations mathématiques standard.
        y, x = pile[-1]

        # Si la position courante n'est pas encore creusée, on le
        # fait.
        if laby[y][x] == MUR:
            laby[y][x] = VIDE
            compteur = compteur - 1

        # À partir de la position courante, on examine les 4
        # directions cardinales et on regarde s'il est possible de
        # creuser par là (la case d'arrivée, 2 positions plus loin, ne
        # doit pas déjà être creusée). Il faut aussi éviter de sortir
        # des limites du tableau, d'où les nombreux tests.
        directions_possibles = []
        for dy, dx in [(1,0), (-1, 0), (0, 1), (0, -1)]:
            if ((dy == -1 and y > 1) or
                (dy == 1 and y < hauteur - 2) or
                (dx == -1 and x > 1) or
                (dx == 1 and x < largeur - 2)):
                if laby[y+2*dy][x+2*dx] == MUR:
                    # La case de destination est pleine: on peut y
                    # aller.
                    directions_possibles.append((dy, dx))
                else:
                    # La case de destination est déjà utilisée, on ne
                    # peut à priori pas y aller. On s'autorise tout de
                    # même le passage dans 20% des cas, afin de créer
                    # des boucles dans le labyrinthe.
                    if random.random() >= 0.8:
                        directions_possibles.append((dy, dx))

        if len(directions_possibles) == 0:
            # Aucune direction n'est possible à partir du point
            # courant (c'est un cul-de-sac). On "dépile" le dernier
            # élément de notre pile pour revenir un cran en arrière (=
            # on rebrousse chemin).
            pile.pop()
        else:
            # Il existe des directions vers lesquelles on peut
            # creuser. On en choisit donc une au hasard en utilisant
            # la fonction standard random.choice que l'on a importée
            # en début de programme.
            dy, dx = random.choice(directions_possibles)
            # On creuse le mur choisi
            laby[y+dy][x+dx] = 0
            # Et on empile la nouvelle position que l'on vient
            # d'atteindre.
            pile.append((y+2*dy, x+2*dx))

    return laby


labyrinthe=fabrique_labyrinthe(21,21)
print(labyrinthe)

level=labyrinthe

print(len(level))
print(len(level[1]))

j = random.randint(1,19)
k = random.randint(1,13)

level[j][k] = 2

print(level)



class Player(object):

    def __init__(self):
        self.rect = pygame.Rect(32, 32, 16, 16)

    def move(self, dx, dy):

        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)

    def move_single_axis(self, dx, dy):

        # Move the rect
        self.rect.x += dx
        self.rect.y += dy

        # If you collide with a wall, move out based on velocity
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0: # Moving right; Hit the left side of the wall
                    self.rect.right = wall.rect.left
                if dx < 0: # Moving left; Hit the right side of the wall
                    self.rect.left = wall.rect.right
                if dy > 0: # Moving down; Hit the top side of the wall
                    self.rect.bottom = wall.rect.top
                if dy < 0: # Moving up; Hit the bottom side of the wall
                    self.rect.top = wall.rect.bottom

# Nice class to hold a wall rect
class Wall(object):

    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)

# Initialise pygame
os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()

# Set up the display
pygame.display.set_caption("Labyrinthe 1.0")
screen = pygame.display.set_mode((640, 480))

clock = pygame.time.Clock()
walls = [] # List to hold the walls
player = Player() # Create the player

##level = [
##    "WWWWWWWWWWWWWWWWWWWW",
##    "W                  W",
##    "W         WWWWWW   W",
##    "W   WWWW       W   W",
##    "W   W        WWWW  W",
##    "W WWW  WWWW        W",
##    "W   W     W W      W",
##    "W   W     W   WWW WW",
##    "W   WWW WWW   W W  W",
##    "W     W   W   W W  W",
##    "WWW   W   WWWWW W  W",
##    "W W      WW        W",
##    "W W   WWWW   WWW   W",
##    "W     W    E   W   W",
##    "WWWWWWWWWWWWWWWWWWWW",
##]

# Parse the level string above. W = wall, E = exit
x = y = 0
for row in level:
    for col in row:
        if col == 1:
            Wall((x, y))
        if col == 2:
            end_rect = pygame.Rect(x, y, 16, 16)
        x += 16
    y += 16
    x = 0

running = True
while running:

    clock.tick(60)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            running = False

    # Move the player if an arrow key is pressed
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        player.move(-2, 0)
    if key[pygame.K_RIGHT]:
        player.move(2, 0)
    if key[pygame.K_UP]:
        player.move(0, -2)
    if key[pygame.K_DOWN]:
        player.move(0, 2)

    # Just added this to make it slightly fun ;)
    if player.rect.colliderect(end_rect):
        pygame.quit()
        sys.exit()

    # Draw the scene
    screen.fill((0, 0, 0))
    for wall in walls:
        pygame.draw.rect(screen, (255, 255, 255), wall.rect)
    pygame.draw.rect(screen, (255, 0, 0), end_rect)
    pygame.draw.rect(screen, (255, 200, 0), player.rect)
    # gfxdraw.filled_circle(screen, 255, 200, 5, (0,128,0))
    pygame.display.flip()
    clock.tick(360)

pygame.quit()