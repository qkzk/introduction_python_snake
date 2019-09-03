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


def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, CYAN)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

############################################################
#####################   GAME INITIALISATION   ##############
############################################################


pygame.init()
horloge = pygame.time.Clock()
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption('Snake')

# taille et type de la fonte
font = pygame.font.SysFont(None, 48)

pygame.display.update()

############################################################
#####################   GAME LOOP    #######################
############################################################
score = 0
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
    key = pygame.key.get_pressed()
    if key:
        if key[pygame.K_UP]:
            print("up")
        if key[pygame.K_DOWN]:
            print("down")
        if key[pygame.K_LEFT]:
            print("left")
        if key[pygame.K_RIGHT]:
            print("right")
    fenetre.fill(NOIR)
    drawText(str(score), font, fenetre, 0.2*LARGEUR, 0.2*HAUTEUR)
    horloge.tick(FPS)
    pygame.display.update()
