# -*- coding: cp1252 -*-
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame, pyglet
from pygame.locals import *
from player import Player

pygame.init()

#FPS clock
clock = pygame.time.Clock()

#space
space = 0

#game screen generation
pygame.display.set_caption('')
size = width, height = 1280, 720
screen = pygame.display.set_mode((size))

#mouse
pygame.mouse.set_cursor(*pygame.cursors.diamond)

#white
white = pygame.image.load('assets/white.jpg')
little_white_corner = pygame.transform.scale(pygame.image.load('assets/white.jpg'), (250, 250))
little_white = pygame.transform.scale(pygame.image.load('assets/white.jpg'), (100, 300))

#black
black = pygame.image.load('assets/black.jpg')
little_black = pygame.transform.scale(pygame.image.load('assets/black.jpg'), (250, 250))

#Player creation
player = Player()

running = True

def event():
    global space
    global running
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN and pygame.key.get_pressed()[pygame.K_SPACE]:
            if space == 0:
                space = 1
            else:
                space = 0
    player.handle_movements(pygame.key.get_pressed)

def old():
    screen.blit(black, (0, 0))
    screen.blit(little_white_corner, (1030, 470))
    screen.blit(little_white, (1180, 210))

def child():
    screen.blit(white, (0, 0))
    screen.blit(little_black, (1030, 470))
    screen.blit(little_black, (1030, 0))

def game():
    while running:
        clock.tick(60)
        screen.fill((0, 0, 0))
        event()
        if space == 0:
            child()
        else:
            old()
        player.update(screen)
        pygame.display.flip()

game()

pygame.quit()