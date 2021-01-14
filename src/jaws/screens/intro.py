import pygame

from game.screen import Screen

from config import INTRO_POS
from jaws.screens.main import MainScreen

from resource.jaws import JawsResources


class Intro(Screen):
    def __init__(self, game):
        super().__init__(game)

        self.pos = INTRO_POS
        self.ms = MainScreen()

        self.paused = False

    def key_event(self, keys):
        super().key_event(keys)

        if not self.paused:
            if keys[pygame.K_RIGHT]:
                self.ms.brody.move(1, 0, self.ms.field)
            if keys[pygame.K_LEFT]:
                self.ms.brody.move(-1, 0, self.ms.field)
            if keys[pygame.K_UP]:
                self.ms.brody.move(0, -1, self.ms.field)
            if keys[pygame.K_DOWN]:
                self.ms.brody.move(0, 1, self.ms.field)
        if keys[pygame.K_p]:
            self.paused = not self.paused

    def draw(self, window):
        super().draw(window)

        window.blit(JawsResources.backdrop, (0, 0))

        if not self.paused:
            self.ms.update()
        window.blit(self.ms, self.pos)
