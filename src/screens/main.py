import os
import pygame

from globals import BLOCK, RES_ROOT
from data.game_map import game_map


MAIN_WIDTH = BLOCK * 32
MAIN_HEIGHT = BLOCK * 20


class MainScreen(pygame.Surface):
    tiles = [None, None]

    def __init__(self):
        super().__init__((MAIN_WIDTH, MAIN_HEIGHT))

        if self.tiles[1] is None:
            self.tiles[1] = pygame.image.load(os.path.join(RES_ROOT, "barrier.png"))

        self.game_map = ()
        self.load(game_map)

    def load(self, m):
        self.game_map = m

        for y, row in enumerate(self.game_map):
            for x, sprite_id in enumerate(row):
                sprite = self.tiles[sprite_id]
                if sprite is None:
                    continue
                self.blit(sprite, (x * BLOCK, y * BLOCK, BLOCK, BLOCK))
