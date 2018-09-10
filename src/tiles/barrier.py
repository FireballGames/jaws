import os
import pygame

from globals import BLOCK, RES_ROOT


class Barrier(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.width = BLOCK
        self.height = BLOCK

        self.image = pygame.image.load(os.path.join(RES_ROOT, "barrier.png"))

        self.rect = pygame.Rect((x * BLOCK, y * BLOCK, self.width, self.height))
