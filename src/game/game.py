import pygame
import config.game as config
from resource.jaws import JawsResources
from .director import Director


class Game(Director):
    init_scene = None
    scene_data = []

    def __init__(self, caption=config.SCREEN_CAPTION, size=(config.SCREEN_WIDTH, config.SCREEN_HEIGHT), fps=config.FPS):
        # Set fields
        self.size = size
        self.caption = caption
        self.fps = fps

        # Initialize pygame
        pygame.init()
        # pygame.mixer.init()

        # Show window
        self.window = pygame.display.set_mode(self.size)
        pygame.display.set_caption(self.caption)

        # Initialize Director
        super().__init__(self.window, self.fps)

        # Load resources
        # self.path = path
        JawsResources.load(config.PATH, self.size)
        # self.resources = Resources(self.path, self.screen_size)
        # pygame.display.set_icon(Resource.image('icon'))

    def play(self):
        # Start up director
        self.set_scene(self.init_scene, *self.scene_data)

        super().play()

    def stop(self):
        pygame.quit()
