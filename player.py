# -*- coding: cp1252 -*-
# Player object

import pygame
from animations import create_animation
import random
from objects import Objects
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
        self.clock = 0
        self.rotation = 0
        self.x = 0
        self.y = 0
        self.animation = create_animation("assets/character/", 3, ".png", (100, 100))
        self.image = self.animation[1]
        self.rect = self.animation[0].get_rect()
        self.current_animation = 0
        self.animation_speed = 0.2
        self.speed = 10
        self.rotation_speed = 20
        self.actual_speed = [0, 0]
        self.stop_speed = 1.5
        self.current_image = self.animation[0]
        self.temp_null_objects = []
        self.rect.x = (1280 - self.rect.width) / 2
        self.rect.y = (720 - self.rect.height) / 2

    def collision_down(self, rooms, objects):
        x = self.rect.left
        y = self.rect.top
        x += self.rect.width / 2
        y += self.rect.height
        for i in rooms:
            if i.collidepoint((x, y)):
                for obj in objects.solid_objects:
                    if (obj.rect.collidepoint(x, y)):
                        return (True)
                return (False)
        return (True)

    def collision_up(self, room, objects):
        x = self.rect.left
        y = self.rect.top
        x += self.rect.width / 2
        for i in room:
            if i.collidepoint((x, y)):
                for obj in objects.solid_objects:
                    if (obj.rect.collidepoint(x, y)):
                        return (True)
                return (False)
        return (True)

    def collision_right(self, room, objects):
        x = self.rect.left
        y = self.rect.top
        y += self.rect.height / 2
        x += self.rect.height
        for i in room:
            if i.collidepoint((x, y)):
                for obj in objects.solid_objects:
                    if (obj.rect.collidepoint(x, y)):
                        return (True)
                return (False)
        return (True)

    def collision_left(self, room, objects):
        x = self.rect.left
        y = self.rect.top
        y += self.rect.height / 2
        for i in room:
            if i.collidepoint((x, y)):
                for obj in objects.solid_objects:
                    if (obj.rect.collidepoint(x, y)):
                        return (True)
                return (False)
        return (True)

    def handle_collisions(self, map, objects):
        #if (self.collision_down(map)):
        #    print("ok")
        #else:
        #    print("pas ok")
        if ((self.actual_speed[0] < 0 and not self.collision_left(map, objects)) or
            (self.actual_speed[0] > 0 and not self.collision_right(map, objects))):
            self.x += self.actual_speed[0] * (50 / self.clock)
        if ((self.actual_speed[1] < 0 and not self.collision_up(map, objects)) or
            (self.actual_speed[1] > 0 and not self.collision_down(map, objects))):
            self.y += self.actual_speed[1] * (50 / self.clock)

    def update_animation(self):
        if (self.actual_speed[0] == 0 and self.actual_speed[1] == 0):
            self.current_image = self.animation[1]
            return
        self.current_animation += self.animation_speed * (50 / self.clock)
        if (self.current_animation < 3):
            self.current_image = self.animation[math.floor(self.current_animation)]
        elif(self.current_animation < 4):
            self.current_image = self.animation[1]
        else:
            self.current_animation = 0
            self.current_image = self.animation[0]

    def update(self, screen, clock):
        self.clock = clock
        self.rect = self.animation[0].get_rect()
        self.rect.x = (1280 - self.rect.width) / 2
        self.rect.y = (720 - self.rect.height) / 2
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
            value -= step * (50 / self.clock)
            if (value < goal):
                value = goal
        elif (value < goal):
            value += step * (50 / self.clock)
            if (value > goal):
                value = goal
        return (value)

    def set_rotation(self, default, alternative):
        self.rotation = self.go_to_value(self.rotation, self.rotation_speed,
            get_nearest(self.rotation, default, alternative))
        if (self.rotation == alternative):
            self.rotation = default

    def handle_movements(self, keys_pressed):
        movements = []
        y = False
        x = False
        if keys_pressed()[pygame.K_UP]:
            if keys_pressed()[pygame.K_RIGHT]:
                self.set_rotation(-45, 315)
            elif keys_pressed()[pygame.K_LEFT]:
                self.set_rotation(45, -315)
            else:
                self.set_rotation(0, 360)
        elif keys_pressed()[pygame.K_RIGHT]:
            if keys_pressed()[pygame.K_UP]:
                self.set_rotation(-45, 315)
            elif keys_pressed()[pygame.K_DOWN]:
                self.set_rotation(225, -225)
            else:
                self.set_rotation(270, -90)
        elif keys_pressed()[pygame.K_LEFT]:
            if keys_pressed()[pygame.K_UP]:
                self.set_rotation(45, -315)
            elif keys_pressed()[pygame.K_DOWN]:
                self.set_rotation(135, -225)
            else:
                self.set_rotation(90, -270)
        elif keys_pressed()[pygame.K_DOWN]:
            self.set_rotation(180, -180)
        for i in self.controls:
            if keys_pressed()[i[0]]:
                if (i[0] == pygame.K_UP or i[0] == pygame.K_DOWN):
                    y = not y
                else:
                    x = not x
                movements.append(i[1])
                if (len(movements) == 2):
                    break
        for i in movements:
            if (((i != self.go_up and i != self.go_down) or y == True) and
                ((i != self.go_left and i != self.go_right) or x == True)):
                i(self.speed / len(movements))
        if (x == False):
            self.actual_speed[0] = self.go_to_value(self.actual_speed[0], self.stop_speed, 0)
        if (y == False):
            self.actual_speed[1] = self.go_to_value(self.actual_speed[1], self.stop_speed, 0)
