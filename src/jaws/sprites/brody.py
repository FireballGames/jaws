import os
import pygame

from config import BRODY_WIDTH, BRODY_HEIGHT, BRODY_X, BRODY_Y, RES_ROOT

from ..controls import LEFT, RIGHT


class Brody(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.width = BRODY_WIDTH
        self.height = BRODY_HEIGHT

        self.direction = LEFT

        self.speed = 4

        # if self.image is None:
        #     self.image = pygame.image.load(os.path.join(RES_ROOT, "brody.png"))
        self.base_image = pygame.image.load(os.path.join(RES_ROOT, "brody.png"))
        self.image = self.base_image

        self.rect = pygame.Rect((BRODY_X, BRODY_Y, self.width, self.height))
        self.movement = (0, 0)

    def update(self, field=None, *args):
        old_rect = self.rect
        self.rect = field.move_in(self.movement, self)
        if pygame.sprite.spritecollideany(self, field):
            self.rect = old_rect

    def move(self, x, y, field):
        if x > 0:
            self.image = pygame.transform.flip(self.base_image, True, False)
            self.direction = RIGHT
        elif x < 0:
            self.image = self.base_image
            self.direction = LEFT

        self.movement = (x * self.speed, y * self.speed)
        self.update(field)
