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
        self.little_white_15 = pygame.transform.scale(pygame.image.load('assets/white.jpg'), (941, 1392))
        self.Rect_white.append(pygame.Rect(-1930, 350, 941, 1392))
        self.little_white_16 = pygame.transform.scale(pygame.image.load('assets/white.jpg'), (941, 1392))
        self.Rect_white.append(pygame.Rect(-3500, 350, 941, 1392))
        self.little_white_11 = pygame.transform.scale(pygame.image.load('assets/white.jpg'), (308, 2646))
        self.Rect_white.append(pygame.Rect(-2400, -1980, 308, 2646))

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

    def make_room(self, room_nb, x, y, screen, image, space, left, top, width, height):
        self.Rect_white[room_nb] = pygame.Rect(left - x, top - y, width, height)
        if self.in_the_screen(self.Rect_white[room_nb]) == 1 and space == 1:
            screen.blit(image, (left - x, top - y))

    def old(self, x, y, screen, space):
        screen.blit(self.black, (0, 0))
        self.make_room(0, x, y, screen, self.little_white_8, space, 200, -100, 873, 873)
        self.make_room(1, x, y, screen, self.little_white_3, space, 483, 722, 308, 1919)
        self.make_room(2, x, y, screen, self.little_white_2, space, -650, 2591, 2571, 1380)
        self.make_room(3, x, y, screen, self.little_white_10_1, space, -400, 1840, 308, 750)
        self.make_room(4, x, y, screen, self.little_white_10_2, space, -2400, 1840, 2000, 308)
        self.make_room(5, x, y, screen, self.little_white_10_3, space, -2400, 940, 308, 900)
        self.make_room(6, x, y, screen, self.little_white_12, space, -2580, 632, 661, 308)
        self.make_room(7, x, y, screen, self.little_white_15, space, -1930, 350, 941, 1392)
        self.make_room(8, x, y, screen, self.little_white_16, space, -3500, 350, 941, 1392)
        self.make_room(9, x, y, screen, self.little_white_11, space, -2400, -1980, 308, 2646)

    def child(self, x, y, screen, space):
        self.Rect_black[0] = pygame.Rect(560 - x, 300 - y, 250, 250)
        self.Rect_black[1] = pygame.Rect(1030 - x, 200 - y, 250, 250)

    def child_display(self, screen, x, y):
        screen.blit(self.white, (0, 0))
        screen.blit(self.little_black_1, (560 - x, 300 - y))
        screen.blit(self.little_black_2, (1030 - x, 200 - y))
        self.display_cams(screen, x, y)