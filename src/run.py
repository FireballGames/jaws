#!/usr/bin/env python
"""
Used to run game
"""
from game.game import Game
from screens.main import MainScreen
from globals import BLOCK, CAPTION, FPS
from screens import Intro



class Jaws(Game):
    init_scene = 'main'

    width = 32 * BLOCK
    height = 24 * BLOCK

    def __init__(self):
        super().__init__(CAPTION, (self.width, self.height), FPS)

        # self.main_screen = MainScreen(self)
        # self.pause_screen = Pause(self)
        # self.game_over_screen = Crash(self)

        self.ms = MainScreen()

        # self.add_scene('intro', Screen(self))
        self.add_scene('main', Intro(self))
        # self.add_scene('main', Screen(self))
        # self.add_scene('pause', Screen(self))
        # self.add_scene('game_over', Screen(self))

        """
        # Logo and title screens
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


def main():
    game = Jaws()
    game.play()
    game.stop()


if __name__ == "__main__":
    # path = os.path.abspath(os.path.dirname(sys.argv[0]))
    # sys.path.append(path)
    # sys.path.append(os.path.join(path, "src"))
    # main(path)

    main()
