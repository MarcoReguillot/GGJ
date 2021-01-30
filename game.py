# -*- coding: cp1252 -*-
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame, pyglet
from pygame.locals import *
from player import Player
from map_class import Map
from menu import menu
from hud import HudText
from objects import Objects


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
objects_light = Objects(0)
objects_dark = Objects(1)

hud = HudText()
hud.render_text("Press [SPACE].", "", "")

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
            maps.old(player.x, player.y, screen, space)
            if collide(player.rect, maps.Rect_white[inc]) == 1:
                return (1)
        return (0)
    else:
        for inc in range(len(maps.Rect_black)):
            maps.child(player.x, player.y, screen, space)
            if collide(player.rect, maps.Rect_black[inc]) == 1:
                return (1)
        return (0)


already_pressed_space = False

def event():
    global already_pressed_space
    global space
    global running
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN and pygame.key.get_pressed()[pygame.K_SPACE]:
            if change_space(space) == 1:
                if not (already_pressed_space):
                    hud.render_text("", "Well done...", "")
                    already_pressed_space = True
                if space == 0:
                    player.animation = player.anim_light
                    space = 1
                else:
                    player.animation = player.anim_dark
                    space = 0
            else:
                sound = pygame.mixer.Sound("assets/stop.wav")
                sound.set_volume(0.1)
                sound.play()
        if (event.type == KEYDOWN):
            if pygame.key.get_pressed()[pygame.K_RETURN]:
                hud.hide_text()
            elif pygame.key.get_pressed()[pygame.K_c]:
                if (space == 0):
                    for i in objects_dark.interactive_objects:
                        if i.collision(player):
                            hud.render_text(i.text1, i.text2, i.text3)
                else:
                    for i in objects_light.interactive_objects:
                        if i.collision(player):
                            hud.render_text(i.text1, i.text2, i.text3)
    player.handle_movements(pygame.key.get_pressed)

def game():
    if menu(screen) == 1:
        return (0)
    while running:
        clock.tick(90)
        screen.fill((0, 0, 0))
        event()
        maps.child(player.x, player.y, screen, space)
        maps.old(player.x, player.y, screen, space)
        if space == 0:
            player.handle_collisions(maps.Rect_black, objects_dark)
            objects_dark.update(screen, player)
        else:
            player.handle_collisions(maps.Rect_white, objects_light)
            objects_light.update(screen, player)
        player.update(screen, clock.get_fps())
        hud.update(screen, space, clock.get_fps())
        pygame.display.flip()

game()

pygame.quit()