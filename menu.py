# -*- coding: cp1252 -*-
import pygame, pyglet
from pygame.locals import *

pygame.init()

#clock
clock = pygame.time.Clock()

#background
background = pygame.image.load('assets/bg.jpg')

#menu buttons
play = pygame.image.load('assets/play.png')
play_rect = pygame.Rect(620, 320, 70, 70)
info = pygame.transform.scale(pygame.image.load('assets/help.png'), (70, 70))
info_rect = pygame.Rect(1210, 0, 70, 70)

#info help cube
info_cube =  pygame.image.load('assets/info_cube.png')

#smyley
smyley = pygame.image.load('assets/smile.png')

def loop_gif(screen, pic, end, wait):
    screen.blit(background, (0, 0))
    screen.blit(pygame.image.load(pic), (400, 100))
    pygame.display.flip()
    for inc in range(4000000):
        0
    for event in pygame.event.get():
        if event.type == QUIT:
            end = 1
            wait = False
        elif event.type == KEYDOWN and pygame.key.get_pressed()[pygame.K_ESCAPE]:
            end = 0
            wait = False
    return (end, wait)

def easter_egg(screen):
    wait = True
    end = 0
    while wait == True:
        screen.blit(background, (0, 0))
        end, wait = loop_gif(screen, 'assets/rikka/rikka1.jpg', end, wait)
        end, wait = loop_gif(screen, 'assets/rikka/rikka2.jpg', end, wait)
        end, wait = loop_gif(screen, 'assets/rikka/rikka3.jpg', end, wait)
        end, wait = loop_gif(screen, 'assets/rikka/rikka4.jpg', end, wait)
        end, wait = loop_gif(screen, 'assets/rikka/rikka5.jpg', end, wait)
    return (end)

def help(screen):
    wait = True
    end = 0
    while wait == True:
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        screen.blit(info_cube, (470, 260))
        for event in pygame.event.get():
            if event.type == QUIT:
                end = 1
                wait = False
            elif event.type == KEYDOWN and pygame.key.get_pressed()[pygame.K_ESCAPE]:
                end = 0
                wait = False
        pygame.display.flip()
    return (end)

def menu(screen):
    wait = True
    click = False
    end = 0
    space = 0
    while wait == True:
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        if space == 0:
            screen.blit(play, (620, 320))
            screen.blit(info, (1210, 0))
        else:
            screen.blit(smyley, (500, 260))
            screen.blit(info, (1210, 0))
        mx, my = pygame.mouse.get_pos()

        if play_rect.collidepoint((mx, my)):
            if click == True:
                end = 0
                wait = False
        elif info_rect.collidepoint((mx, my)):
            if click == True and space == 0:
                if help(screen) == 1:
                    return (1)
            elif click == True and space == 1:
                if easter_egg(screen) == 1:
                    return (1)
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                end = 1
                wait = False
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            elif event.type == KEYDOWN and pygame.key.get_pressed()[pygame.K_SPACE]:
                if space == 0:
                    space = 1
                else:
                    space = 0
        pygame.display.flip()
        clock.tick(60)
    return (end)