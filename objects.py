##
## EPITECH PROJECT, 2021
## GGJ
## File description:
## objects
##

import pygame

class InteractiveObject(pygame.sprite.Sprite):
    def __init__(self, image, position, scale, text):
        super().__init__
        self.image = image
        self.image = pygame.transform.scale(self.image, scale)
        self.rect = self.image.get_rect()
        self.text = text
        self.x = position[0]
        self.y = position[1]
    def collision(self, player):
        return (self.rect.colliderect(player.rect))

    def update(self, screen, player):
        self.rect.x = self.x - player.x
        self.rect.y = self.y - player.y
        if self.collision(player):
            print("ok")
        else:
            print("pas ok")
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


class Objects(pygame.sprite.Sprite):
    def __init__(self):
        self.images = {
            'siege': pygame.image.load("assets/props/siege.png")
        }
        self.solid_objects = []
        self.solid_objects.append(SolidObject(self.images['siege'], (200, 200), (140, 120), -90))
        self.solid_objects.append(SolidObject(self.images['siege'], (400, 200), (140, 120), 0))

    def update(self, screen, player):
        for i in self.solid_objects:
            i.update(screen, player)