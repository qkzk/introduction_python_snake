'''
Snake vraiment rapide

Snake réalisé "simplement" en Pygame avec Python 3.
Nécessite Pygame et Python 3.7

1 seule fonction,
le reste est directement dans la boucle infinie.


Auteur : qkzk
Date : 2019/09/03

'''
# -*- coding: utf-8 -*-

# pour choisir où faire apparaître la nouvelle pomme
from random import randint
# la librairie pygame
import pygame
# afin de quitter le jeu proprement
from pygame.locals import *


# Les dimensions de la fenêtre
HAUTEUR = 600  # hauteur de la fenetre
LARGEUR = 600  # largeur de la fenetre
# Ainsi que celle d'un carré à l'écran : 60 pixels
BLOC = 60

# Les couleurs utilisées
NOIR = (0, 0, 0)  # fond
ROUGE = (255, 0, 0)  # pomme
JAUNE = (255, 255, 0)  # tête
VERT = (0, 255, 0)  # corps
CYAN = (0, 255, 255)  # texte

# Vitesse de rafaîchissement du jeu
FPS = 30
# On effectue les calculs toutes les 15 frames
MAJ = 15


############################################################
#####################   Fonctions             ##############
############################################################


def drawText(text, font, surface, x, y):
    '''
    Dessine du texte à l'écran
    @param text: (str) le texte
    @param font: (pygame.font) la police
    @param surface: (pygame.surface) la surface sur laquelle écrire
    @param x, y: (int) les coordonnées du texte
    '''
    textobj = font.render(text, 1, CYAN)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


############################################################
#####################   GAME INITIALISATION   ##############
############################################################


# pygame
# les éléments indispensables sont init, time.Clock()  et un
# display
pygame.init()
horloge = pygame.time.Clock()
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
# titre de la fenêtre
pygame.display.set_caption('Snake')

# taille et type de la fonte
font = pygame.font.SysFont(None, 48)

# on met immédiatement à jour avant de commencer
pygame.display.update()

############################################################
#####################   GAME LOOP    #######################
############################################################

# les éléments du jeu
# le serpent est un tableau à 2 dimensions.
# le premier est la tête, les suivants le corps
# chaque élément est une liste de cooordonnées [abs, ord]
snake = [[3, 3], [2, 3], [1, 3]]
direction = (1, 0)
pomme = [8, 3]

# le score est un entier
score = 0

# compteur de frame pour les mises à jour
compteur = 0

while True:
    # Saisies de l'utilisateur

    # quitter le jeu
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()

    # déplacer le serpent
    key = pygame.key.get_pressed()
    if key:
        if key[pygame.K_UP]:
            # on change la direction vers le haut
            direction = (0, -1)
        if key[pygame.K_DOWN]:
            # on change la direction vers le bas
            direction = (0, 1)
        if key[pygame.K_LEFT]:
            # on change la direction vers la gauche
            direction = (-1, 0)
        if key[pygame.K_RIGHT]:
            # on change la direction vers la droite
            direction = (1, 0)

    # Calculs
    # ils ne sont effectués que toutes les 15 frames
    if compteur == MAJ:
        # on reset le compteur
        compteur = 0

        # la nouvelle tête est l'ancienne, déplacée dans la direction
        head = [snake[0][0] + direction[0], snake[0][1] + direction[1]]

        # on l'insère au début
        snake.insert(0, head)

        # collision tête / pomme
        if snake[0] == pomme:
            # on augmente le score
            score += 1
            # on déplace la pomme en dehors du corps
            while pomme in snake:
                # nécessaire de tirer plusieurs fois si on n'a
                # pas de chance !
                pomme = [randint(0, LARGEUR / BLOC - 1),
                         randint(0, HAUTEUR / BLOC - 1)]
        else:
            # si le serpent n'a pas mangé la pomme, il diminue
            snake.pop(-1)

        # mort du serpent
        # s'il touche son corps
        # ou s'il quitte l'écran
        if head in snake[1:] \
                or head[0] < 0 \
                or head[0] > LARGEUR / BLOC - 1 \
                or head[1] < 0 \
                or head[1] > HAUTEUR / BLOC - 1:
            pygame.quit()

    # Graphiques

    # d'abord on remplit de noir pour cacher les images précédentes
    fenetre.fill(NOIR)
    # Ensuite on dessine le corps en vert
    for elt in snake[1:]:
        pygame.draw.rect(fenetre, VERT,
                         (elt[0] * BLOC, elt[1] * BLOC, BLOC, BLOC))

    # la tête en jaune
    pygame.draw.rect(fenetre, JAUNE,
                     (snake[0][0] * BLOC, snake[0][1] * BLOC, BLOC, BLOC))

    # la pomme en rouge
    pygame.draw.rect(fenetre, ROUGE,
                     (pomme[0] * BLOC, pomme[1] * BLOC, BLOC, BLOC))

    # le score dans le coin de l'écran
    drawText(str(score), font, fenetre, 0.2 * LARGEUR, 0.2 * HAUTEUR)

    # On met pygame à jour
    # en avançant l'horloge
    horloge.tick(FPS)
    # en dessinant les éléments
    pygame.display.update()
    # et comptant les frames
    compteur += 1
