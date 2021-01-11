import pygame

from .cutscenes import SizedScene
from ..fade import Fade
from ..game import ProgressData
from ..camera import Camera
from ..resources import Resources
from ..menu import Menu, MenuItem

from ..tilemap import TiledLayers
from ..submarine import Submarine


class MainGame(SizedScene):
    def __init__(self, director, size):
        super().__init__(director, size)

        # frame rate recording
        self.avg_framerate = -1
        self.fr_samples = 0

        # fade in/out
        self.fade = Fade(15)

        # Music
        self.current_music = 'none'

        # Initialise player data
        self.progress_data = ProgressData()

        self.camera = None
        self.tiled_layers = None
        self.submarine = None

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

        # collision types:
        # 1: harpoon (on hook)
        # 2: harpoon (loose)
        # 3: player
        # 4: dart
        # 5: shark
        # 6: mine
        # 7: roboshark
        # 8: squid
        # 9: dead squid

        # self.space.add_collision_handler(0, 1, post_solve=submarine.harpoon_hit_func)  # harpoon generics
        # self.space.add_collision_handler(0, 2, post_solve=submarine.looseharpoon_hit_func)
        # self.space.add_collision_handler(9, 1, post_solve=submarine.harpoon_hit_func)  # harpoon generics
        # self.space.add_collision_handler(9, 2, post_solve=submarine.looseharpoon_hit_func)

        # self.space.add_collision_handler(0, 4, post_solve=monsters.dart_hit_func)  # darts
        # self.space.add_collision_handler(9, 4, post_solve=monsters.dart_hit_func)
        # self.space.add_collision_handler(3, 4, post_solve=monsters.dart_hit_player_func)

        # self.space.add_collision_handler(3, 5, post_solve=monsters.shark_bite_player_func)  # shark bite
        # self.space.add_collision_handler(0, 5, post_solve=monsters.shark_bite_thing_func)  # shark bite

        # self.space.add_collision_handler(5, 1, post_solve=submarine.harpoon_hit_monster)  # harpoon hit monster
        # self.space.add_collision_handler(5, 2, post_solve=submarine.harpoon_hit_monster)  # harpoon hit monster
        # self.space.add_collision_handler(8, 1, post_solve=submarine.harpoon_hit_monster)  # harpoon hit monster
        # self.space.add_collision_handler(8, 2, post_solve=submarine.harpoon_hit_monster)  # harpoon hit monster

        # mine contact
        # self.space.add_collision_handler(0, 6, post_solve=tilemap.mine_contact_func)
        # self.space.add_collision_handler(1, 6, post_solve=tilemap.mine_contact_func)
        # self.space.add_collision_handler(2, 6, post_solve=tilemap.mine_contact_func)
        # self.space.add_collision_handler(3, 6, post_solve=tilemap.mine_contact_func)
        # self.space.add_collision_handler(4, 6, post_solve=tilemap.mine_contact_func)
        # self.space.add_collision_handler(5, 6, post_solve=tilemap.mine_contact_func)
        # self.space.add_collision_handler(7, 6, post_solve=tilemap.mine_contact_func)
        # self.space.add_collision_handler(8, 6, post_solve=tilemap.mine_contact_func)
        # self.space.add_collision_handler(9, 6, post_solve=tilemap.mine_contact_func)

        # self.submarine.space = self.space
        # self.tiledlayers.space = self.space
        pass

    def switch_to(self, level_reset, level_id, *options):
        if not level_reset:
            return

        # Save progress
        self.progress_data.current_level = level_id
        self.progress_data.save()

        self.init_objects()
        self.init_physics()

        # load level data
        self.tiled_layers.load_level(level_id)
        # self.camera.UpdateCamera([int(self.submarine.body.position[0]), -int(self.submarine.body.position[1])])
        self.camera.update([0, 0])

        # Check music
        if not self.current_music == Resources.initleveldata[level_id].music:
            self.current_music = Resources.initleveldata[level_id].music
            pygame.mixer.music.stop()
            if not self.current_music == 'none':
                pygame.mixer.music.load(Resources.musicpaths[self.current_music])
                pygame.mixer.music.set_volume(0.5)
                pygame.mixer.music.play(-1)

        # Fade in game
        self.background.fill((0, 0, 0))
        self.fade.fade_in()

        # self.submarine.SetThought("sub_plastic",120)

    def update(self):
        # frame rate tracking
        self.fr_samples += 1
        if self.fr_samples == 1:
            self.avg_framerate = self.director.framerate
        else:
            self.avg_framerate = self.avg_framerate + (self.director.framerate - self.avg_framerate) / (self.fr_samples)

        # Update player motion
        self.submarine.Update()
        # self.camera.UpdateCamera([int(self.submarine.body.position[0]), -int(self.submarine.body.position[1])])
        self.camera.update([0, 0])

        # Update Boulders
        self.tiled_layers.UpdateEffects()
        self.tiled_layers.UpdateBoulders()
        self.tiled_layers.UpdateBlocks()

        # Update all Monsters
        self.tiled_layers.UpdateMonsters()

        # Update All items
        self.tiled_layers.UpdateItems()

        # Update Triggers
        self.tiled_layers.UpdateTriggers()

        # Update space
        # self.space.step(1.0 / 120)
        # self.space.step(1.0 / 120)
        # self.space.step(1.0 / 120)
        # self.space.step(1.0 / 120)

        # Post update steps
        if self.submarine.alive:
            self.submarine.PostUpdate()

        # Control fade in/out, look for end game cues
        self.fade.update()
        if self.tiled_layers.exiting and self.fade.direction == self.fade.FADE_IN:
            if not self.current_music == Resources.initleveldata[self.tiled_layers.destination].music:
                music_fade = True
            else:
                music_fade = False
            self.fade.fade_out(music_fade)
        if self.submarine.death_to == 0 and self.fade.direction == self.fade.FADE_IN:
            self.fade.fade_out()
        if self.fade.has_finished:
            if self.submarine.death_to == 0:
                self.director.set_scene('maingame', True, self.tiled_layers.level_id)
            else:
                if self.tiled_layers.level_id == 'level_boulderlift_003':
                    self.director.set_scene('cutscene1', *Resources.cutscene1_data)
                elif self.tiled_layers.level_id == 'level_sharkminetwo_005':
                    self.director.set_scene('cutscene2', *Resources.cutscene2_data)
                elif self.tiled_layers.level_id == 'level_lasertunnel_007':
                    self.director.set_scene('cutscene3', *Resources.cutscene3_data)
                elif self.tiled_layers.level_id == 'level_sharkmagnet_008':
                    self.director.set_scene('cutscene4', *Resources.cutscene4_data)
                else:
                    self.director.set_scene('maingame', True, self.tiled_layers.destination)

    def event(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                # self.director.change_scene(None, [])
                self.draw(self.h_pausescene.background)
                self.director.set_scene('pausescene', self.tiled_layers.level_id)
            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                self.submarine.control.ProcessKeyEvent(event)

    def do_draw(self, screen):
        self.tiled_layers.RenderBackdrop(screen)
        self.tiled_layers.RenderTileLayer(screen)
        self.tiled_layers.RenderBlocks(screen)
        self.tiled_layers.RenderBoulders(screen)
        self.tiled_layers.RenderFishSchools(screen)
        self.tiled_layers.RenderItems(screen)
        self.tiled_layers.RenderMonsters(screen)
        self.submarine.harpoon.Draw(screen)
        self.submarine.Draw(screen)
        self.tiled_layers.RenderFGLayer(screen)
        self.tiled_layers.RenderStaticAni(screen)
        self.tiled_layers.RenderBubbles(screen)
        self.submarine.RenderHUD(screen)
        self.submarine.RenderThought(screen)

    def draw(self, screen):
        self.do_draw(screen)
        self.background.set_alpha(self.fade.alpha)
        screen.blit(self.background, (0, 0))


class PauseScreen(SizedScene):
    def __init__(self, director, size):
        super().__init__(director, size)

        self.from_level = None

        self.pos_v = 0
        self.button_resume = None
        self.button_reset = None
        self.button_quit = None
        self.buttons = []
        self.top_menu = None

    def resume_game_now(self):
        self.director.set_scene('maingame', False, -1)

    def reset_game_now(self):
        self.director.set_scene('maingame', True, self.from_level)

    def quit_game_now(self):
        self.h_maingame.current_music = 'none'
        self.director.set_scene('titlescene')
        # self.director.change_scene('logocutscene', resources.logocutscene_data)

    def switch_to(self, from_level, *options):
        self.from_level = from_level

        # Setup background
        backfade = pygame.Surface(self.background.get_size())
        backfade.fill((0, 0, 0))
        backfade.convert()
        backfade.set_alpha(128)
        self.background.blit(backfade, (0, 0))

        # top-level menu buttons
        # self.pos_h = (self.window_size[0]/2)-((resources.pausescreen_surfs['bg'].get_width()+resources.pausescreen_surfs['help'].get_width()+40)/2)
        # self.pos_h2 = self.pos_h + resources.pausescreen_surfs['bg'].get_width() + 40
        # self.pos_v = (self.window_size[1]/2)-(resources.pausescreen_surfs['bg'].get_height()/2)
        # self.pos_v2 = (self.window_size[1]/2)-(resources.pausescreen_surfs['help'].get_height()/2)
        self.pos_v = 200
        self.button_resume = MenuItem(
            (0, self.pos_v),
            Resources.pause_spritedata['resume_on'],
            Resources.pause_spritedata['resume_off'],
            self.resume_game_now
        )
        self.button_reset = MenuItem(
            (0, self.pos_v + 32),
            Resources.pause_spritedata['reset_on'],
            Resources.pause_spritedata['reset_off'],
            self.reset_game_now
        )
        self.button_quit = MenuItem(
            (0, self.pos_v + 64),
            Resources.pause_spritedata['quit_on'],
            Resources.pause_spritedata['quit_off'],
            self.quit_game_now
        )
        self.buttons = [self.button_resume, self.button_reset, self.button_quit]
        self.top_menu = Menu(self.buttons, 0, Resources.controlmap)

        # reset menu
        self.top_menu.select_ind = 0

    def update(self):
        pass

    def event(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.director.set_scene('maingame', False, -1)
            if event.type == pygame.KEYDOWN:
                self.top_menu.event(event)

    def draw(self, screen):
        screen.blit(self.background, (0, 0))
        self.top_menu.draw(screen)
