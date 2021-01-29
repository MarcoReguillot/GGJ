import pygame

def create_animation(prefix, number,suffix, size):
    images = []
    for i in range(number):
        images.append(pygame.image.load(prefix + str(i) + suffix))
        images[i] = pygame.transform.scale(images[i], size)
    return images
