#!/usr/bin/python

"""
cutscenes.py - scene classes for cutscenes/story
"""

import os
import pygame
from pygame.locals import *

# import pymunk
# from pymunk import Vec2d

from ..fade import Fade
from ..camera import Camera
from ..menu import Menu, MenuItem

from ..resources import Resources
from ..tilemap import TiledLayers
from ..submarine import Submarine


class GameScene:
    def __init__(self, director):
        self.director = director

    def switch_to(self, *options):
        raise NotImplementedError("on_switchto abstract method must be defined in subclass.")

    def event(self, event):
        raise NotImplementedError("on_event abstract method must be defined in subclass.")

    def update(self):
        raise NotImplementedError("on_update abstract method must be defined in subclass.")

    def draw(self, screen):
        raise NotImplementedError("on_draw abstract method must be defined in subclass.")


class SizedScene(GameScene):
    def __init__(self, director, size):
        super().__init__(director)
        self.size = size

        # Background
        self.background = pygame.Surface(self.size)
        self.background.fill((0, 0, 0))
        self.background.convert()


class TitleScreen(SizedScene):
    def __init__(self, director, size):
        super().__init__(director, size)

        self.start_game = False
        self.continue_game = False

        self.save_file = None

        self.camera = None
        self.tiled_layers = None
        self.submarine = None

        self.progress_data = None

        # Controls
        self.button_continue = None
        self.button_newgame = None
        self.buttons = []
        self.top_menu = None
        self.fade = None

    def start_game_now(self):
        self.start_game = True

    def continue_game_now(self):
        self.continue_game = True

    def init_objects(self):
        # Initialise objects
        self.camera = Camera(self.size)
        self.tiled_layers = TiledLayers()
        self.submarine = Submarine()

        # set cross handles
        self.tiled_layers.set_handles((self.camera, self.submarine))
        self.submarine.set_handles((self.camera, self.tiled_layers))

    def init_physics(self):
        # Initialise physics space
        # self.space = pymunk.Space()
        # self.space.gravity = Vec2d(0.0, -450.0)

        # self.submarine.space = self.space
        # self.tiledlayers.space = self.space
        pass

    def load_level(self, level_id):
        # load level data
        self.tiled_layers.load_level(level_id)
        # self.camera.UpdateCamera([int(self.submarine.body.position[0]),-int(self.submarine.body.position[1])])
        self.camera.update([
            int(16 * self.tiled_layers.map_size[0]),
            int(16 * self.tiled_layers.map_size[1])
        ])

    def switch_to(self, *options):
        # Check music
        pygame.mixer.music.load(Resources.musicpaths['pamgaea'])
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

        # top-level menu buttons
        pos_h1 = (self.size[0] / 2) - (Resources.titlescreen_surfs['continue_red'].get_width() / 2)
        pos_h2 = (self.size[0] / 2) - (Resources.titlescreen_surfs['newgame_red'].get_width() / 2)

        if os.path.isfile(self.save_file):
            self.button_continue = MenuItem(
                (pos_h1, 280),
                Resources.titlescreen_surfs['continue_red'],
                Resources.titlescreen_surfs['continue_gold'],
                self.continue_game_now
            )
            self.button_newgame = MenuItem(
                (pos_h2, 320),
                Resources.titlescreen_surfs['newgame_red'],
                Resources.titlescreen_surfs['newgame_gold'],
                self.start_game_now
            )
            self.buttons = [self.button_continue, self.button_newgame]
        else:
            self.button_newgame = MenuItem(
                (pos_h2, 280),
                Resources.titlescreen_surfs['newgame_red'],
                Resources.titlescreen_surfs['newgame_gold'],
                self.start_game_now
            )
            self.buttons = [self.button_newgame]
        self.top_menu = Menu(self.buttons, 0, Resources.controlmap)

        # fade in/out
        self.fade = Fade(30)

        # reset menu
        self.top_menu.selected_index = 0

        # control
        self.start_game = False
        self.continue_game = False

        # run "game"
        level_id = 'level_explore_001'

        self.init_objects()
        self.init_physics()
        self.load_level(level_id)

        # Fade in game
        self.fade.fade_in()

    def update(self):
        # Update Boulders
        self.tiled_layers.UpdateEffects()
        self.tiled_layers.UpdateBoulders()
        self.tiled_layers.UpdateBlocks()

        # Control fade in/out, look for end game cues
        self.fade.update()
        if self.fade.direction == 'in' and (self.start_game or self.continue_game):
            self.fade.fade_out(True)
        if self.fade.finished_out and self.start_game:
            self.progress_data.reset()
            # self.director.change_scene('introcutscene', resources.introcutscene_data)
            self.director.set_scene('maingame', True, "level_explore_001")
        elif self.fade.finished_out and self.continue_game:
            self.progress_data.load()
            self.director.set_scene('maingame', True, self.progress_data.current_level)

    def event(self, events):
        for event in events:
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                self.director.set_scene(None)
            if event.type == KEYDOWN:
                self.top_menu.event(event)

    def draw(self, screen):
        self.tiled_layers.RenderBackdrop(screen)
        self.tiled_layers.RenderTileLayer(screen)
        self.tiled_layers.RenderFishSchools(screen)
        self.tiled_layers.RenderStaticAni(screen)
        self.tiled_layers.RenderBubbles(screen)

        screen.blit(Resources.titlescreen_surfs['bg'], (183, 170))

        self.top_menu.draw(screen)
        self.background.set_alpha(self.fade.alpha)
        screen.blit(self.background, (0, 0))


class CutScene(SizedScene):
    def __init__(self, director, size):
        super().__init__(director, size)

        self.midground = pygame.Surface(self.size)
        self.midground.fill((0, 0, 0))
        self.midground.convert()

        self.fadebackground = pygame.Surface(self.size)
        self.fadebackground.fill((0, 0, 0))
        self.fadebackground.convert()

        self.fade = Fade(30)
        self.fade_text = Fade(15)

        self.go_next = False

        self.sequence = None
        self.music_id = None
        self.next_scene_type = None
        self.next_scene_options = []

        self.step = 0
        self.text_step = -1

        self.ani_to = 0
        self.ani_frame1 = 0
        self.ani_frame2 = 0

    def switch_to(self, sequence, music_id, next_scene_type, next_scene_options, *options):
        self.sequence = sequence  # [ [bgid, [textid1, textid2, ...] ]
        self.music_id = music_id
        self.next_scene_type = next_scene_type
        self.next_scene_options = next_scene_options

        self.step = 0
        self.text_step = -1

        self.ani_to = 0
        self.ani_frame1 = 0
        self.ani_frame2 = 0

        # Check music
        pygame.mixer.music.stop()
        if not self.music_id == 'none':
            pygame.mixer.music.load(Resources.musicpaths[self.music_id])
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(-1)

        self.fade.fade_in()

    def update(self):
        # update animation
        if self.ani_to == 0:
            self.ani_frame1 = (self.ani_frame1 + 1) % 5
            self.ani_frame2 = (self.ani_frame2 + 1) % 2
            self.ani_to = 15
        else:
            self.ani_to -= 1

        # Check for return to game
        self.fade.update()
        self.fade_text.update()

        if self.fade.direction == 'in' and self.fade.finished_in and not self.fade_text.running:
            if len(self.sequence[self.step][1]) > 0:
                self.text_step = 0
                self.fade_text.fade_in()
        if self.go_next:
            if len(self.sequence[self.step][1]) > 0:  # any text?
                if self.fade.direction == 'in' and self.fade_text.direction == 'in' and self.fade_text.running:
                    self.fade_text.fade_out()
            else:
                self.fade.fade_out()
            self.go_next = False
        if self.fade_text.finished_out:  # next text
            self.fade_text.reset()
            self.text_step += 1
            if self.text_step == len(self.sequence[self.step][1]):
                self.text_step = -1
                if self.step == len(self.sequence) - 1:
                    self.fade.fade_out(True)
                else:
                    self.fade.fade_out()
            else:
                self.fade_text.fade_in()
        if self.fade.finished_out:  # next cut
            self.step += 1
            if self.step == len(self.sequence):
                self.director.set_scene(self.next_scene_type, *self.next_scene_options)
            else:
                self.fade.reset()
                self.fade.fade_in()

    def event(self, events):
        for event in events:
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.mixer.music.stop()
                self.director.set_scene(self.next_scene_type, *self.next_scene_options)
            if event.type == KEYDOWN:
                self.go_next = True

    def render_animation(self, screen):
        raise NotImplementedError("render_animation abstract method must be defined in subclass.")

    def render_bg(self, screen):
        bg_data = self.sequence[self.step][0]
        if isinstance(bg_data, list):
            self.render_animation(screen)
            return
        surface = Resources.cutscenesurfs[bg_data]
        pos = ((self.size[0] / 2) - (surface.get_width() / 2), (self.size[1] / 2) - (surface.get_height() / 2))
        screen.blit(surface, pos)

        # check for extra animation render in intro seq
        if len(self.sequence[self.step][1]) > 0:

            if self.sequence[self.step][1][0] == 'introtxt_001':
                tilecoords = Resources.introcutscenespritedata['water'][self.ani_frame1]
                tilecoords2 = list(tilecoords)
                tilecoords2[2] = tilecoords[2] - 7
                screen.blit(Resources.cutscenesurfs['intro_sprites'], (168 - 8, 359 + 4 * 7), tilecoords)
                screen.blit(Resources.cutscenesurfs['intro_sprites'], (168 + 56 - 8, 359 + 4 * 7), tilecoords)
                screen.blit(Resources.cutscenesurfs['intro_sprites'], (168 + 2 * 56 - 8, 359 + 4 * 7), tilecoords2)

                tilecoords = Resources.introcutscenespritedata['man'][self.ani_frame2]
                screen.blit(Resources.cutscenesurfs['intro_sprites'], (166 + 3 * 7 * 8, 359 - 7 * 7), tilecoords)

                tilecoords = Resources.introcutscenespritedata['penguin'][self.ani_frame2]
                screen.blit(Resources.cutscenesurfs['intro_sprites'], (166 - 2 * 7 * 8, 359 - 7 * 7), tilecoords)

            if self.sequence[self.step][1][0] == 'introtxt_005':

                tilecoords = Resources.introcutscenespritedata['sub'][0]
                if self.ani_frame2 == 0:
                    screen.blit(Resources.cutscenesurfs['intro_sprites'], (168 + 7, 359 - 6 * 7), tilecoords)
                else:
                    screen.blit(Resources.cutscenesurfs['intro_sprites'], (168 + 7, 359 - 5 * 7), tilecoords)

                tilecoords = Resources.introcutscenespritedata['water'][self.ani_frame1]
                tilecoords2 = list(tilecoords)
                tilecoords2[2] = tilecoords[2] - 7
                screen.blit(Resources.cutscenesurfs['intro_sprites'], (168 - 8, 359 + 4 * 7), tilecoords)
                screen.blit(Resources.cutscenesurfs['intro_sprites'], (168 + 56 - 8, 359 + 4 * 7), tilecoords)
                screen.blit(Resources.cutscenesurfs['intro_sprites'], (168 + 2 * 56 - 8, 359 + 4 * 7), tilecoords2)

    def render_text(self, screen):
        text_data = self.sequence[self.step][1][self.text_step]
        surface = Resources.cutscenesurfs[text_data]
        # pos = ((self.window_size[0]/2)-(surf.get_width()/2), (self.window_size[1]/2)-(surf.get_height()/2))
        pos = ((self.size[0] / 2) - (surface.get_width() / 2), 20)
        surface.set_alpha(255 - self.fade_text.alpha)
        screen.blit(surface, pos)

    def draw(self, screen):
        screen.blit(self.background, (0, 0))
        self.render_bg(screen)
        if self.text_step >= 0:
            self.render_text(screen)
        self.fadebackground.set_alpha(self.fade.alpha)
        screen.blit(self.fadebackground, (0, 0))
