##
## EPITECH PROJECT, 2021
## GGJ
## File description:
## hud
##

import pygame
import pygame.freetype

pygame.freetype.init()

GAME_FONT = pygame.freetype.Font("assets/font.ttf", 50)

class HudText(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__
        self.text = ""
        self.line2 = ""
        self.line3 = ""
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

    def hide_text(self):
        self.display_script = False

    def update(self, screen, space):
        if self.display_script:
            if (space == 1):
                screen.blit(self.script_image, (140, 720 - 300))
                GAME_FONT.render_to(screen, (260, 720 - 220), self.text, (0, 0, 0))
                GAME_FONT.render_to(screen, (260, 720 - 175), self.line2, (0, 0, 0))
                GAME_FONT.render_to(screen, (260, 720 - 130), self.line3, (0, 0, 0))
            else:
                screen.blit(self.script_image_dark, (140, 720 - 300))
                GAME_FONT.render_to(screen, (260, 720 - 220), self.text, (255, 255, 255))
                GAME_FONT.render_to(screen, (260, 720 - 175), self.line2, (255, 255, 255))
                GAME_FONT.render_to(screen, (260, 720 - 130), self.line3, (255, 255, 255))