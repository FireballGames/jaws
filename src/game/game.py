import os
import sys
import pygame

from .states import *

from resource import JawsResources

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 1024
SCREEN_CAPTION = "Game"


PATH = os.path.abspath(os.path.dirname(sys.argv[0]))


class Director:
    def __init__(self, screen, fps):
        self.screen = screen

        self.clock = pygame.time.Clock()
        self.fps = fps
        self.time = 0
        self.framerate = 0
        self.frame = 0
        self.elapsed = 0

        self.state = STATE_INTRO

        self.scene = None
        self.scenes = dict()

    def play(self):
        while self.state != STATE_QUIT:
            # Framerate
            self.time = self.clock.tick(self.fps)
            """
            self.framerate = 1000.0 / self.time
            self.frame += 1
            self.elapsed += self.time
            """

            # Exit events
            events = []
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                else:
                    events.append(event)

            # Detect events
            self.scene.event(events)

            # Update scene
            self.scene.update()

            # Draw the screen
            self.scene.draw(self.screen)

            """
            while self.state == STATE_INTRO:
                self.intro_screen.show()
            while self.state == STATE_RUN:
                self.main_screen.show()
            while self.state == STATE_PAUSED:
                self.pause_screen.show()
            while self.state == STATE_GAME_OVER:
                self.game_over_screen.show()
            """

            """
            b_movie = False
            movie_framerate = 15
            outnumoffset = 0
            if b_movie and self.frame % (self.fps / movie_framerate) == 0:
                filename = "screens/screen_%04d.jpg" % (self.frame / (self.fps / movie_framerate) + outnumoffset)
                pygame.image.save(self.screen, filename)
                # pygame.image.save(self.screen,"screens/screen_%04d.png"%(self.frame/(self.fps/movie_framerate) + outnumoffset))
            """

            pygame.display.update()
            # pygame.display.flip()

    def add_scene(self, name, scene):
        self.scenes[name] = scene

    def set_scene(self, name, *options):
        print(name, self.scenes)
        self.scene = self.scenes.get(name)

        if name is None:
            self.quit()
            return
        self.scene.load(*options)

    def quit(self):
        self.state = STATE_QUIT


class Game(Director):
    init_scene = None
    scene_data = []

    def __init__(self, caption=SCREEN_CAPTION, size=(SCREEN_WIDTH, SCREEN_HEIGHT), fps=30):
        self.size = size
        self.caption = caption

        # Initialise pygame
        pygame.init()
        # pygame.mixer.init()

        self.window = pygame.display.set_mode(self.size)
        pygame.display.set_caption(self.caption)

        self.fps = fps
        super().__init__(self.window, self.fps)

        # Load resources
        # self.path = path
        JawsResources.load(PATH, self.size)
        # self.resources = Resources(self.path, self.screen_size)
        # pygame.display.set_icon(Resource.image('icon'))

    def play(self):
        # Start up director
        self.set_scene(self.init_scene, *self.scene_data)

        super().play()


    def stop(self):
        pygame.quit()
