# -*- coding: cp1252 -*-
# Player object

import pygame
import numpy as np
import animations
from camera import Camera

class Map(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.cameras = Camera()
        #self.cameras.append(Camera())
        #white
        self.Rect_white = []
        self.white = pygame.image.load('assets/white.jpg')
        self.little_white_8 = pygame.transform.scale(pygame.image.load('assets/white.jpg'), (873, 873))
        self.Rect_white.append(pygame.Rect(200, -100, 873, 873))
        self.little_white_3 = pygame.transform.scale(pygame.image.load('assets/white.jpg'), (308, 1919))
        self.Rect_white.append(pygame.Rect(483, 722, 308, 1919))
        self.little_white_2 = pygame.transform.scale(pygame.image.load('assets/white.jpg'), (2571, 1380))
        self.Rect_white.append(pygame.Rect(-650, 2591, 2571, 1380))
        self.little_white_10_1 = pygame.transform.scale(pygame.image.load('assets/white.jpg'), (308, 750))
        self.Rect_white.append(pygame.Rect(-400, 1840, 308, 750))
        self.little_white_10_2 = pygame.transform.scale(pygame.image.load('assets/white.jpg'), (2000, 308))
        self.Rect_white.append(pygame.Rect(-2400, 1840, 2000, 308))
        self.little_white_10_3 = pygame.transform.scale(pygame.image.load('assets/white.jpg'), (308, 900))
        self.Rect_white.append(pygame.Rect(-2400, 940, 308, 900))
        self.little_white_12 = pygame.transform.scale(pygame.image.load('assets/white.jpg'), (661, 308))
        self.Rect_white.append(pygame.Rect(-2580, 632, 661, 308))

        #black
        self.Rect_black = []
        self.black = pygame.image.load('assets/black.jpg')
        self.little_black_1 = pygame.transform.scale(pygame.image.load('assets/black.jpg'), (250, 250))
        self.Rect_black.append(pygame.Rect(560, 300, 250, 250))
        self.little_black_2 = pygame.transform.scale(pygame.image.load('assets/black.jpg'), (250, 250))
        self.Rect_black.append(pygame.Rect(1030, 0, 250, 250))

    def display_cams(self, screen, x, y):
        self.cameras.display(screen, x, y)

    def in_the_screen(self, rect):
        if rect.left + rect.width < 0 or rect.left > 1280 or rect.top + rect.height < 0 or rect.top > 720:
            return (0)
        return (1)

    def old(self, x, y):
        self.Rect_white[0] = pygame.Rect(200 - x, -100 - y, 873, 873)
        self.Rect_white[2] = pygame.Rect(-650 - x, 2591 - y, 2571, 1380)
        self.Rect_white[1] = pygame.Rect(483 - x, 722 - y, 308, 1919)
        self.Rect_white[3] = pygame.Rect(-400 - x, 1840 - y, 308, 750)
        self.Rect_white[4] = pygame.Rect(-2400 - x, 1840 - y, 2000, 308)
        self.Rect_white[5] = pygame.Rect(-2400 - x, 940 - y, 308, 900)
        self.Rect_white[6] = pygame.Rect(-2580 - x, 632 - y, 661, 308)

    def old_display(self, screen, x, y):
        screen.blit(self.black, (0, 0))
        if self.in_the_screen(self.Rect_white[0]) == 1:
            screen.blit(self.little_white_8, (200 - x, -100 - y))
        if self.in_the_screen(self.Rect_white[2]) == 1:
            screen.blit(self.little_white_2, (-650 - x, 2591 - y))
        if self.in_the_screen(self.Rect_white[1]) == 1:
            screen.blit(self.little_white_3, (483 - x, 722 - y))
        if self.in_the_screen(self.Rect_white[3]) == 1:
            screen.blit(self.little_white_10_1, (-400 - x, 1840 - y))
        if self.in_the_screen(self.Rect_white[4]) == 1:
            screen.blit(self.little_white_10_2, (-2400 - x, 1840 - y))
        if self.in_the_screen(self.Rect_white[5]) == 1:
            screen.blit(self.little_white_10_3, (-2400 - x, 940 - y))
        if self.in_the_screen(self.Rect_white[6]) == 1:
            screen.blit(self.little_white_12, (-2580 - x, 632 - y))

    def child(self, x, y):
        self.Rect_black[0] = pygame.Rect(560 - x, 300 - y, 250, 250)
        self.Rect_black[1] = pygame.Rect(1030 - x, 200 - y, 250, 250)

    def child_display(self, screen, x, y):
        screen.blit(self.white, (0, 0))
        screen.blit(self.little_black_1, (560 - x, 300 - y))
        screen.blit(self.little_black_2, (1030 - x, 200 - y))
        self.display_cams(screen, x, y)