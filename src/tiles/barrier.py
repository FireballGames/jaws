import os
import pygame

from config.globals import BLOCK, RES_ROOT


class Tile(pygame.sprite.Sprite):
    filename = "barrier.png"
    offsets = {
        "A": (0, 0),
        "B": (1, 0),
        "C": (2, 0),
        "D": (3, 0),
        "E": (4, 0),
        "F": (5, 0),
        "G": (0, 1),
        "H": (1, 1),
        "I": (2, 1),
        "J": (3, 1),
        "K": (4, 1),
        "L": (5, 1),
        "M": (0, 2),
        "N": (1, 2),
        "O": (2, 2),
        "P": (3, 2),
        "Q": (4, 2),
        "R": (5, 2),
        "S": (0, 3),
        "T": (1, 3),
        "U": (2, 3),
        "V": (3, 3),
        "W": (4, 3),
        "X": (5, 3),
    }

    def __init__(self, x, y, code):
        super().__init__()

        self.width = BLOCK
        self.height = BLOCK

        offset = self.offsets[code]

        image = pygame.image.load(os.path.join(RES_ROOT, "tiles", self.filename))
        rect = pygame.Rect((offset[0] * BLOCK, offset[1] * BLOCK, self.width, self.height))

        self.rect = pygame.Rect((x * BLOCK, y * BLOCK, self.width, self.height))
        self.image = pygame.Surface(rect.size).convert()
        self.image.blit(image, (0, 0), rect)
        self.image.set_alpha(196)
