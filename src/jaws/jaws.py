from config import CAPTION, FPS
from game.game import Game

from .screens.intro import Intro
from .screens.title import Title
from .screens.cutscene import CutScene
from .screens.main import MainScreen

from resource.cutscenes import LogoResource


class Jaws(Game):
    init_scene = 'logo'

    width = 640  # 32 * BLOCK
    height = 480  # 24 * BLOCK

    def __init__(self):
        super().__init__(CAPTION, (self.width, self.height), FPS)

        resource = LogoResource()
        self.scene_data = resource.data()

        self.ms = MainScreen()

        # Logo and title screens
        self.add_scene('logo', CutScene(self))
        self.add_scene('intro', CutScene(self))
        self.add_scene('title', Title(self))

        self.add_scene('main', Intro(self))
        # self.add_scene('main', Screen(self))
        # self.add_scene('pause', Screen(self))
        # self.add_scene('game_over', Screen(self))

        # self.main_screen = MainScreen(self)
        # self.pause_screen = Pause(self)
        # self.game_over_screen = Crash(self)

        """
        logocutscene = CutScene(self.director, self.screen_size)
        self.director.add_scene('logocutscene', logocutscene)

        titlescene = TitleScreen(self.director, self.screen_size)
        titlescene.savepath = os.path.join(self.path, 'data', 'saved_progress.txt')
        self.director.add_scene('titlescene', titlescene)

        # Load game scenes
        maingame = MainGame(self.director, self.screen_size)
        maingame.progress_data.savepath = os.path.join(self.path, 'data', 'saved_progress.txt')
        self.director.add_scene('maingame', maingame)
        titlescene.h_progress_data = maingame.progress_data

        pausescene = PauseScreen(self.director, self.screen_size)
        self.director.add_scene('pausescene', pausescene)
        maingame.h_pausescene = pausescene
        pausescene.h_maingame = maingame

        # Cutscenes
        cutscenes = [
            'introcutscene',
            'cutscene1',
            'cutscene2',
            'cutscene3',
            'cutscene4',
            'cutscene5',
        ]
        for name in cutscenes:
            cutscene = CutScene(self.director, self.screen_size)
            self.director.add_scene(name, cutscene)
        """
