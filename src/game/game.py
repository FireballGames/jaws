import pygame
from pygame.locals import *

from .states import *
from .screen import Screen


SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 1024
SCREEN_CAPTION = "Game"


class Game:
    def __init__(self, caption=SCREEN_CAPTION, size=(SCREEN_WIDTH, SCREEN_HEIGHT)):
        pygame.init()
        self.window = pygame.display.set_mode(size)
        pygame.display.set_caption(caption)

        self.state = STATE_INTRO

        self.intro_screen = Screen(self)
        self.main_screen = Screen(self)
        self.pause_screen = Screen(self)
        self.game_over_screen = Screen(self)

        # pygame.display.set_icon(Resource.image('icon'))

    def play(self):
        while self.state != STATE_QUIT:
            while self.state == STATE_INTRO:
                self.intro_screen.show()
            while self.state == STATE_RUN:
                self.main_screen.show()
            while self.state == STATE_PAUSED:
                self.pause_screen.show()
            while self.state == STATE_GAME_OVER:
                self.game_over_screen.show()

    def quit(self):
        pygame.quit()
