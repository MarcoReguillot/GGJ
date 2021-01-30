# -*- coding: cp1252 -*-
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame, pyglet
from pygame.locals import *
from player import Player
from map_class import Map
from menu import menu

pygame.init()

#FPS clock
clock = pygame.time.Clock()

#space
space = 1

#game screen generation
pygame.display.set_caption('')
size = width, height = 1280, 720
screen = pygame.display.set_mode((size))
icon = pygame.image.load('assets/icon.png')
pygame.display.set_icon(icon)

#mouse
pygame.mouse.set_cursor(*pygame.cursors.diamond)

#Player creation
player = Player()

#Map creation
maps = Map()

#Sound
ost = pygame.mixer.Sound('assets/ost.wav')
ost.set_volume(0.2)
ost.play(loops = -1, maxtime = 0, fade_ms = 0)

running = True

def collide(character, obj):
    if obj.contains(character) == 1:
        return (1)
    return (0)

def change_space(space):
    if space == 0:
        for inc in range(len(maps.Rect_white)):
            maps.old(player.x, player.y)
            if collide(player.rect, maps.Rect_white[inc]) == 1:
                return (1)
        return (0)
    else:
        for inc in range(len(maps.Rect_black)):
            maps.child(player.x, player.y)
            if collide(player.rect, maps.Rect_black[inc]) == 1:
                return (1)
        return (0)

def event():
    global space
    global running
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN and pygame.key.get_pressed()[pygame.K_SPACE]:
            if change_space(space) == 1:
                if space == 0:
                    space = 1
                else:
                    space = 0
            else:
                sound = pygame.mixer.Sound("assets/stop.wav")
                sound.set_volume(0.1)
                sound.play()
    player.handle_movements(pygame.key.get_pressed)

def game():
    if menu(screen) == 1:
        return (0)
    while running:
        clock.tick(90)
        screen.fill((0, 0, 0))
        event()
        maps.child(player.x, player.y)
        maps.old(player.x, player.y)
        if space == 0:
            player.handle_collisions(maps.Rect_black)
            maps.child_display(screen, player.x, player.y)
        else:
            player.handle_collisions(maps.Rect_white)
            maps.old_display(screen, player.x, player.y)
        player.update(screen)
        pygame.display.flip()

game()

pygame.quit()