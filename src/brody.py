import os
import pygame

from globals import BLOCK, RES_ROOT


X_BOUNDS = (0, 32 * BLOCK)
Y_BOUNDS = (0, 20 * BLOCK)


class Brody(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.width = 2 * BLOCK
        self.height = 2 * BLOCK

        # if self.image is None:
        #     self.image = pygame.image.load(os.path.join(RES_ROOT, "brody.png"))
        self.image = pygame.image.load(os.path.join(RES_ROOT, "brody.png"))

        self.rect = pygame.Rect((15 * BLOCK, BLOCK, self.width, self.height))
        self.movement = (0, 0)

    def update(self, *args):
        x, y = self.movement
        self.rect = self.rect.move(x, y)
        if self.rect.left < X_BOUNDS[0]:
            self.rect.left = X_BOUNDS[1] - self.width
            print("left")
        if self.rect.right > X_BOUNDS[1]:
            self.rect.right = X_BOUNDS[0] + self.width
            print("right")
        if self.rect.top < Y_BOUNDS[0]:
            self.rect.top = Y_BOUNDS[1] - self.height
            print("top")
        if self.rect.bottom > Y_BOUNDS[1]:
            self.rect.bottom = Y_BOUNDS[0] + self.height
            print("down")

    def move(self, x, y):
        self.movement = (x, y)
        self.update()
