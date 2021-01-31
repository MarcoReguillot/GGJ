##
## EPITECH PROJECT, 2021
## GGJ
## File description:
## objects
##

import pygame
import math

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
            }
            self.solid_objects.append(SolidObject(self.images['siege'], (200, 200), (140, 120), -95))
            self.solid_objects.append(SolidObject(self.images['siege'], (200, 400), (140, 120), -85))
            self.solid_objects.append(SolidObject(self.images['siege'], (850, 650), (140, 120), 4))

            #self.deco_objects.append(DecoObject(self.images['os'], (800, 400), (50, 80), 120))
            self.deco_objects.append(DecoObject(self.images['train_circuit'], (600 + 100, 0), (150, 150), 80))
            self.deco_objects.append(DecoObject(self.images['train'], (720 + 100, 40), (100, 80), 50))
            self.deco_objects.append(DecoObject(self.images['locomotive'], (620 + 100, 85), (50, 50), 90))

            self.lamp((210, 550), (100, 100), 0)

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
                'bed': pygame.image.load("assets/props/neg/solid/lit_neg.png"),
                'bed_table': pygame.image.load("assets/props/neg/solid/table_de_nuit_neg.png")
            }
            self.solid_objects.append(SolidObject(self.images['siege'], (200, 200), (140, 120), -95))
            self.solid_objects.append(SolidObject(self.images['siege'], (200, 400), (140, 120), -85))
            self.solid_objects.append(SolidObject(self.images['siege'], (850, 650), (140, 120), 184))

            self.deco_objects.append(DecoObject(self.images['train_circuit'], (600 + 100, 0), (150, 150), 80))
            self.deco_objects.append(DecoObject(self.images['train'], (720 + 100, 40), (100, 80), 50))
            self.deco_objects.append(DecoObject(self.images['locomotive'], (705 + 100, 50), (50, 50), 257))

            self.deco_objects.append(DecoObject(self.images['os'], (800, 400), (50, 80), 120))

            self.lamp((210, 550), (100, 100), 0)

            self.interactive_objects.append(InteractiveObject(self.images['os'], (800, 400), (50, 80), 120,
                "this is an os", "Crazy Insane...", "...Insane Crazy !"))

    def update(self, screen, player):
        for i in self.deco_objects:
            i.update(screen, player)
        for i in self.interactive_objects:
            i.update(screen, player)
        for i in self.solid_objects:
            i.update(screen, player)