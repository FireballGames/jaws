import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *


class Game3D:
    def __init__(self, caption=SCREEN_CAPTION, size=(SCREEN_WIDTH, SCREEN_HEIGHT)):
        self.fps = 5

        pygame.init()

        pygame.display.set_mode(size, DOUBLEBUF|OPENGL)

        # self.window = pygame.display.set_mode(size)
        # pygame.display.set_caption(caption)

        self.state = STATE_RUN

        # self.intro_screen = Screen(self)
        # self.main_screen = Screen(self)
        # self.pause_screen = Screen(self)
        # self.game_over_screen = Screen(self)

    def play(self):
         while self.state == STATE_RUN:
             self.show()

    def show(self):
        # Read events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.state = STATE_QUIT
            self.events(event)

        # Controlling keys
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            self.state = STATE_QUIT

        self.key_event(keys)

        self.draw()

        pygame.display.flip()
        pygame.time.wait(5)

    def events(self, event):
        pass

    def key_event(self, keys):
        pass

    def draw(self):
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
