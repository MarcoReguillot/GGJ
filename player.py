# -*- coding: cp1252 -*-
# Player object

import pygame
import animations
import random

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
        self.speed = 10
        self.rotation_speed = 20
        self.actual_speed = [0, 0]
        self.stop_speed = 1.5
        self.current_image = self.idle
        #self.walk_anim = create_animation("assets/character/walk/", 1, "assets")

    def update(self, screen):
        #updating position
        self.x += self.actual_speed[0]
        self.y += self.actual_speed[1]
        #render character
        self.current_image = pygame.transform.rotate(self.idle, self.rotation)
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
        print(self.rotation)
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
