# Camera

import pygame

class Camera(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__
        self.image = pygame.image.load("assets/cam/cam.png")
        self.image = pygame.transform.scale(self.image, (400, 500))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rotation_speed = 5
        self.rotation_degree = 0, 0
        self.x = 0
        self.y = 0

    def change_behavior(self, rotation_speed, rotation_degree, position):
        self.rotation_speed = rotation_speed
        self.rotation_degree = rotation_degree
        self.x = position[0]
        self.y = position[1]

    def detect(self, sprite):
        #print(sprite.rect)
        #print(self.rect)
        if (pygame.sprite.collide_mask(self, sprite)):
            return (True)
        else:
            return (False)

    def display(self, screen, x, y):
        screen.blit(self.image, (self.x - x, self.y - y))
        self.rect.x = self.x - x
        self.rect.y = self.y - y