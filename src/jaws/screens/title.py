import os
import pygame

from game.screen import Screen

from controls.menu import Menu, MenuItem
from controls.fade import Fade

from resource.jaws import JawsResources
from resource.cutscenes import TitleResource, IntroResource


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
