import os
import pygame

from .. import Resources
from .fonts import FontResources


class JawsResources(Resources):
    backdrop = None
    tiles = None
    tiles_pos = []

    static_spriteseq = dict()
    fishschool_spriteseq = dict()
    bubbles_spriteseq = dict()
    monster_spriteseq = dict()
    item_spriteseq = dict()
    sub_spriteseq = dict()

    bubbles_spritedata = []
    sub_spritedata = []
    hudtext_spritedata = []
    boulder_spritedata = []
    block_spritedata = []
    harpoon_spritedata = []

    initleveldata = dict()
    soundfx = dict()
    controls = dict()

    thoughtsurfs = dict()
    thoughtto = dict()

    thoughtsurfs_bg = dict()

    pause_spritedata = dict()

    fonts = None


    @classmethod
    def load(cls, path, screen_size):
        cls.path = os.path.abspath(os.path.join(path, "..", "res"))

        print("PATH", path)

        cls.fonts = FontResources(cls)

        # Load background
        cls.backdrop = cls.load_image(os.path.join('img', 'background_2x.png'), (255, 0, 255))

        # sprite rotation angles (used for pre-rendered rotations)
        # angles = [float(i) for i in range(-180, 170, 10)]

        # Load background and tile layer images
        # self.tiles = pygame.image.load(os.path.join(path, 'data', 'gfx', 'tiles_2x.png')).convert()
        # self.tiles.set_colorkey((255, 0, 255))

        # self.tiles_pos = []
        # for j in range(32):
        #     for i in range(16):
        #         self.tiles_pos.append((i * 16, j * 16, 16, 16))

        # Sequences for animated background objects
        # self.static_spriteseq = {}
        # self.static_spriteseq['kelp'] = [37, 38, 39, 38]

        # self.fishschool_spriteseq = {}
        # self.fishschool_spriteseq['normal'] = [96, 98, 100, 102]

        # self.bubbles_spriteseq = {}
        # self.bubbles_spriteseq['normal'] = [82, 83, 84, 85]

        # self.bubbles_spritedata = []
        # for i in range(4):
        #     self.bubbles_spritedata.append(pygame.Surface((16, 16)))
        #     self.bubbles_spritedata[-1].fill((255, 0, 255))
        #     self.bubbles_spritedata[-1].set_colorkey((255, 0, 255))
        #     self.bubbles_spritedata[-1].set_alpha(255)
        #     pos = self.tiles_pos[self.bubbles_spriteseq['normal'][i]]
        #     self.bubbles_spritedata[-1].blit(self.tiles, (0, 0), pos)

        # monster sprites
        # self.monster_spriteseq = {}

        # self.monster_spriteseq['dart'] = [0]
        # self.monster_spriteseq['dartshooter'] = [74, 59]

        # self.monster_spriteseq['squid'] = [88, 90, 92, 94, 124, 126, 156]

        # self.monster_spriteseq['shark'] = {}
        # self.monster_spriteseq['shark']['right'] = [240, 256, 272, 288]
        # self.monster_spriteseq['shark']['left'] = [243, 259, 275, 291]

        # self.monster_spriteseq['roboshark'] = {}
        # self.monster_spriteseq['roboshark']['right'] = [246, 262, 278, 294]
         #self.monster_spriteseq['roboshark']['left'] = [249, 265, 281, 297]

        # Item Sprites
        # self.item_spriteseq = {}
        # self.item_spriteseq['mine'] = [54, 53]
        # self.item_spriteseq['magnet'] = [55]

        # Load player sprites
        # sub_spritesheet_coords = {}
        # sub_spritesheet_coords['left'] = []
        # sub_spritesheet_coords['right'] = []

        # y_offset = 112
        # for j in range(4):
        #     for i in range(2):
        #         sub_spritesheet_coords['right'].append((i * 16 * 3, y_offset + j * 16 * 2, 48, 32))
        #         sub_spritesheet_coords['left'].append((i * 16 * 3 + 16 * 6, y_offset + j * 16 * 2, 48, 32))

        # sub_spritesheet_coords['left'].append((0, y_offset, 24, 32))
        # sub_spritesheet_coords['right'].append((16 * 6, y_offset, 24, 32))

        # sub_spritesheet_coords['left'].append((24, y_offset, 24, 32))
        # sub_spritesheet_coords['right'].append((16 * 6 + 24, y_offset, 24, 32))

        # self.sub_spriteseq = {}
        # self.sub_spriteseq['float'] = [0]
        # self.sub_spriteseq['move'] = [0, 1, 2, 3]
        # self.sub_spriteseq['float_harp'] = [4]
        # self.sub_spriteseq['move_harp'] = [4, 5, 6, 7]
        # self.sub_spriteseq['dead'] = [8, 9]

        # self.sub_spritedata = {}
        # self.sub_spritedata['left'] = []
        # self.sub_spritedata['right'] = []
        # for coords in sub_spritesheet_coords['left']:
        #     self.sub_spritedata['left'].append([])
        #     img = pygame.Surface((coords[2], coords[3]))
        #     img.fill((255, 0, 255))
        #     img.set_colorkey((255, 0, 255))
        #     img.blit(self.tiles, (0, 0), coords)
        #     for ang in angles:
        #         self.sub_spritedata['left'][-1].append(pygame.transform.rotate(img, ang))
        # for coords in sub_spritesheet_coords['right']:
        #     self.sub_spritedata['right'].append([])
        #     img = pygame.Surface((coords[2], coords[3]))
        #     img.fill((255, 0, 255))
        #     img.set_colorkey((255, 0, 255))
        #     img.blit(self.tiles, (0, 0), coords)
        #     for ang in angles:
        #         self.sub_spritedata['right'][-1].append(pygame.transform.rotate(img, ang))

        # Player HUD graphics
        # self.hudtext_spritedata = gamefontgold_small.RenderSentence("structural integrity", 120, 16, align='vcentre')

        # Load boulder and block sprites
        # self.boulder_spritedata = []
        # tile_list = [48, 50, 49]
        # for ti in tile_list:
        #     coords = self.tiles_pos[ti]
        #     self.boulder_spritedata.append([])
        #     img = pygame.Surface((coords[2], coords[3]))
        #     img.fill((255, 0, 255))
        #     img.set_colorkey((255, 0, 255))
        #     img.blit(self.tiles, (0, 0), coords)
        #     for ang in angles:
        #         self.boulder_spritedata[-1].append(pygame.transform.rotate(img, ang))

        # Setup Block Textures
        # blocktexturetiles = [17, 28, 7]
        # self.block_spritedata = []
        # for ti in blocktexturetiles:
        #     coords = self.tiles_pos[ti]
        #     img = pygame.Surface((coords[2], coords[3]))
        #     img.fill((255, 0, 255))
        #     img.set_colorkey((255, 0, 255))
        #     img.blit(self.tiles, (0, 0), coords)
        #     self.block_spritedata.append(img)

        # Setup harpoon sprites
        # self.harpoon_spritedata = []
        # img = pygame.Surface((24, 24))
        # img.fill((255, 0, 255))
        # img.set_colorkey((255, 0, 255))
        # img.blit(self.tiles, (4, 12), (128, 64, 24, 4))
        # for ang in angles:
        #     self.harpoon_spritedata.append(pygame.transform.rotate(img, ang))

        # Load level data
        # self.initleveldata = {}
        # self.initleveldata["level_explore_001"] = InitLevelData(
        #     os.path.join(path, "data", "lvl", "level_explore_001.txt"))
        # self.initleveldata["level_blockages_002"] = InitLevelData(
        #     os.path.join(path, "data", "lvl", "level_blockages_002.txt"))
        # self.initleveldata["level_boulderlift_003"] = InitLevelData(
        #     os.path.join(path, "data", "lvl", "level_boulderlift_003.txt"))
        # self.initleveldata["level_sharksandmines_004"] = InitLevelData(
        #     os.path.join(path, "data", "lvl", "level_sharksandmines_004.txt"))
        # self.initleveldata["level_sharkminetwo_005"] = InitLevelData(
        #     os.path.join(path, "data", "lvl", "level_sharkminetwo_005.txt"))
        # self.initleveldata["level_magnet_006"] = InitLevelData(
        #     os.path.join(path, "data", "lvl", "level_magnet_006.txt"))
        # self.initleveldata["level_lasertunnel_007"] = InitLevelData(
        #     os.path.join(path, "data", "lvl", "level_lasertunnel_007.txt"))
        # self.initleveldata["level_sharkmagnet_008"] = InitLevelData(
        #     os.path.join(path, "data", "lvl", "level_sharkmagnet_008.txt"))

        # Sound Data
        # self.soundfx = {}
        # self.soundfx['subbreak'] = pygame.mixer.Sound(os.path.join(path, 'data', 'snd', 'bigbubblesonwater.ogg'))
        # self.soundfx['mineexplode'] = pygame.mixer.Sound(os.path.join(path, 'data', 'snd', 'clean_explosions.ogg'))

        # self.soundfx['swish'] = pygame.mixer.Sound(os.path.join(path, 'data', 'snd', 'swish.ogg'))
        # self.soundfx['sword_steel'] = pygame.mixer.Sound(os.path.join(path, 'data', 'snd', 'sword_steel.ogg'))
        # self.soundfx['bigthud'] = pygame.mixer.Sound(os.path.join(path, 'data', 'snd', 'bigthud.ogg'))
        # self.soundfx['bodythud'] = pygame.mixer.Sound(os.path.join(path, 'data', 'snd', 'bodythud.ogg'))
        # self.soundfx['laser'] = pygame.mixer.Sound(os.path.join(path, 'data', 'snd', 'laser.ogg'))

        # Music Data
        cls.add_music('wind_effect', os.path.join('music', 'wind_effect.ogg'))
        cls.add_music('dreamy_flashback', os.path.join('music', 'dreamy_flashback.ogg'))
        cls.add_music('pamgaea', os.path.join('music', 'pamgaea.ogg'))
        cls.add_music('deeper', os.path.join('music', 'deeper.ogg'))
        cls.add_music('exotic_battle', os.path.join('music', 'exotic_battle.ogg'))

        # pre-sets and controls
        cls.controls['R'] = pygame.K_RIGHT
        cls.controls['L'] = pygame.K_LEFT
        cls.controls['U'] = pygame.K_UP
        cls.controls['D'] = pygame.K_DOWN
        cls.controls['Fire'] = pygame.K_SPACE

        ####################
        # Though Bubble Data
        # self.thoughtsurfs = {}
        # self.thoughtto = {}

        # self.thoughtsurfs['arrggh'] = [gamefontgold_small.RenderSentence("Arrggh!", 60, 10, align='vcentre')]
        # self.thoughtto['arrggh'] = 45

        """
        # Level 1

        self.thoughtsurfs['lvl001_a'] = [gamefontgold_small.RenderSentence('"here we go ..."', 120, 10, align='vcentre')]
        self.thoughtto['lvl001_a'] = 90

        self.thoughtsurfs['lvl001_b'] = [
            gamefontgold_small.RenderSentence('"... and some loose ice up the top."', 140, 20, align='vcentre'), \
            gamefontgold_small.RenderSentence('"There`s some boulders down there ..."', 140, 20, align='vcentre'), \
            gamefontgold_small.RenderSentence('"I should test out the harpoon (z key)..."', 140, 20, align='vcentre')]
        self.thoughtto['lvl001_b'] = 120

        self.thoughtsurfs['lvl001_c'] = [
            gamefontgold_small.RenderSentence('"There`s so much life down here."', 140, 20, align='vcentre')]
        self.thoughtto['lvl001_c'] = 90

        self.thoughtsurfs['lvl001_d'] = [
            gamefontgold_small.RenderSentence('"A sea cave! I can use that to explore further."', 140, 20, align='vcentre')]
        self.thoughtto['lvl001_d'] = 120

        # Level 2

        self.thoughtsurfs['lvl002_a'] = [
            gamefontgold_small.RenderSentence('"A rockslide. Time to use my harpoon."', 140, 20, align='vcentre')]
        self.thoughtto['lvl002_a'] = 120

        # Level 3

        self.thoughtsurfs['lvl003_a'] = [
            gamefontgold_small.RenderSentence('"That rock looks to heavy for the harpoon."', 140, 20, align='vcentre')]
        self.thoughtto['lvl003_a'] = 120

        self.thoughtsurfs['lvl003_b'] = [gamefontgold_small.RenderSentence('"I need some help."', 140, 20, align='vcentre'), \
                                    gamefontgold_small.RenderSentence('"It`s too heavy to lift on my own."', 140, 20,
                                                                      align='vcentre')]
        self.thoughtto['lvl003_b'] = 120

        # Level 4

        self.thoughtsurfs['lvl004_a'] = [
            gamefontgold_small.RenderSentence("Time for some target practice.", 140, 20, align='vcentre'), \
            gamefontgold_small.RenderSentence("Whoa there! better not run into that ...", 140, 20, align='vcentre')]
        self.thoughtto['lvl004_a'] = 120

        self.thoughtsurfs['lvl004_b'] = [gamefontgold_small.RenderSentence("Eeeek!", 140, 20, align='vcentre')]
        self.thoughtto['lvl004_b'] = 60

        self.thoughtsurfs['lvl004_c'] = [
            gamefontgold_small.RenderSentence("These sharks seem a bit hungry.", 140, 20, align='vcentre')]
        self.thoughtto['lvl004_c'] = 60

        self.thoughtsurfs['lvl004_d'] = [
            gamefontgold_small.RenderSentence("Can`t get too close ... better find another way to get rid of it.", 140, 30,
                                              align='vcentre')]
        self.thoughtto['lvl004_d'] = 120

        self.thoughtsurfs['lvl004_e'] = [
            gamefontgold_small.RenderSentence("If I can harpoon onto the base ..", 140, 20, align='vcentre'), \
            gamefontgold_small.RenderSentence("hmmm ...", 140, 20, align='vcentre')]
        self.thoughtto['lvl004_e'] = 120

        # Level 5

        self.thoughtsurfs['lvl005_a'] = [
            gamefontgold_small.RenderSentence("I need to find something to trigger it.", 140, 20, align='vcentre')]
        self.thoughtto['lvl005_a'] = 120

        # Level 6

        self.thoughtsurfs['lvl006_a'] = [
            gamefontgold_small.RenderSentence("It shouldn`t effect me. Most of the sub is built from carbon fibre.", 140,
                                              30, align='vcentre'), \
            gamefontgold_small.RenderSentence("A giant magnet ... how did this get down here?", 140, 20, align='vcentre')]
        self.thoughtto['lvl006_a'] = 120

        # Level 7

        self.thoughtsurfs['lvl007_a'] = [
            gamefontgold_small.RenderSentence("That boulder`s too big to move.", 140, 20, align='vcentre')]
        self.thoughtto['lvl007_a'] = 120

        self.thoughtsurfs['lvl007_b'] = [gamefontgold_small.RenderSentence("What are those things?", 140, 20, align='vcentre')]
        self.thoughtto['lvl007_b'] = 120

        # Level 8

        self.thoughtsurfs['lvlfinal_a'] = [
            gamefontgold_small.RenderSentence("He doesn`t look friendly.", 140, 20, align='vcentre')]
        self.thoughtto['lvlfinal_a'] = 120

        self.thoughtsurfs['lvlfinal_b'] = [
            gamefontgold_small.RenderSentence("Another magnet ... might be useful somehow.", 140, 20, align='vcentre')]
        self.thoughtto['lvlfinal_b'] = 120

        self.thoughtsurfs['lvlfinal_c'] = [gamefontgold_small.RenderSentence("An underwater base!", 140, 20, align='vcentre')]
        self.thoughtto['lvlfinal_c'] = 120

        self.thoughtsurfs_bg = {}
        bevel_rad = 8
        for key in self.thoughtsurfs.keys():
            self.thoughtsurfs_bg[key] = []
            for i in range(len(self.thoughtsurfs[key])):
                surf = self.thoughtsurfs[key][i]
                if type(surf) == type(True):
                    raise NotImplementedError("Surface render failed for thought: %s, ind: %d" % (key, i))
                (imw, imh) = (surf.get_width(), surf.get_height())
                self.thoughtsurfs_bg[key].append(pygame.Surface((imw + 2 * bevel_rad, imh + 2 * bevel_rad)))
                self.thoughtsurfs_bg[key][-1].fill((255, 0, 255))
                self.thoughtsurfs_bg[key][-1].set_colorkey((255, 0, 255))
                pygame.draw.rect(self.thoughtsurfs_bg[key][-1], (0, 0, 0), ((bevel_rad, bevel_rad), (imw, imh)), 0)
                pygame.draw.rect(self.thoughtsurfs_bg[key][-1], (0, 0, 0), ((bevel_rad, 0), (imw, bevel_rad)), 0)
                pygame.draw.rect(self.thoughtsurfs_bg[key][-1], (0, 0, 0), ((bevel_rad, bevel_rad + imh), (imw, bevel_rad)), 0)
                pygame.draw.rect(self.thoughtsurfs_bg[key][-1], (0, 0, 0), ((0, bevel_rad), (bevel_rad, imh)), 0)
                pygame.draw.rect(self.thoughtsurfs_bg[key][-1], (0, 0, 0), ((bevel_rad + imw, bevel_rad), (bevel_rad, imh)), 0)
                pygame.draw.circle(self.thoughtsurfs_bg[key][-1], (0, 0, 0), (bevel_rad, bevel_rad), bevel_rad, 0)
                pygame.draw.circle(self.thoughtsurfs_bg[key][-1], (0, 0, 0), (bevel_rad + imw, bevel_rad), bevel_rad, 0)
                pygame.draw.circle(self.thoughtsurfs_bg[key][-1], (0, 0, 0), (bevel_rad + imw, bevel_rad + imh), bevel_rad, 0)
                pygame.draw.circle(self.thoughtsurfs_bg[key][-1], (0, 0, 0), (bevel_rad, bevel_rad + imh), bevel_rad, 0)

        """
