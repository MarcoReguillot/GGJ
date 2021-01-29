# -*- coding: cp1252 -*-
# Player object

import pygame
import animations

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
        self.rect = self.idle.get_rect()
        self.x = 0
        self.y = 0
        self.speed = 10
        self.actual_speed = [0, 0]
        self.stop_speed = 1.5
        self.current_image = self.idle
        #self.walk_anim = create_animation("assets/character/walk/", 1, "assets")

    def update(self, screen):
        #updating position
        self.x += self.actual_speed[0]
        self.y += self.actual_speed[1]
        #render character
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

    def decelerate(self, speed):
        if (speed > 0):
            speed -= self.stop_speed
            if (speed < 0):
                speed = 0
        elif (speed < 0):
            speed += self.stop_speed
            if (speed > 0):
                speed = 0
        return (speed)

    def handle_movements(self, keys_pressed):
        movements = []
        y = False
        x = False
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
            self.actual_speed[0] = self.decelerate(self.actual_speed[0])
        if (y == False):
            self.actual_speed[1] = self.decelerate(self.actual_speed[1])
