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
        self.white = pygame.image.load('assets/bg_white.jpg')
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
        self.little_white_14 = pygame.transform.scale(pygame.image.load('assets/white.jpg'), (1954, 1233))
        self.Rect_white.append(pygame.Rect(-3240, -3213, 1954, 1233))
        self.little_white_7 = pygame.transform.scale(pygame.image.load('assets/white.jpg'), (1300, 308))
        self.Rect_white.append(pygame.Rect(2073, 160, 1300, 308))

        #black
        self.Rect_black = []
        self.black = pygame.image.load('assets/bg_black.jpg')
        self.little_black_17 = pygame.transform.scale(pygame.image.load('assets/black.png'), (873, 873))
        self.Rect_black.append(pygame.Rect(200, -100, 873, 873))
        self.little_black_14 = pygame.transform.scale(pygame.image.load('assets/black.png'), (308, 1919))
        self.Rect_black.append(pygame.Rect(484, -2019, 308, 1919))
        self.little_black_7 = pygame.transform.scale(pygame.image.load('assets/black.png'), (308, 1919))
        self.Rect_black.append(pygame.Rect(483, 722, 308, 1919))
        self.little_black_4 = pygame.transform.scale(pygame.image.load('assets/black.png'), (2571, 1380))
        self.Rect_black.append(pygame.Rect(-650, 2591, 2571, 1380))
        self.little_black_5_1 = pygame.transform.scale(pygame.image.load('assets/black.png'), (308, 900))
        self.Rect_black.append(pygame.Rect(483, 3971, 308, 900))
        self.little_black_5_2 = pygame.transform.scale(pygame.image.load('assets/black.png'), (2500, 308))
        self.Rect_black.append(pygame.Rect(-2017, 4571, 2500, 308))
        self.little_black_2 = pygame.transform.scale(pygame.image.load('assets/black.png'), (1954, 1233))
        self.Rect_black.append(pygame.Rect(-3971, 4200, 1954, 1233))
        self.little_black_18 = pygame.transform.scale(pygame.image.load('assets/black.png'), (661, 308))
        self.Rect_black.append(pygame.Rect(-2580, 632, 661, 308))
        self.little_black_19 = pygame.transform.scale(pygame.image.load('assets/black.png'), (941, 1392))
        self.Rect_black.append(pygame.Rect(-1930, 350, 941, 1392))
        self.little_black_20 = pygame.transform.scale(pygame.image.load('assets/black.png'), (941, 1392))
        self.Rect_black.append(pygame.Rect(-3500, 350, 941, 1392))
        self.little_black_15 = pygame.transform.scale(pygame.image.load('assets/black.png'), (308, 2646))
        self.Rect_black.append(pygame.Rect(-2400, -1980, 308, 2646))
        self.little_black_16 = pygame.transform.scale(pygame.image.load('assets/black.png'), (1954, 1233))
        self.Rect_black.append(pygame.Rect(-3240, -3213, 1954, 1233))
        self.little_black_6 = pygame.transform.scale(pygame.image.load('assets/black.png'), (1800, 308))
        self.Rect_black.append(pygame.Rect(1921, 2800, 1800, 308))
        self.little_black_3 = pygame.transform.scale(pygame.image.load('assets/black.png'), (1000, 941))
        self.Rect_black.append(pygame.Rect(3721, 2300, 1000, 941))
        self.little_black_13 = pygame.transform.scale(pygame.image.load('assets/black.png'), (1300, 308))
        self.Rect_black.append(pygame.Rect(1073, 160, 1300, 308))
        self.little_black_12 = pygame.transform.scale(pygame.image.load('assets/black.png'), (308, 1000))
        self.Rect_black.append(pygame.Rect(3065, -532, 308, 1000))



    def display_cams(self, screen, x, y):
        self.cameras.display(screen, x, y)

    def in_the_screen(self, rect):
        if rect.left + rect.width < 0 or rect.left > 1280 or rect.top + rect.height < 0 or rect.top > 720:
            return (0)
        return (1)

    def make_room_w(self, room_nb, x, y, screen, image, space, left, top, width, height):
        self.Rect_white[room_nb] = pygame.Rect(left - x, top - y, width, height)
        if self.in_the_screen(self.Rect_white[room_nb]) == 1 and space == 1:
            screen.blit(image, (left - x, top - y))

    def make_room_b(self, room_nb, x, y, screen, image, space, left, top, width, height):
        self.Rect_black[room_nb] = pygame.Rect(left - x, top - y, width, height)
        if self.in_the_screen(self.Rect_black[room_nb]) == 1 and space == 0:
            screen.blit(image, (left - x, top - y))

    def old(self, x, y, screen, space):
        if space == 1:
            screen.blit(self.black, (0, 0))
        self.make_room_w(0, x, y, screen, self.little_white_8, space, 200, -100, 873, 873)
        self.make_room_w(1, x, y, screen, self.little_white_3, space, 483, 722, 308, 1919)
        self.make_room_w(2, x, y, screen, self.little_white_2, space, -650, 2591, 2571, 1380)
        self.make_room_w(3, x, y, screen, self.little_white_10_1, space, -400, 1840, 308, 800)
        self.make_room_w(4, x, y, screen, self.little_white_10_2, space, -2400, 1840, 2000, 308)
        self.make_room_w(5, x, y, screen, self.little_white_10_3, space, -2400, 940, 308, 900)
        self.make_room_w(6, x, y, screen, self.little_white_12, space, -2580, 632, 661, 308)
        self.make_room_w(7, x, y, screen, self.little_white_15, space, -1930, 350, 941, 1392)
        self.make_room_w(8, x, y, screen, self.little_white_16, space, -3500, 350, 941, 1392)
        self.make_room_w(9, x, y, screen, self.little_white_11, space, -2400, -1980, 308, 2646)
        self.make_room_w(10, x, y, screen, self.little_white_14, space, -3240, -3213, 1954, 1233)
        self.make_room_w(11, x, y, screen, self.little_white_7, space, 2073, 160, 1300, 308)

    def child(self, x, y, screen, space):
        if space == 0:
            screen.blit(self.white, (0, 0))
        self.make_room_b(0, x, y, screen, self.little_black_17, space, 200, -100, 873, 873)
        self.make_room_b(1, x, y, screen, self.little_black_14, space, 484, -2019, 308, 1919)
        self.make_room_b(2, x, y, screen, self.little_black_7, space, 483, 722, 308, 1919)
        self.make_room_b(3, x, y, screen, self.little_black_4, space, -650, 2591, 2571, 1380)
        self.make_room_b(4, x, y, screen, self.little_black_5_1, space, 483, 3971, 308, 900)
        self.make_room_b(5, x, y, screen, self.little_black_5_2, space, -2017, 4564, 2500, 308)
        self.make_room_b(6, x, y, screen, self.little_black_2, space, -3971, 4200, 1954, 1233)
        self.make_room_b(7, x, y, screen, self.little_black_18, space, -2580, 632, 661, 308)
        self.make_room_b(8, x, y, screen, self.little_black_19, space, -1930, 350, 941, 1392)
        self.make_room_b(9, x, y, screen, self.little_black_20, space, -3500, 350, 941, 1392)
        self.make_room_b(10, x, y, screen, self.little_black_15, space, -2400, -1980, 308, 2646)
        self.make_room_b(11, x, y, screen, self.little_black_16, space, -3240, -3213, 1954, 1233)
        self.make_room_b(12, x, y, screen, self.little_black_6, space, 1921, 2800, 1800, 308)
        self.make_room_b(13, x, y, screen, self.little_black_3, space, 3721, 2300, 1000, 941)
        self.make_room_b(14, x, y, screen, self.little_black_13, space, 1073, 160, 1300, 308)
        self.make_room_b(15, x, y, screen, self.little_black_12, space, 3065, -532, 308, 1000)