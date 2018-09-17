import pygame

from game.screen import Screen
from resource.jaws import JawsResources
from resource.cutscenes import CutsceneResource, IntroResource
from controls.fade import Fade


# class CutScene(SizedScene):
class CutScene(Screen):
    def __init__(self, game):
        super().__init__(game)

        self.background = self.panel()
        self.midground = self.panel()
        self.fade_background = self.panel()

        self.fade = Fade(30)
        self.fade_text = Fade(15)

        self.go_next = False

        self.sequence = []
        self.music_id = None
        self.next_scene_type = ""
        self.next_scene_options = []

        self.step = 0
        self.text_step = -1

        self.ani_to = 0
        self.ani_frame1 = 0
        self.ani_frame2 = 0

        self.resource = CutsceneResource()
        self.intro = IntroResource()

    def panel(self):
        panel = pygame.Surface(self.game.size)
        panel.fill((0, 0, 0))
        panel.convert()
        return panel

    def load(self, sequence, music_id, next_scene_type, next_scene_options, *options):
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
        if self.music_id is not None:
            pygame.mixer.music.load(JawsResources.music_paths[self.music_id])
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
                print("Next:", self.next_scene_type, self.next_scene_options)
                self.game.set_scene(self.next_scene_type, *self.next_scene_options)
            else:
                self.fade.reset()
                self.fade.fade_in()

    def event(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.mixer.music.stop()
                self.game.set_scene(self.next_scene_type, *self.next_scene_options)
            if event.type == pygame.KEYDOWN:
                self.go_next = True

    @property
    def current_step(self):
        return self.sequence[self.step]

    @property
    def surfaces(self):
        return self.resource.surfaces

    def render_animation(self, screen):
        raise NotImplementedError("render_animation abstract method must be defined in subclass.")

    def render_bg(self, surface):
        bg_data = self.current_step[0]

        if isinstance(bg_data, list):
            self.render_animation(surface)
            return

        background_surface = self.surfaces[bg_data]
        pos = (
            (self.game.size[0] / 2) - (background_surface.get_width() / 2),
            (self.game.size[1] / 2) - (background_surface.get_height() / 2)
        )
        surface.blit(background_surface, pos)

        # check for extra animation render in intro seq
        if len(self.current_step[1]) > 0:
            if self.current_step[1][0] == 'introtxt_001':

                tile = self.intro.sprites['water'][self.ani_frame1]
                tile_pos = list(tile)
                tile_pos[2] = tile[2] - 7
                surface.blit(self.surfaces['intro_sprites'], (168 - 8, 359 + 4 * 7), tile)
                surface.blit(self.surfaces['intro_sprites'], (168 + 56 - 8, 359 + 4 * 7), tile)
                surface.blit(self.surfaces['intro_sprites'], (168 + 2 * 56 - 8, 359 + 4 * 7), tile_pos)

                tile = self.intro.sprites['man'][self.ani_frame2]
                surface.blit(self.surfaces['intro_sprites'], (166 + 3 * 7 * 8, 359 - 7 * 7), tile)

                tiles = self.intro.sprites['penguin'][self.ani_frame2]
                surface.blit(self.surfaces['intro_sprites'], (166 - 2 * 7 * 8, 359 - 7 * 7), tile)

            if self.current_step[1][0] == 'introtxt_005':
                tile = self.intro.sprites['sub'][0]
                if self.ani_frame2 == 0:
                    surface.blit(self.surfaces['intro_sprites'], (168 + 7, 359 - 6 * 7), tile)
                else:
                    surface.blit(self.surfaces['intro_sprites'], (168 + 7, 359 - 5 * 7), tile)

                tile = self.intro.sprites['water'][self.ani_frame1]
                tile_pos = list(tile)
                tile_pos[2] = tile_pos[2] - 7
                surface.blit(self.surfaces['intro_sprites'], (168 - 8, 359 + 4 * 7), tile)
                surface.blit(self.surfaces['intro_sprites'], (168 + 56 - 8, 359 + 4 * 7), tile)
                surface.blit(self.surfaces['intro_sprites'], (168 + 2 * 56 - 8, 359 + 4 * 7), tile_pos)

    def render_text(self, screen):
        text_data = self.current_step[1][self.text_step]
        surface = self.surfaces[text_data]
        # pos = ((self.window_size[0]/2)-(surf.get_width()/2), (self.window_size[1]/2)-(surf.get_height()/2))
        pos = ((self.game.size[0] / 2) - (surface.get_width() / 2), 20)
        surface.set_alpha(255 - self.fade_text.alpha)
        screen.blit(surface, pos)

    def draw(self, surface):
        # Background
        surface.blit(self.background, (0, 0))
        self.render_bg(surface)

        # Text
        if self.text_step >= 0:
            self.render_text(surface)

        self.fade_background.set_alpha(self.fade.alpha)
        surface.blit(self.fade_background, (0, 0))
