import os
import pygame

from globals import BLOCK, RES_ROOT
from data.game_map import GAME_MAP
from brody import Brody
from tiles.barrier import Barrier


MAIN_WIDTH = BLOCK * 32
MAIN_HEIGHT = BLOCK * 20

X_BOUNDS = (0, 32 * BLOCK)
Y_BOUNDS = (0, 20 * BLOCK)

class Field(pygame.sprite.Group):
    tiles = (None, Barrier)

    def __init__(self, game_map, x):
        super().__init__()

        self.game_map = game_map
        self.x = x
        self.y = 0

    def load(self):
        level_row = self.game_map[self.y]
        level_map = level_row[self.x]

        self.empty()
        for y, row in enumerate(level_map):
            for x, sprite_id in enumerate(row):
                sprite = self.tiles[sprite_id]
                if sprite is None:
                    continue

                self.add(sprite(x, y))

    def slide(self, x, y):
        self.x += x

        if self.x < 0:
            self.x = len(self.game_map[self.y]) - 1
        if self.x >= len(self.game_map[self.y]):
            self.x = 0

        self.y += y
        print(self.y)
        if self.y < 0:
            self.y = 0
        if self.y >= len(self.game_map):
            print("DOWN")
            self.y = len(self.game_map) - 1

        print((self.x, self.y))
        self.load()

    def move_in(self, movement, sprite):
        x, y = movement

        new_rect = sprite.rect.move(x, y)
        if new_rect.left < X_BOUNDS[0]:
            new_rect.right = X_BOUNDS[1]
            self.slide(-1, 0)
            print("left")
        if new_rect.right > X_BOUNDS[1]:
            new_rect.left = X_BOUNDS[0]
            self.slide(1, 0)
            print("right")
        if new_rect.top < Y_BOUNDS[0]:
            new_rect.bottom = Y_BOUNDS[1]
            self.slide(0, -1)
            print("top")
        if new_rect.bottom > Y_BOUNDS[1]:
            new_rect.top = Y_BOUNDS[0]
            self.slide(0, 1)
            print("down")

        return new_rect


class MainScreen(pygame.Surface):
    def __init__(self):
        super().__init__((MAIN_WIDTH, MAIN_HEIGHT))

        self.bg_color = (0, 0, 0)

        self.brody = Brody()
        self.players = pygame.sprite.GroupSingle(self.brody)

        self.field = Field(GAME_MAP, 12)
        self.field.load()

        self.update()

    def update(self):
        self.players.update(self.field)

        self.fill(self.bg_color)

        self.field.draw(self)
        self.players.draw(self)
