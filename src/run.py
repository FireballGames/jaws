from game.game import Game

BLOCK = 8
FPS = 32

class Jaws(Game):
    caption = "Jaws"
    width = 32 * BLOCK
    height = 24 * BLOCK

    def __init__(self):
        super().__init__(self.caption, (self.width, self.height))
        # Resource.load_images({
        #     'icon': "res/racecar.png",
        #     'car': "res/racecar.png",
        # })

        # self.intro_screen = Intro(self)
        # self.main_screen = MainScreen(self)
        # self.pause_screen = Pause(self)
        # self.game_over_screen = Crash(self)


def main():
    game = Jaws()
    game.play()
    game.quit()


if __name__ == "__main__":
    main()
