import os
import pygame

from globals import BLOCK, RES_ROOT


class Brody(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.width = 2 * BLOCK
        self.height = 2 * BLOCK

        self.speed = 4

        # if self.image is None:
        #     self.image = pygame.image.load(os.path.join(RES_ROOT, "brody.png"))
        self.image = pygame.image.load(os.path.join(RES_ROOT, "brody.png"))

        self.rect = pygame.Rect((15 * BLOCK, BLOCK, self.width, self.height))
        self.movement = (0, 0)

    def update(self, field=None, *args):
        old_rect = self.rect
        self.rect = field.move_in(self.movement, self)
        if pygame.sprite.spritecollideany(self, field):
            self.rect = old_rect

    def move(self, x, y, field):
        self.movement = (x * self.speed, y * self.speed)
        self.update(field)
