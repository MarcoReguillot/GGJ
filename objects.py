##
## EPITECH PROJECT, 2021
## GGJ
## File description:
## objects
##

import pygame
import math
import random

class InteractiveObject(pygame.sprite.Sprite):
    def __init__(self, image, position, scale, angle, text1, text2, text3):
        super().__init__
        self.image = image
        self.image = pygame.transform.scale(self.image, scale)
        self.image = pygame.transform.rotate(self.image, angle)
        self.rect = self.image.get_rect()
        self.text1 = text1
        self.text2 = text2
        self.text3 = text3
        self.x = position[0]
        self.y = position[1]
    def collision(self, player):
        return (self.rect.colliderect(player.rect))

    def update(self, screen, player):
        self.rect.x = self.x - player.x
        self.rect.y = self.y - player.y
        screen.blit(self.image, (self.x - player.x, self.y - player.y))

class SolidObject(pygame.sprite.Sprite):
    def __init__(self, image, position, scale, angle):
        super().__init__
        self.image = image
        self.image = pygame.transform.scale(self.image, scale)
        self.image = pygame.transform.rotate(self.image, angle)
        self.rect = self.image.get_rect()
        self.x = position[0]
        self.y = position[1]

    def update(self, screen, player):
        self.rect.x = self.x - player.x
        self.rect.y = self.y - player.y
        screen.blit(self.image, (self.x - player.x, self.y - player.y))

class DecoObject(pygame.sprite.Sprite):
    def __init__(self, image, position, scale, angle):
        super().__init__
        self.image = image
        self.image = pygame.transform.scale(self.image, scale)
        self.image = pygame.transform.rotate(self.image, angle)
        self.x = position[0]
        self.y = position[1]

    def update(self, screen, player):
        screen.blit(self.image, (self.x - player.x, self.y - player.y))


class Objects(pygame.sprite.Sprite):

    def lamp(self, pos, scale, angle):
        self.deco_objects.append(DecoObject(self.images['deco_lamp'], pos, scale, angle))
        self.solid_objects.append(SolidObject(self.images['solid_lamp'],
            (round(pos[0] + 0.2 * scale[0]), round(pos[1] + 0.2 * scale[1])),
            (round(scale[0] * 0.6), round(scale[1] * 0.6)), angle))

    def __init__(self, world):
        self.solid_objects = []
        self.deco_objects = []
        self.interactive_objects = []

        if (world == 0): #bright
            self.images = {
                'siege': pygame.image.load("assets/props/pos/solid/siege.png"),
                'solid_lamp': pygame.image.load("assets/props/pos/solid/lamp.png"),
                'deco_lamp': pygame.image.load("assets/props/pos/deco/lamp.png"),
                'os': pygame.image.load("assets/props/pos/deco/os.png"),
                'train': pygame.image.load("assets/props/pos/deco/train.png"),
                'locomotive': pygame.image.load("assets/props/pos/deco/locomotive.png"),
                'train_circuit': pygame.image.load("assets/props/pos/deco/train_circuit.png"),
                'button': pygame.image.load("assets/props/pos/interactive/button.png"),
                'bed': pygame.image.load("assets/props/pos/solid/lit_pos.png"),
                'bed_table': pygame.image.load("assets/props/pos/solid/table_de_nuit_pos.png"),
                'bed+table': pygame.image.load("assets/props/pos/solid/lit.png"),
                'armoire': pygame.image.load("assets/props/pos/solid/armoire.png"),
                'kitchen': pygame.image.load("assets/props/pos/solid/cuisine.png"),
                'table_01': pygame.image.load("assets/props/pos/solid/table_01.png"),
                'table_02': pygame.image.load("assets/props/pos/solid/table_02.png"),
                'table_03': pygame.image.load("assets/props/pos/solid/table_02.png"),
                'table': pygame.image.load("assets/props/pos/solid/table.png"),
                'chaise': pygame.image.load("assets/props/pos/solid/chaise.png")
            }
            self.solid_objects.append(SolidObject(self.images['siege'], (200, 200), (140, 120), -95))
            self.solid_objects.append(SolidObject(self.images['siege'], (200, 400), (140, 120), -85))
            self.solid_objects.append(SolidObject(self.images['siege'], (850, 650), (140, 120), 4))

            #room 15
            self.solid_objects.append(SolidObject(self.images['bed+table'], (-1930, 350), (153, 170), 0))
            self.lamp((-1830, 350), (50, 50), 0)
            self.solid_objects.append(SolidObject(self.images['bed+table'], (-1740, 350), (153, 170), 0))
            self.lamp((-1640, 350), (50, 50), 0)
            self.solid_objects.append(SolidObject(self.images['bed+table'], (-1540, 350), (153, 170), 0))
            self.lamp((-1440, 350), (50, 50), 0)
            self.solid_objects.append(SolidObject(self.images['bed+table'], (-1340, 350), (153, 170), 0))
            self.lamp((-1240, 350), (50, 50), 0)
            self.solid_objects.append(SolidObject(self.images['bed+table'], (-1140, 350), (153, 170), 0))
            self.lamp((-1040, 350), (50, 50), 0)
            self.solid_objects.append(SolidObject(self.images['siege'], (-1940, 1640), (100, 67), -45))
            self.solid_objects.append(SolidObject(self.images['siege'], (-1110, 1640), (100, 67), 45))

            #room 12
            self.solid_objects.append(SolidObject(self.images['armoire'], (-2570, 632), (310, 200), -90))

            #room 14
            self.interactive_objects.append(InteractiveObject(self.images['armoire'], (-3040, -3213), (200, 100), 0,
                "The cabinet is stuck ...", "it seems difficult to turn it", ""))
            self.solid_objects.append(SolidObject(self.images['armoire'], (-3040, -3213), (200, 100), 0))
            self.solid_objects.append(SolidObject(self.images['siege'], (-2740, -3213), (150, 100), 180))

            #room 16
            self.interactive_objects.append(InteractiveObject(self.images['train_circuit'], (-2900, 1500), (150, 150), 80,
                "Someone played here..", "", ""))
            self.deco_objects.append(DecoObject(self.images['train'], (-2780, 1540), (100, 80), 50))
            self.deco_objects.append(DecoObject(self.images['locomotive'], (-2880, 1585), (50, 50), 90))

            #self.deco_objects.append(DecoObject(self.images['os'], (800, 400), (50, 80), 120))
            self.deco_objects.append(DecoObject(self.images['train_circuit'], (600 + 100, 0), (150, 150), 80))
            self.deco_objects.append(DecoObject(self.images['train'], (720 + 100, 40), (100, 80), 50))
            self.deco_objects.append(DecoObject(self.images['locomotive'], (620 + 100, 85), (50, 50), 90))

            self.lamp((210, 550), (100, 100), 0)

            self.solid_objects.append(SolidObject(self.images['armoire'], (1080, 2585), (310, 120), 180))
            self.solid_objects.append(SolidObject(self.images['armoire'], (1530, 2585), (310, 120), 180))

            self.solid_objects.append(SolidObject(self.images['siege'], (2400, 150), (140, 120), -180))

            self.solid_objects.append(SolidObject(self.images['siege'], (2700, 350), (140, 120), 3))
            self.solid_objects.append(SolidObject(self.images['siege'], (3000, 350), (140, 120), -10))

            self.solid_objects.append(SolidObject(self.images['kitchen'], (900, 3495), (820, 484), 0))
            self.solid_objects.append(SolidObject(self.images['kitchen'], (-400, 3495), (820, 484), 0))
            for x in range(7):
                for y in range(2):
                    n = random.randint(1, 3)
                    self.solid_objects.append(SolidObject(self.images['table_0' + str(n)],
                        (-500 + x * 350, 2850 + y * 330), (210, 190), random.randint(-6, 6) + 180))

            self.solid_objects.append(SolidObject(self.images['bed'], (300, -89), (160, 260), 0))
            self.solid_objects.append(SolidObject(self.images['bed_table'], (228, -85), (60, 70), 9))
            self.solid_objects.append(SolidObject(self.images['armoire'], (985, 250), (200, 100), 90))

            self.interactive_objects.append(InteractiveObject(self.images['os'], (800, 400), (50, 80), 120,
                "this is an os", "Crazy Insane...", "...Insane Crazy !"))
            self.interactive_objects.append(InteractiveObject(self.images['button'], (5000, 77), (39, 24), -90,
                "This button seems to lead to the", "exit", ""))
        else:
            self.images = {
                'siege': pygame.image.load("assets/props/neg/solid/siege.png"),
                'solid_lamp': pygame.image.load("assets/props/neg/solid/lamp.png"),
                'deco_lamp': pygame.image.load("assets/props/neg/deco/lamp.png"),
                'os': pygame.image.load("assets/props/neg/deco/os.png"),
                'train': pygame.image.load("assets/props/neg/deco/train.png"),
                'locomotive': pygame.image.load("assets/props/neg/deco/locomotive.png"),
                'train_circuit': pygame.image.load("assets/props/neg/deco/train_circuit.png"),
                'bed': pygame.image.load("assets/props/neg/solid/lit.png"),
                'bed_table': pygame.image.load("assets/props/neg/solid/table_de_nuit_neg.png"),
                'bed+table': pygame.image.load("assets/props/neg/solid/lit_neg.png"),
                'armoire': pygame.image.load("assets/props/neg/solid/armoire.png"),
                'kitchen': pygame.image.load("assets/props/neg/solid/cuisine.png"),
                'table_01': pygame.image.load("assets/props/neg/solid/table_01.png"),
                'table_02': pygame.image.load("assets/props/neg/solid/table_02.png"),
                'table_03': pygame.image.load("assets/props/neg/solid/table_02.png"),
                'table': pygame.image.load("assets/props/neg/solid/table.png"),
                'chaise': pygame.image.load("assets/props/neg/solid/chaise.png")
            }
            self.solid_objects.append(SolidObject(self.images['siege'], (200, 200), (140, 120), -95))
            self.solid_objects.append(SolidObject(self.images['siege'], (200, 400), (140, 120), -85))
            self.solid_objects.append(SolidObject(self.images['siege'], (850, 650), (140, 120), 184))

            self.deco_objects.append(DecoObject(self.images['train_circuit'], (600 + 100, 0), (150, 150), 80))
            self.deco_objects.append(DecoObject(self.images['train'], (720 + 100, 40), (100, 80), 50))
            self.deco_objects.append(DecoObject(self.images['locomotive'], (705 + 100, 50), (50, 50), 257))

            self.deco_objects.append(DecoObject(self.images['os'], (800, 400), (50, 80), 120))

            self.lamp((210, 550), (100, 100), 0)

            self.lamp((1700, 150), (100, 100), 0)
            self.lamp((1700, 390), (100, 100), 0)

            self.solid_objects.append(SolidObject(self.images['kitchen'], (900, 3495), (820, 484), 0))
            self.solid_objects.append(SolidObject(self.images['kitchen'], (-400, 3495), (820, 484), 0))
            for x in range(7):
                for y in range(2):
                    n = random.randint(1, 3)
                    self.solid_objects.append(SolidObject(self.images['table_0' + str(n)],
                        (-500 + x * 350, 2850 + y * 330), (210, 190), random.randint(-6, 6) + 180))

            self.solid_objects.append(SolidObject(self.images['bed'], (300, -89), (160, 260), 0))
            self.solid_objects.append(SolidObject(self.images['bed_table'], (228, -85), (60, 70), 9))
            self.solid_objects.append(SolidObject(self.images['armoire'], (960, 405), (200, 100), 83))

            self.solid_objects.append(SolidObject(self.images['bed+table'], (-1930, 350), (153, 170), 0))
            self.solid_objects.append(SolidObject(self.images['bed+table'], (-1740, 350), (153, 170), 0))
            self.solid_objects.append(SolidObject(self.images['bed+table'], (-1540, 350), (153, 170), 0))
            self.solid_objects.append(SolidObject(self.images['bed+table'], (-1340, 350), (153, 170), 0))
            self.solid_objects.append(SolidObject(self.images['bed+table'], (-1140, 350), (153, 170), 0))

            #tas d'os 15
            self.deco_objects.append(DecoObject(self.images['os'], (-1440, 1200), (50, 80), 120))
            self.deco_objects.append(DecoObject(self.images['os'], (-1442, 1200), (50, 80), 80))
            self.deco_objects.append(DecoObject(self.images['os'], (-1443, 1201), (50, 80), 30))
            self.deco_objects.append(DecoObject(self.images['os'], (-1440, 1198), (50, 80), -43))
            self.deco_objects.append(DecoObject(self.images['os'], (-1441, 1201), (50, 80), 0))
            self.deco_objects.append(DecoObject(self.images['os'], (-1439, 1199), (50, 80), 105))
            self.deco_objects.append(DecoObject(self.images['os'], (-1439, 1200), (50, 80), -78))
            self.deco_objects.append(DecoObject(self.images['os'], (-1444, 1207), (50, 80), 3))
            self.deco_objects.append(DecoObject(self.images['os'], (-1442, 1213), (50, 80), -32))
            self.deco_objects.append(DecoObject(self.images['os'], (-1446, 129), (50, 80), -76))
            self.deco_objects.append(DecoObject(self.images['os'], (-1444, 1183), (50, 80), 165))
            self.deco_objects.append(DecoObject(self.images['os'], (-1444, 1212), (50, 80), -178))
            self.deco_objects.append(DecoObject(self.images['os'], (-1436, 1184), (50, 80), 98))
            self.interactive_objects.append(InteractiveObject(self.images['os'], (-1434, 1220), (50, 80), -7,
                "It's weird..", "", ""))

            #room 14
            self.solid_objects.append(SolidObject(self.images['armoire'], (-3040, -3213), (200, 100), 180))
            self.interactive_objects.append(InteractiveObject(self.images['armoire'], (-3040, -3213), (200, 100), 180,
                "There are plenty of clothes.", "Different sizes..", ""))
            self.solid_objects.append(SolidObject(self.images['siege'], (-2740, -3213), (150, 100), 180))
            self.interactive_objects.append(InteractiveObject(self.images['os'], (-2720, -3170), (50, 80), 180,
                "Someone died here", "", "..."))

            self.solid_objects.append(SolidObject(self.images['armoire'], (-2900, 702), (310, 200), -45))
            self.deco_objects.append(DecoObject(self.images['os'], (-2900, 1500), (50, 80), -7))

            self.interactive_objects.append(InteractiveObject(self.images['os'], (800, 400), (50, 80), 120,
                "this is an os", "Crazy Insane...", "...Insane Crazy !"))
    def update(self, screen, player):
        for i in self.deco_objects:
            i.update(screen, player)
        for i in self.interactive_objects:
            i.update(screen, player)
        for i in self.solid_objects:
            i.update(screen, player)