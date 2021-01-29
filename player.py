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
        self.stop_speed = 2
        self.current_image = self.idle
        #self.walk_anim = create_animation("assets/character/walk/", 1, "assets")

    def update(self, screen):
        #updating position
        self.x += self.actual_speed[0]
        self.y += self.actual_speed[1]
        #render character
        screen.blit(self.current_image, (1280 / 2, 720 / 2))

    #deplacements
    def go_left(self, speed):
        self.actual_speed[0] = -speed

    def go_right(self, speed):
        self.actual_speed[0] = speed

    def go_up(self, speed):
        self.actual_speed[1] = -speed

    def go_down(self, speed):
        self.actual_speed[1] = speed

    def handle_movements(self, keys_pressed):
        movements = []

        for i in self.controls:
            if keys_pressed()[i[0]]:
                movements.append(i[1])
        if len(movements) == 0:
            self.actual_speed[0] = 0
            self.actual_speed[1] = 0
        else:
            for i in movements:
                i(self.speed / len(movements))