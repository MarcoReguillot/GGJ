# -*- coding: cp1252 -*-
# Player object

import pygame
from animations import create_animation
import random
import math

def get_nearest(value, goal1, goal2):
    if (value == goal1 or value == goal2):
        return (value)
    if (abs(goal1 - value) == abs(goal2 - value)):
        if (random.randint(0, 1) == 0):
            return(goal1)
        else:
            return (goal2)
    elif (abs(goal1 - value) > abs(goal2 - value)):
        return (goal2)
    else:
        return (goal1)

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__
        self.controls = {
            (pygame.K_UP, self.go_up),
            (pygame.K_DOWN ,self.go_down),
            (pygame.K_LEFT, self.go_left),
            (pygame.K_RIGHT, self.go_right)
        }
        self.idle = pygame.image.load("assets/character.png")
        self.idle = pygame.transform.scale(self.idle, (100, 100))
        self.rotation = 0
        self.rect = self.idle.get_rect()
        self.x = 0
        self.y = 0
        self.animation = create_animation("assets/character/", 3, ".png", (100, 100))
        self.current_animation = 0
        self.animation_speed = 0.2
        self.speed = 10
        self.rotation_speed = 20
        self.actual_speed = [0, 0]
        self.stop_speed = 1.5
        self.current_image = self.idle
        #self.walk_anim = create_animation("assets/character/walk/", 1, "assets")

    def update_animation(self):
        if (self.actual_speed[0] == 0 and self.actual_speed[1] == 0):
            self.current_image = self.animation[1]
            return
        self.current_animation += self.animation_speed
        if (self.current_animation < 3):
            self.current_image = self.animation[math.floor(self.current_animation)]
        elif(self.current_animation < 4):
            self.current_image = self.animation[1]
        else:
            self.current_animation = 0
            self.current_image = self.animation[0]

    def update(self, screen):
        #updating position
        self.x += self.actual_speed[0]
        self.y += self.actual_speed[1]
        #render character
        self.update_animation()
        self.current_image = pygame.transform.rotate(self.current_image, self.rotation)
        screen.blit(self.current_image, ((1280 - self.rect.width) / 2, (720 - self.rect.height) / 2))

    #deplacements
    def go_left(self, speed):
        self.actual_speed[0] = -speed

    def go_right(self, speed):
        self.actual_speed[0] = speed

    def go_up(self, speed):
        self.actual_speed[1] = -speed

    def go_down(self, speed):
        self.actual_speed[1] = speed

    def go_to_value(self, value, step, goal):
        if (value > goal):
            value -= step
            if (value < goal):
                value = goal
        elif (value < goal):
            value += step
            if (value > goal):
                value = goal
        return (value)

    def handle_movements(self, keys_pressed):
        movements = []
        y = False
        x = False
        if keys_pressed()[pygame.K_UP]:
            self.rotation = self.go_to_value(self.rotation, self.rotation_speed, get_nearest(self.rotation, 0, 360))
            if (self.rotation == 360):
                self.rotation = 0
        elif keys_pressed()[pygame.K_RIGHT]:
            self.rotation = self.go_to_value(self.rotation, self.rotation_speed, get_nearest(self.rotation, 270, -90))
            if (self.rotation == -90):
                self.rotation = 270
        elif keys_pressed()[pygame.K_LEFT]:
            self.rotation = self.go_to_value(self.rotation, self.rotation_speed, get_nearest(self.rotation, 90, -270))
            if (self.rotation == -270):
                self.rotation = 90
        elif keys_pressed()[pygame.K_DOWN]:
            self.rotation = self.go_to_value(self.rotation, self.rotation_speed, get_nearest(self.rotation, 180, -180))
            if (self.rotation == -180):
                self.rotation = 180
        for i in self.controls:
            if keys_pressed()[i[0]]:
                if (i[0] == pygame.K_UP or i[0] == pygame.K_DOWN):
                    y = not y
                else:
                    x = not x
                movements.append(i[1])
        for i in movements:
            i(self.speed / len(movements))
        if (x == False):
            self.actual_speed[0] = self.go_to_value(self.actual_speed[0], self.stop_speed, 0)
        if (y == False):
            self.actual_speed[1] = self.go_to_value(self.actual_speed[1], self.stop_speed, 0)
