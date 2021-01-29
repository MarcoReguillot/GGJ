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
        self.rect = self.idle.get_rect()
        self.x = 1280 / 2
        self.y = 720 / 2
        self.speed = 10
        self.idle = pygame.transform.scale(self.idle, (100, 100))
        self.actual_speed = [0, 0]
        self.stop_speed = 2
        self.current_image = self.idle
        #self.walk_anim = create_animation("assets/character/walk/", 1, "assets")

    def update(self, screen):
        #updating position
        self.x += self.actual_speed[0]
        self.y += self.actual_speed[1]
        #render character
        screen.blit(self.current_image, (self.x, self.y))

    #deplacements
    def go_left(self):
        self.actual_speed[0] = -self.speed

    def go_right(self):
        self.actual_speed[0] = self.speed

    def go_up(self):
        self.actual_speed[1] = -self.speed

    def go_down(self):
        self.actual_speed[1] = self.speed

    def handle_movements(self, keys_pressed):
        movement = False

        for i in self.controls:
            if keys_pressed()[i[0]]:
                i[1]()
                movement = True
        if not movement:
            self.actual_speed[0] = 0
            self.actual_speed[1] = 0

