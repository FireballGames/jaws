import pygame

from config import MAIN_WIDTH, MAIN_HEIGHT, X_BOUNDS, Y_BOUNDS
from data.game_map import GAME_MAP
from jaws.sprites.brody import Brody
from jaws.sprites.tiles.barrier import Tile
from jaws.sprites.tiles import Background


class Field(pygame.sprite.Group):
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
                """
                i = x % 4
                j = y % 2
                print("SPRITE", i, j)
                if sprite_id == 1:
                    if not j:
                        print(len(TILES), j, 8 + i)
                        sprite_id = 8 + i
                    else:
                        print(len(TILES), j, 13 + i)
                        sprite_id = 13 + i
                elif sprite_id == 2:
                    sprite_id = 2 + i
                    pass
                """
                if sprite_id == " ":
                    continue

                sprite = Tile(x, y, sprite_id)
                self.add(sprite)

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
        self.background = Background()

        self.brody = Brody()
        self.players = pygame.sprite.GroupSingle(self.brody)

        self.field = Field(GAME_MAP, 12)
        self.field.load()

        self.update()

    def update(self):
        self.players.update(self.field)

        self.fill(self.bg_color)
        rect = (
            self.field.x * MAIN_WIDTH,
            self.field.y * MAIN_HEIGHT,
            MAIN_WIDTH,
            MAIN_HEIGHT
        )
        self.blit(self.background.image, (0, -1), rect)

        self.field.draw(self)
        self.players.draw(self)
