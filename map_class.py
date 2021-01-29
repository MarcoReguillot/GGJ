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
        self.little_white = pygame.transform.scale(pygame.image.load('assets/white.jpg'), (100, 300))
        #black
        self.black = pygame.image.load('assets/black.jpg')
        self.little_black = pygame.transform.scale(pygame.image.load('assets/black.jpg'), (250, 250))