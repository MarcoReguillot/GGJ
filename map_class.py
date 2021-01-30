# -*- coding: cp1252 -*-
# Player object

import pygame
import numpy as np
import animations

class Map(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        #white
        self.Rect_white = []
        self.white = pygame.image.load('assets/white.jpg')
        self.little_white_corner = pygame.transform.scale(pygame.image.load('assets/white.jpg'), (250, 250))
        self.Rect_white.append(pygame.Rect(560, 300, 250, 250))
        self.little_white = pygame.transform.scale(pygame.image.load('assets/white.jpg'), (400, 150))
        self.Rect_white.append(pygame.Rect(810, 300, 300, 100))

        #black
        self.Rect_black = []
        self.black = pygame.image.load('assets/black.jpg')
        self.little_black_1 = pygame.transform.scale(pygame.image.load('assets/black.jpg'), (250, 250))
        self.Rect_black.append(pygame.Rect(560, 300, 250, 250))
        self.little_black_2 = pygame.transform.scale(pygame.image.load('assets/black.jpg'), (250, 250))
        self.Rect_black.append(pygame.Rect(1030, 0, 250, 250))

    def old(self, x, y):
        self.Rect_white[0] = pygame.Rect(560 - x, 300 - y, 250, 250)
        self.Rect_white[1] = pygame.Rect(810 - x, 300 - y, 400, 150)

    def old_display(self, screen, x, y):
        screen.blit(self.black, (0, 0))
        screen.blit(self.little_white_corner, (560 - x, 300 - y))
        screen.blit(self.little_white, (810 - x, 300 - y))

    def child(self, x, y):
        self.Rect_black[0] = pygame.Rect(560 - x, 300 - y, 250, 250)
        self.Rect_black[1] = pygame.Rect(1030 - x, 200 - y, 250, 250)

    def child_display(self, screen, x, y):
        screen.blit(self.white, (0, 0))
        screen.blit(self.little_black_1, (560 - x, 300 - y))
        screen.blit(self.little_black_2, (1030 - x, 200 - y))