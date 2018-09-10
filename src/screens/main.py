import os
import pygame

from globals import BLOCK, RES_ROOT
from data.game_map import game_map
from brody import Brody
from tiles.barrier import Barrier


MAIN_WIDTH = BLOCK * 32
MAIN_HEIGHT = BLOCK * 20


class Field(pygame.sprite.Group):
    tiles = (None, Barrier)

    def __init__(self, game_map):
        super().__init__()
        self.load(game_map)

    def load(self, game_map):
        self.empty()
        for y, row in enumerate(game_map):
            for x, sprite_id in enumerate(row):
                sprite = self.tiles[sprite_id]
                if sprite is None:
                    continue

                self.add(sprite(x, y))


class MainScreen(pygame.Surface):
    def __init__(self):
        super().__init__((MAIN_WIDTH, MAIN_HEIGHT))

        self.bg_color = (0, 0, 0)

        self.brody = Brody()
        self.players = pygame.sprite.GroupSingle(self.brody)

        self.game_map = game_map
        self.field = Field(self.game_map)

        self.update()

    def update(self):
        self.players.update(self.field)

        self.fill(self.bg_color)

        self.field.draw(self)
        self.players.draw(self)
