import os
import pygame

# from game.states import STATE_QUIT, STATE_RUN
from game.screen import Screen

from controls.fade import Fade
from controls.menu import Menu, MenuItem

from config import INTRO_POS
from screens.main import MainScreen

from resource.jaws import JawsResources
from resource.cutscenes import TitleResource, IntroResource


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


class Title(Screen):
    def __init__(self, game):
        super().__init__(game)

        self.background = self.panel()

        self.start_game = False
        self.continue_game = False

        self.save = ""

        self.button_continue = None
        self.button_new = None
        self.top_menu = None

        self.fade = None

        self.resource = TitleResource()
        self.intro = IntroResource()

    def panel(self):
        panel = pygame.Surface(self.game.size)
        panel.fill((0, 0, 0))
        panel.convert()
        return panel

    def do_start_game(self):
        self.start_game = True

    def do_continue_game(self):
        self.continue_game = True

    def load(self):
        # Check music
        pygame.mixer.music.load(JawsResources.music_paths['pamgaea'])
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

        # top-level menu buttons
        pos_h1 = (self.game.size[0] / 2) - (self.resource.surfaces['continue_red'].get_width() / 2)
        pos_h2 = (self.game.size[0] / 2) - (self.resource.surfaces['newgame_red'].get_width() / 2)
        if os.path.isfile(self.save):
            self.button_continue = MenuItem(
                (pos_h1, 280),
                {
                    MenuItem.MENU_ITEM_INACTIVE: self.resource.surfaces['continue_red'],
                    MenuItem.MENU_ITEM_ACTIVE: self.resource.surfaces['continue_gold'],
                },
                self.do_continue_game
            )
            self.button_new = MenuItem(
                (pos_h2, 320),
                {
                    MenuItem.MENU_ITEM_INACTIVE: self.resource.surfaces['newgame_red'],
                    MenuItem.MENU_ITEM_ACTIVE: self.resource.surfaces['newgame_gold'],
                },
                self.do_start_game
            )
            self.buttons = [
                self.button_continue,
                self.button_new
            ]
        else:
            self.button_new = MenuItem(
                (pos_h2, 280),
                {
                    MenuItem.MENU_ITEM_INACTIVE: self.resource.surfaces['newgame_red'],
                    MenuItem.MENU_ITEM_ACTIVE: self.resource.surfaces['newgame_gold'],
                },
                self.do_start_game
            )
            self.buttons = [
                self.button_new
            ]
        self.top_menu = Menu(self.buttons, 0, JawsResources.controls)

        # fade in/out
        self.fade = Fade(30)

        # control
        self.start_game = False
        self.continue_game = False

        # run "game"
        # level_id = 'level_explore_001'

        # Initialise objects
        # self.camera = Camera(self.window_size)
        # self.tiledlayers = tilemap.TiledLayers()
        # self.submarine = submarine.Submarine()

        # set cross handles
        # self.tiledlayers.set_handles((self.camera, self.submarine))
        # self.submarine.set_handles((self.camera, self.tiledlayers))

        # Initialise physics space
        # self.space = pymunk.Space()
        # self.space.gravity = Vec2d(0.0, -450.0)

        # self.submarine.space = self.space
        # self.tiledlayers.space = self.space

        # load level data
        # self.tiledlayers.load_level(level_id)
        # # self.camera.UpdateCamera([int(self.submarine.body.position[0]),-int(self.submarine.body.position[1])])
        # self.camera.UpdateCamera([int(16 * self.tiledlayers.map_size[0]), int(16 * self.tiledlayers.map_size[1])])

        # Fade in game
        self.fade.fade_in()

    def update(self):
        # Update Boulders
        # self.tiledlayers.UpdateEffects()
        # self.tiledlayers.UpdateBoulders()
        # self.tiledlayers.UpdateBlocks()

        # Control fade in/out, look for end game cues
        self.fade.update()

        if self.fade.direction == self.fade.FADE_IN and (self.start_game or self.continue_game):
            self.fade.fade_out(True)

        if not self.fade.has_finished:
            return

        if self.start_game:
            print("START")
            # self.h_progress_data.Reset
            self.game.set_scene('intro', *self.intro.data())
            # self.director.change_scene('maingame', [True, "level_explore_001"])
        elif self.continue_game:
            print("CONTINUE")
            # self.h_progress_data.LoadProgressData()
            # self.director.change_scene('maingame', [True, self.h_progress_data.current_level])

    def event(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.game.set_scene(None)
            if event.type == pygame.KEYDOWN:
                self.top_menu.event(event)

    def draw(self, surface):
        # self.tiledlayers.RenderBackdrop(surface)
        # self.tiledlayers.RenderTileLayer(surface)
        # self.tiledlayers.RenderFishSchools(surface)
        # self.tiledlayers.RenderStaticAni(surface)
        # self.tiledlayers.RenderBubbles(surface)

        surface.blit(self.resource.surfaces['bg'], (183, 170))

        self.top_menu.draw(surface)
        self.background.set_alpha(self.fade.alpha)
        surface.blit(self.background, (0, 0))


"""
class MainScreen(Screen):
    def __init__(self, game):
        super().__init__(game, FPS)
        self.bg_color = WHITE

        self.car = Car()
        self.thing = Thing()

        self.start()

    def start(self):
        self.car = Car()
        self.thing = Thing()

    def draw(self, window):
        super().draw(window)

        self.thing.move()
        if self.car.collision(self.thing):
            self.car.game_over()

        self.car.draw(window, self.car.x, self.car.y)
        self.thing.draw(window)

        self.dodged(self.thing.count)

        if self.car.state == self.car.STATE_GAME_OVER:
            self.game.state = STATE_GAME_OVER

    def key_event(self, keys):
        if keys[pygame.K_RIGHT]:
            self.car.move(self.car.RIGHT)
        if keys[pygame.K_LEFT]:
            self.car.move(self.car.LEFT)
        if keys[pygame.K_p]:
            self.game.state = STATE_PAUSED

    def dodged(self, count):
        text = self.sys_font.render("Dodged: {}".format(count), True, BLACK)
        self.game.window.blit(text, (0, 0))


class Pause(Screen):
    def __init__(self, game):
        super().__init__(game, 15)
        self.bg_color = None

        button = PauseButton()
        button.action = self.unpause

        self.buttons = [
            button,
        ]

    def draw(self, window):
        super().draw(window)

        pos = WIDTH / 2, HEIGHT / 2
        self.message(self.large_text, "Pause", pos, BLACK)

        for button in self.buttons:
            button.draw(window)

    def unpause(self):
        self.game.state = STATE_RUN


class Crash(Screen):
    def __init__(self, game):
        super().__init__(game, 15)
        self.bg_color = None

    def draw(self, window):
        super().draw(window)

        pos = WIDTH / 2, HEIGHT / 2
        self.message(self.large_text, "Game Over", pos, BLACK)
        pygame.display.update()

    def after(self):
        time.sleep(2)
        self.game.state = STATE_RUN

        self.game.main_screen = MainScreen(self.game)


class TutorialScreen(Screen):
    def __init__(self, game):
        super().__init__(game)
        self.bg_color = BLACK

    def draw(self, window):
        super().draw(window)

        pixels = pygame.PixelArray(window)

        import math
        for t in range(255):
            t1 = t / 20
            x1 = int(50 * math.cos(t1) + 255)
            y1 = int(50 * math.sin(t1) + 255)
            pixels[x1][y1] = (255, 128, 128)

            t2 = t / 10
            x2 = int(100 * math.cos(t2) + 255)
            y2 = int(100 * math.sin(t2) + 255)
            pixels[x2][y2] = (128, 128, 255)

            pygame.draw.line(window, (255, 255, 255), (x1, y1), (x2, y2))

        pixels[10][20] = GREEN
        pixels[10][30] = RED
        pixels[10][40] = BLUE

        pygame.draw.line(window, BLUE, (100, 200), (300, 450), 5)
        pygame.draw.rect(window, RED, (400, 400, 50, 25))
        pygame.draw.circle(window, GREEN, (150, 150), 75)
        pygame.draw.polygon(window, WHITE, ((25, 75), (76, 125), (250, 375)))
"""
