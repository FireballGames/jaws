import os
import pygame

from config.globals import RES_ROOT


class Background(pygame.sprite.Sprite):
    filename = "map.png"

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join(RES_ROOT, self.filename))
        self.rect = pygame.Rect((0, 0, self.image.get_width(), self.image.get_height()))
