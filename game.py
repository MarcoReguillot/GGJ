# -*- coding: cp1252 -*-
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame, pyglet
from pygame.locals import *
from player import Player
from map_class import Map

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

#Player creation
player = Player()

#Map creation
maps = Map()

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

def game():
    while running:
        clock.tick(60)
        screen.fill((0, 0, 0))
        event()
        if space == 0:
            maps.child(screen)
        else:
            maps.old(screen)
        player.update(screen)
        pygame.display.flip()

game()

pygame.quit()