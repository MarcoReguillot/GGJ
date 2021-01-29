# -*- coding: cp1252 -*-
# Player object

import pygame
import animations

class Map(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        #white
        self.white = pygame.image.load('assets/white.jpg')
        self.little_white_corner = pygame.transform.scale(pygame.image.load('assets/white.jpg'), (250, 250))
        self.little_white_corner_rect = pygame.Rect(560, 300, 250, 250)
        self.little_white = pygame.transform.scale(pygame.image.load('assets/white.jpg'), (300, 100))
        self.little_white_rect = pygame.Rect(810, 300, 300, 100)

        #black
        self.black = pygame.image.load('assets/black.jpg')
        self.little_black_1 = pygame.transform.scale(pygame.image.load('assets/black.jpg'), (250, 250))
        self.little_black_1_rect = pygame.Rect(560, 300, 250, 250)
        self.little_black_2 = pygame.transform.scale(pygame.image.load('assets/black.jpg'), (250, 250))
        self.little_black_2_rect = pygame.Rect(1030, 0, 250, 250)

    def old(self, x, y):
        self.little_white_corner_rect = pygame.Rect(560 - x, 300 - y, 250, 250)
        self.little_white_rect = pygame.Rect(810 - x, 300 - y, 300, 100)

    def old_display(self, screen, x, y):
        screen.blit(self.black, (0, 0))
        screen.blit(self.little_white_corner, (560 - x, 300 - y))
        screen.blit(self.little_white, (810 - x, 300 - y))

    def child(self, x, y):
        self.little_black_1_rect = pygame.Rect(560 - x, 300 - y, 250, 250)
        self.little_black_2_rect = pygame.Rect(1030 - x, 0 - y, 250, 250)

    def child_display(self, screen, x, y):
        screen.blit(self.white, (0, 0))
        screen.blit(self.little_black_1, (560 - x, 300 - y))
        screen.blit(self.little_black_2, (1030 - x, 0 - y))