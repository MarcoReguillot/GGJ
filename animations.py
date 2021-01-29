import pygame

def create_animation(prefix, number,suffix):
    images = []
    for i in range(number):
        images.append(pygame.image.load(prefix + i + suffix))
    return images
