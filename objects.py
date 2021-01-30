##
## EPITECH PROJECT, 2021
## GGJ
## File description:
## objects
##

import pygame
from player import Player

class InteractiveObject(pygame.sprite.Sprite):
    def __init__(self, image, position, scale, text):
        super().__init__
        self.image = pygame.image.load(image)
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
