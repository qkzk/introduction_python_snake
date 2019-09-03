'''
Snake vraiment rapide
'''
# -*- coding: utf-8 -*-


import pygame
from pygame.locals import *

HAUTEUR = 600  # hauteur de la fenetre
LARGEUR = 600  # largeur de la fenetre
BLOC = 60

NOIR = (0, 0, 0)
ROUGE = (255, 0, 0)
JAUNE = (255, 255, 0)
VERT = (0, 255, 0)
CYAN = (0, 255, 255)

FPS = 30


############################################################
#####################   GAME INITIALISATION   ##############
############################################################


# pygame
pygame.init()
horloge = pygame.time.Clock()
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption('Snake')

pygame.display.update()

############################################################
#####################   GAME LOOP    #######################
############################################################

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()

    fenetre.fill(NOIR)

    horloge.tick(FPS)
    pygame.display.update()
