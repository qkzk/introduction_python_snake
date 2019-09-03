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

FPS = 3


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
snake = [[3, 3], [2, 3], [1, 3]]
direction = (1, 0)

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
            direction = (0, -1)
        if key[pygame.K_DOWN]:
            direction = (0, 1)
        if key[pygame.K_LEFT]:
            direction = (-1, 0)
        if key[pygame.K_RIGHT]:
            direction = (1, 0)
    fenetre.fill(NOIR)

    head = [snake[0][0] + direction[0], snake[0][1] + direction[1]]
    snake.insert(0, head)
    snake.pop(-1)

    for elt in snake[1:]:
        pygame.draw.rect(fenetre, VERT,
                         (elt[0] * BLOC, elt[1] * BLOC, BLOC, BLOC))
    pygame.draw.rect(fenetre, JAUNE,
                     (snake[0][0] * BLOC, snake[0][1] * BLOC, BLOC, BLOC))
    drawText(str(score), font, fenetre, 0.2*LARGEUR, 0.2*HAUTEUR)
    horloge.tick(FPS)
    pygame.display.update()
