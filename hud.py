##
## EPITECH PROJECT, 2021
## GGJ
## File description:
## hud
##

import pygame
import pygame.freetype
import math

pygame.freetype.init()

GAME_FONT = pygame.freetype.Font("assets/font.ttf", 50)

def pos(value):
    if (value < 0):
        return (0)
    else:
        return math.floor(value)

class HudText(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__
        self.text = ""
        self.line2 = ""
        self.line3 = ""
        self.display_speed = 25
        self.moment = 0
        self.script_image = pygame.image.load("assets/hud/script.png")
        self.script_image_dark = pygame.image.load("assets/hud/script_dark.png")
        self.script_image = pygame.transform.scale(self.script_image, (1000, 300))
        self.script_image_dark = pygame.transform.scale(self.script_image_dark, (1000, 300))
        self.display_script = True

    def render_text(self, line1, line2, line3):
        self.text = line1
        self.line2 = line2
        self.line3 = line3
        self.display_script = True
        self.moment = 3

    def hide_text(self):
        if self.text == "This button seems to lead to the":
            exit (0)
        self.display_script = False

    def update(self, screen, space, clock):
        if self.display_script:
            len1 = len(self.text)
            len2 = len(self.line2)
            if (clock != 0):
                self.moment += self.display_speed / clock
            if (space == 1):
                screen.blit(self.script_image, (140, 720 - 300))
                GAME_FONT.render_to(screen, (260, 720 - 220), self.text[0:math.floor(self.moment)], (0, 0, 0))
                GAME_FONT.render_to(screen, (260, 720 - 175), self.line2[0:pos(self.moment - len1)], (0, 0, 0))
                GAME_FONT.render_to(screen, (260, 720 - 130), self.line3[0:pos(self.moment - len1 - len2)], (0, 0, 0))
            else:
                screen.blit(self.script_image_dark, (140, 720 - 300))
                GAME_FONT.render_to(screen, (260, 720 - 220), self.text[0:math.floor(self.moment)], (255, 255, 255))
                GAME_FONT.render_to(screen, (260, 720 - 175), self.line2[0:pos(self.moment - len1)], (255, 255, 255))
                GAME_FONT.render_to(screen, (260, 720 - 130), self.line3[0:pos(self.moment - len1 - len2)], (255, 255, 255))