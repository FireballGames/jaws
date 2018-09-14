"""
resources.py - Load all resource data once
"""

import os, sys
import pygame
from pygame.locals import *


class InitLevelData(object):
    def __init__(self, filepath):

        f = open(filepath, "r")
        self.map_size = [int(i) for i in f.readline().split()]  # (w, h)
        self.music = f.readline().split()[0]
        self.player_start_tile = [int(i) for i in f.readline().split()][0]  # tile number for player start
        line = f.readline().split()
        self.finish_tile = [int(line[0]), line[1]]
        self.tilelayer = []
        self.tilelayer_bg = []
        self.tilelayer_fg = []
        self.occlayer = []
        self.effectslayer = []
        self.monsterlayer = []
        self.itemlayer = []
        for j in range(self.map_size[1]):  # read in tile layer
            self.tilelayer.extend([int(i) for i in f.readline().split()])
        for j in range(self.map_size[1]):  # read in tile layer (background)
            self.tilelayer_bg.extend([int(i) for i in f.readline().split()])
        for j in range(self.map_size[1]):  # read in tile layer (foreground)
            self.tilelayer_fg.extend([int(i) for i in f.readline().split()])
        for j in range(self.map_size[1]):  # read in occupancy layer
            self.occlayer.extend([int(i) for i in f.readline().split()])
        for j in range(self.map_size[1]):  # read in effects layer
            self.effectslayer.extend([int(i) for i in f.readline().split()])
        for j in range(self.map_size[1]):  # read in monster layer
            self.monsterlayer.extend([int(i) for i in f.readline().split()])
        for j in range(self.map_size[1]):  # read in item layer
            self.itemlayer.extend([int(i) for i in f.readline().split()])
        self.boulders = []
        num_boulders = [int(i) for i in f.readline().split()][0]  # number of boulders
        for i in range(num_boulders):
            data = [float(i) for i in f.readline().split()]
            self.boulders.append((data[0], data[1], data[2], data[3]))  # (x,y,rad,buoyancy)
        self.blocks = []
        num_blocks = int(f.readline().split()[0])
        for i in range(num_blocks):
            line = f.readline().split()
            self.blocks.append([int(line[0])])
            for j in range(1, len(line)):
                self.blocks[-1].append(float(line[j]))
        self.triggers = []
        num_triggers = int(f.readline().split()[0])
        for i in range(num_triggers):
            line = f.readline().split()
            self.triggers.append([float(line[0]), float(line[1]), float(line[2]), line[3]])
        f.close()


class GameFont(object):
    def __init__(self, mainpath, path, size):
        self.fontim = pygame.image.load(os.path.join(mainpath, 'data', 'gfx', path)).convert()
        self.fontim.set_colorkey((255, 0, 255))

        keys = list('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ? = abcdefghijklmnopqrstuvwxyz+,-.!"#$%&`():')
        self.rects = {}
        for i in range(8):
            for j in range(10):
                k = keys[i * 10 + j]
                self.rects[k] = [j * size[0], i * size[1], size[0], size[1]]
        self.rects['i'][2] = size[1] / 5
        self.rects['l'][2] = size[1] / 5

    def RenderSentence(self, sentence, maxx, maxy, align='left'):
        sentsurf = pygame.Surface((maxx, maxy))
        sentsurf.fill((255, 0, 255))
        sentsurf.convert()
        sentsurf.set_colorkey((255, 0, 255))
        textheight = self.rects['A'][3]
        maxlines = maxy / textheight
        linedist = 0
        line = 0
        offsets = []
        if align in ['centre', 'vcentre']:
            for word in sentence.split(' '):
                letters = word.split()[0] + ' '
                wordsize = sum([self.rects[let][2] for let in letters])
                if wordsize > maxx:
                    return False
                if (linedist + wordsize) >= maxx:
                    line += 1
                    offsets.append((maxx - linedist) / 2)
                    linedist = 0
                    if line == maxlines:
                        return False
                for let in letters:
                    linedist += self.rects[let][2]
                if word[-1] == '\n':
                    line += 1
                    offsets.append((maxx - linedist) / 2)
                    linedist = 0
            offsets.append((maxx - linedist) / 2)
            voffset = maxy / 2 - ((line + 1) * textheight) / 2
            linedist = 0
            line = 0
        for word in sentence.split(' '):
            letters = word.split()[0] + ' '
            wordsize = sum([self.rects[let][2] for let in letters])
            if wordsize > maxx:
                return False
            if (linedist + wordsize) >= maxx:
                line += 1
                linedist = 0
                if line == maxlines:
                    return False
            for let in letters:
                if align == 'centre':
                    sentsurf.blit(self.fontim, (linedist + offsets[line], textheight * line), area=self.rects[let])
                elif align == 'vcentre':
                    sentsurf.blit(self.fontim, (linedist + offsets[line], textheight * line + voffset),
                                  area=self.rects[let])
                else:
                    sentsurf.blit(self.fontim, (linedist, textheight * line), area=self.rects[let])
                linedist += self.rects[let][2]
            if word[-1] == '\n':
                line += 1
                linedist = 0
        return sentsurf


class Resources:
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
    musicpaths = dict()
    controlmap = dict()

    thoughtsurfs = dict()
    thoughtto = dict()

    thoughtsurfs_bg = dict()

    titlescreen_surfs = dict()
    pause_spritedata = dict()

    cutscenesurfs = dict()
    introcutscenespritedata = dict()

    introcutscene_data = []
    cutscene1_data = []
    cutscene2_data = []
    cutscene3_data = []
    cutscene4_data = []
    cutscene5_data = []
    logocutscene_data = []

    def __init__(self, path, screen_size):
        # Load background
        self.backdrop = pygame.image.load(os.path.join(path, 'data', 'gfx', 'background_2x.png')).convert()
        self.backdrop.set_colorkey((255, 0, 255))

        # Fonts and text
        gamefontgold = GameFont(path, 'broddmin_5x10_shad_yellow_2x.png', (10, 20))
        gamefontgold_small = GameFont(path, 'broddmin_5x10_shad_yellow_1x.png', (5, 10))
        gamefontred = GameFont(path, 'broddmin_5x10_shad_red_2x.png', (10, 20))
        gamefontred_small = GameFont(path, 'broddmin_5x10_shad_red_1x.png', (5, 10))
        gamefontgreen = GameFont(path, 'broddmin_5x10_shad_green_2x.png', (10, 20))

        # sprite rotation angles (used for pre-rendered rotations)
        angles = [float(i) for i in range(-180, 170, 10)]

        # Load background and tile layer images
        self.tiles = pygame.image.load(os.path.join(path, 'data', 'gfx', 'tiles_2x.png')).convert()
        self.tiles.set_colorkey((255, 0, 255))

        self.tiles_pos = []
        for j in range(32):
            for i in range(16):
                self.tiles_pos.append((i * 16, j * 16, 16, 16))

        # Sequences for animated background objects
        self.static_spriteseq = {}
        self.static_spriteseq['kelp'] = [37, 38, 39, 38]

        self.fishschool_spriteseq = {}
        self.fishschool_spriteseq['normal'] = [96, 98, 100, 102]

        self.bubbles_spriteseq = {}
        self.bubbles_spriteseq['normal'] = [82, 83, 84, 85]

        self.bubbles_spritedata = []
        for i in range(4):
            self.bubbles_spritedata.append(pygame.Surface((16, 16)))
            self.bubbles_spritedata[-1].fill((255, 0, 255))
            self.bubbles_spritedata[-1].set_colorkey((255, 0, 255))
            self.bubbles_spritedata[-1].set_alpha(255)
            pos = self.tiles_pos[self.bubbles_spriteseq['normal'][i]]
            self.bubbles_spritedata[-1].blit(self.tiles, (0, 0), pos)

        # monster sprites
        self.monster_spriteseq = {}

        self.monster_spriteseq['dart'] = [0]
        self.monster_spriteseq['dartshooter'] = [74, 59]

        self.monster_spriteseq['squid'] = [88, 90, 92, 94, 124, 126, 156]

        self.monster_spriteseq['shark'] = {}
        self.monster_spriteseq['shark']['right'] = [240, 256, 272, 288]
        self.monster_spriteseq['shark']['left'] = [243, 259, 275, 291]

        self.monster_spriteseq['roboshark'] = {}
        self.monster_spriteseq['roboshark']['right'] = [246, 262, 278, 294]
        self.monster_spriteseq['roboshark']['left'] = [249, 265, 281, 297]

        # Item Sprites
        self.item_spriteseq = {}
        self.item_spriteseq['mine'] = [54, 53]
        self.item_spriteseq['magnet'] = [55]

        # Load player sprites
        sub_spritesheet_coords = {}
        sub_spritesheet_coords['left'] = []
        sub_spritesheet_coords['right'] = []

        y_offset = 112
        for j in range(4):
            for i in range(2):
                sub_spritesheet_coords['right'].append((i * 16 * 3, y_offset + j * 16 * 2, 48, 32))
                sub_spritesheet_coords['left'].append((i * 16 * 3 + 16 * 6, y_offset + j * 16 * 2, 48, 32))

        sub_spritesheet_coords['left'].append((0, y_offset, 24, 32))
        sub_spritesheet_coords['right'].append((16 * 6, y_offset, 24, 32))

        sub_spritesheet_coords['left'].append((24, y_offset, 24, 32))
        sub_spritesheet_coords['right'].append((16 * 6 + 24, y_offset, 24, 32))

        self.sub_spriteseq = {}
        self.sub_spriteseq['float'] = [0]
        self.sub_spriteseq['move'] = [0, 1, 2, 3]
        self.sub_spriteseq['float_harp'] = [4]
        self.sub_spriteseq['move_harp'] = [4, 5, 6, 7]
        self.sub_spriteseq['dead'] = [8, 9]

        self.sub_spritedata = {}
        self.sub_spritedata['left'] = []
        self.sub_spritedata['right'] = []
        for coords in sub_spritesheet_coords['left']:
            self.sub_spritedata['left'].append([])
            img = pygame.Surface((coords[2], coords[3]))
            img.fill((255, 0, 255))
            img.set_colorkey((255, 0, 255))
            img.blit(self.tiles, (0, 0), coords)
            for ang in angles:
                self.sub_spritedata['left'][-1].append(pygame.transform.rotate(img, ang))
        for coords in sub_spritesheet_coords['right']:
            self.sub_spritedata['right'].append([])
            img = pygame.Surface((coords[2], coords[3]))
            img.fill((255, 0, 255))
            img.set_colorkey((255, 0, 255))
            img.blit(self.tiles, (0, 0), coords)
            for ang in angles:
                self.sub_spritedata['right'][-1].append(pygame.transform.rotate(img, ang))

        # Player HUD graphics
        self.hudtext_spritedata = gamefontgold_small.RenderSentence("structural integrity", 120, 16, align='vcentre')

        # Load boulder and block sprites
        self.boulder_spritedata = []
        tile_list = [48, 50, 49]
        for ti in tile_list:
            coords = self.tiles_pos[ti]
            self.boulder_spritedata.append([])
            img = pygame.Surface((coords[2], coords[3]))
            img.fill((255, 0, 255))
            img.set_colorkey((255, 0, 255))
            img.blit(self.tiles, (0, 0), coords)
            for ang in angles:
                self.boulder_spritedata[-1].append(pygame.transform.rotate(img, ang))

        # Setup Block Textures
        blocktexturetiles = [17, 28, 7]
        self.block_spritedata = []
        for ti in blocktexturetiles:
            coords = self.tiles_pos[ti]
            img = pygame.Surface((coords[2], coords[3]))
            img.fill((255, 0, 255))
            img.set_colorkey((255, 0, 255))
            img.blit(self.tiles, (0, 0), coords)
            self.block_spritedata.append(img)

        # Setup harpoon sprites
        self.harpoon_spritedata = []
        img = pygame.Surface((24, 24))
        img.fill((255, 0, 255))
        img.set_colorkey((255, 0, 255))
        img.blit(self.tiles, (4, 12), (128, 64, 24, 4))
        for ang in angles:
            self.harpoon_spritedata.append(pygame.transform.rotate(img, ang))

        # Load level data
        self.initleveldata = {}
        self.initleveldata["level_explore_001"] = InitLevelData(
            os.path.join(path, "data", "lvl", "level_explore_001.txt"))
        self.initleveldata["level_blockages_002"] = InitLevelData(
            os.path.join(path, "data", "lvl", "level_blockages_002.txt"))
        self.initleveldata["level_boulderlift_003"] = InitLevelData(
            os.path.join(path, "data", "lvl", "level_boulderlift_003.txt"))
        self.initleveldata["level_sharksandmines_004"] = InitLevelData(
            os.path.join(path, "data", "lvl", "level_sharksandmines_004.txt"))
        self.initleveldata["level_sharkminetwo_005"] = InitLevelData(
            os.path.join(path, "data", "lvl", "level_sharkminetwo_005.txt"))
        self.initleveldata["level_magnet_006"] = InitLevelData(
            os.path.join(path, "data", "lvl", "level_magnet_006.txt"))
        self.initleveldata["level_lasertunnel_007"] = InitLevelData(
            os.path.join(path, "data", "lvl", "level_lasertunnel_007.txt"))
        self.initleveldata["level_sharkmagnet_008"] = InitLevelData(
            os.path.join(path, "data", "lvl", "level_sharkmagnet_008.txt"))

        # Sound Data
        self.soundfx = {}
        self.soundfx['subbreak'] = pygame.mixer.Sound(os.path.join(path, 'data', 'snd', 'bigbubblesonwater.ogg'))
        self.soundfx['mineexplode'] = pygame.mixer.Sound(os.path.join(path, 'data', 'snd', 'clean_explosions.ogg'))

        self.soundfx['swish'] = pygame.mixer.Sound(os.path.join(path, 'data', 'snd', 'swish.ogg'))
        self.soundfx['sword_steel'] = pygame.mixer.Sound(os.path.join(path, 'data', 'snd', 'sword_steel.ogg'))
        self.soundfx['bigthud'] = pygame.mixer.Sound(os.path.join(path, 'data', 'snd', 'bigthud.ogg'))
        self.soundfx['bodythud'] = pygame.mixer.Sound(os.path.join(path, 'data', 'snd', 'bodythud.ogg'))
        self.soundfx['laser'] = pygame.mixer.Sound(os.path.join(path, 'data', 'snd', 'laser.ogg'))

        # Music Data
        self.musicpaths = {}
        self.musicpaths['wind_effect'] = os.path.join(path, 'data', 'music', 'wind_effect.ogg')
        self.musicpaths['dreamy_flashback'] = os.path.join(path, 'data', 'music', 'dreamy_flashback.ogg')
        self.musicpaths['pamgaea'] = os.path.join(path, 'data', 'music', 'pamgaea.ogg')
        self.musicpaths['deeper'] = os.path.join(path, 'data', 'music', 'deeper.ogg')
        self.musicpaths['exotic_battle'] = os.path.join(path, 'data', 'music', 'exotic_battle.ogg')

        # pre-sets and controls
        self.controlmap = {}
        self.controlmap['R'] = K_RIGHT
        self.controlmap['L'] = K_LEFT
        self.controlmap['U'] = K_UP
        self.controlmap['D'] = K_DOWN
        self.controlmap['Fire'] = K_z

        ####################
        # Though Bubble Data
        self.thoughtsurfs = {}
        self.thoughtto = {}

        self.thoughtsurfs['arrggh'] = [gamefontgold_small.RenderSentence("Arrggh!", 60, 10, align='vcentre')]
        self.thoughtto['arrggh'] = 45

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

        ####################
        # Title Screen Stuff

        self.titlescreen_surfs = {}

        self.titlescreen_surfs['bg'] = pygame.image.load(os.path.join(path, 'data', 'gfx', 'titletext.png')).convert()
        self.titlescreen_surfs['bg'].set_colorkey((255, 0, 255))

        self.titlescreen_surfs['newgame_gold'] = gamefontgold.RenderSentence("New Game", screen_size[0], 20, align='vcentre')
        self.titlescreen_surfs['continue_gold'] = gamefontgold.RenderSentence("Continue", screen_size[0], 20, align='vcentre')
        self.titlescreen_surfs['newgame_red'] = gamefontred.RenderSentence("New Game", screen_size[0], 20, align='vcentre')
        self.titlescreen_surfs['continue_red'] = gamefontred.RenderSentence("Continue", screen_size[0], 20, align='vcentre')

        ####################
        # Pause Screen Stuff

        self.pause_spritedata = {}
        self.pause_spritedata['resume_on'] = gamefontred.RenderSentence("Resume Game", 640, 20, align='vcentre')
        self.pause_spritedata['resume_off'] = gamefontgold.RenderSentence("Resume Game", 640, 20, align='vcentre')
        self.pause_spritedata['reset_on'] = gamefontred.RenderSentence("Reset Level", 640, 20, align='vcentre')
        self.pause_spritedata['reset_off'] = gamefontgold.RenderSentence("Reset Level", 640, 20, align='vcentre')
        self.pause_spritedata['quit_on'] = gamefontred.RenderSentence("Quit Game", 640, 20, align='vcentre')
        self.pause_spritedata['quit_off'] = gamefontgold.RenderSentence("Quit Game", 640, 20, align='vcentre')

        for key in self.pause_spritedata.keys():
            surf = self.pause_spritedata[key]
            if type(surf) == type(True):
                raise NotImplementedError("Surface render failed data: %s" % (key))

        ####################
        # Cutscene Stuff

        # Cutscene Surfaces
        self.cutscenesurfs = {}

        # Logo
        self.cutscenesurfs['team_chimera'] = pygame.image.load(
            os.path.join(path, 'data', 'gfx', 'team_chimera_5x.png')).convert()
        self.cutscenesurfs['team_chimera'].set_colorkey((255, 0, 255))

        # Intro cutscenes

        self.cutscenesurfs['intro_backdrop'] = pygame.image.load(
            os.path.join(path, 'data', 'gfx', 'intro_backdrop_7x.png')).convert()
        self.cutscenesurfs['intro_backdrop'].set_colorkey((255, 0, 255))

        self.cutscenesurfs['intro_sprites'] = pygame.image.load(
            os.path.join(path, 'data', 'gfx', 'intro_sprites_7x.png')).convert()
        self.cutscenesurfs['intro_sprites'].set_colorkey((255, 0, 255))

        self.introcutscenespritedata = {}
        self.introcutscenespritedata['water'] = [(7, 7, 56, 56), (63 + 7, 7, 56, 56), (119 + 14, 7, 56, 56),
                                            (175 + 21, 7, 56, 56), (231 + 28, 7, 56, 56)]
        self.introcutscenespritedata['penguin'] = [(77, 70, 56, 63), (77, 140, 56, 63)]
        self.introcutscenespritedata['man'] = [(7, 70, 56, 63), (7, 154, 56, 63)]
        self.introcutscenespritedata['sub'] = [(119 + 21, 63, 126, 98)]

        self.cutscenesurfs['introtxt_001'] = gamefontgold.RenderSentence(
            "For years I had lived upon the glacier, sustaining myself by fishing through a hole in the ice.", 600, 60,
            align='vcentre')
        self.cutscenesurfs['introtxt_002'] = gamefontgold.RenderSentence(
            "The sea below the ice must have been a treasure trove of life, for I had caught many a tasty tuna, scrumptious salmon and heavenly haddock.",
            600, 60, align='vcentre')
        self.cutscenesurfs['introtxt_003'] = gamefontgold.RenderSentence(
            "But fish were not all I caught: on my line I often hauled up strange artifacts and mysterious mechanisms from the icy depths.",
            600, 60, align='vcentre')
        self.cutscenesurfs['introtxt_004'] = gamefontgold.RenderSentence(
            "I pondered over the origins of these strange objects. One day curiosity got the better of me.", 600, 60,
            align='vcentre')

        self.cutscenesurfs['introtxt_005'] = gamefontgold.RenderSentence(
            "I built a submarine that would take me under the ice. I had to get in there and find out where these treasures had come from.",
            600, 60, align='vcentre')
        self.cutscenesurfs['introtxt_006'] = gamefontgold.RenderSentence(
            "Who can say what dangers I might encounter there? If my fate is to be a watery grave, then at least I`ll die knowing.",
            600, 60, align='vcentre')

        # In-between level cutscenes

        # cutscenesurfs['cut1_backdrop'] = pygame.image.load(os.path.join(mainpath,'data','gfx','intro_backdrop_7x.png')).convert()
        self.cutscenesurfs['cut1_backdrop'] = pygame.Surface((640, 480))
        self.cutscenesurfs['cut1_backdrop'].fill((255, 0, 255))
        self.cutscenesurfs['cut1_backdrop'].set_colorkey((255, 0, 255))

        self.cutscenesurfs['cut1_backdrop_sil'] = pygame.image.load(
            os.path.join(path, 'data', 'gfx', 'drfishhead_bg_sil.png')).convert()
        self.cutscenesurfs['cut1_backdrop_sil'].set_colorkey((255, 0, 255))

        self.cutscenesurfs['cut1txt_001'] = gamefontgreen.RenderSentence(
            "Sir! We`ve detected a small vessel approaching the base.", 600, 60, align='vcentre')
        self.cutscenesurfs['cut1txt_002'] = gamefontgreen.RenderSentence("We can`t let him in here.", 600, 60, align='vcentre')
        self.cutscenesurfs['cut1txt_003'] = gamefontgreen.RenderSentence("He`ll discover everything.", 600, 60, align='vcentre')

        self.cutscenesurfs['cut1txt_004'] = gamefontred.RenderSentence(
            "What? Don`t bother me when I`m so close to finishing my work!", 600, 60, align='vcentre')
        self.cutscenesurfs['cut1txt_005'] = gamefontred.RenderSentence(
            "Get out! Deal with the situation, and report back if there`s a real problem.", 600, 60, align='vcentre')

        self.cutscenesurfs['cut2_backdrop'] = pygame.image.load(
            os.path.join(path, 'data', 'gfx', 'drfishhead_bg.png')).convert()
        self.cutscenesurfs['cut2_backdrop'].set_colorkey((255, 0, 255))

        self.cutscenesurfs['cut2txt_001'] = gamefontgreen.RenderSentence(
            "Sir! The vessel is getting closer! He`s almost at the perimeter of the base.", 600, 60, align='vcentre')
        self.cutscenesurfs['cut2txt_002'] = gamefontgreen.RenderSentence("We can`t let him in here.", 600, 60, align='vcentre')
        self.cutscenesurfs['cut2txt_003'] = gamefontgreen.RenderSentence("He`ll find out about project `Justice`.", 600, 60,
                                                                    align='vcentre')

        self.cutscenesurfs['cut2txt_004'] = gamefontred.RenderSentence(
            "So ... society outcasts me because of my hideous fish head and now they send someone to find me?", 600, 60,
            align='vcentre')
        self.cutscenesurfs['cut2txt_005'] = gamefontred.RenderSentence(
            "Never mind, they are too late to stop me! Project `Justice` is almost complete ...", 600, 60, align='vcentre')
        self.cutscenesurfs['cut2txt_006'] = gamefontred.RenderSentence(
            "... and for the world, `Justice` will be served ... Mwuuhahah!", 600, 60, align='vcentre')

        self.cutscenesurfs['cut3txt_001'] = gamefontgreen.RenderSentence("Sir! He`s breached the perimeter!", 600, 60,
                                                                    align='vcentre')
        self.cutscenesurfs['cut3txt_002'] = gamefontgreen.RenderSentence("We can`t let him in here!", 600, 60, align='vcentre')
        self.cutscenesurfs['cut3txt_003'] = gamefontgreen.RenderSentence("He`ll be outside the base in minutes!", 600, 60,
                                                                    align='vcentre')

        self.cutscenesurfs['cut3txt_004'] = gamefontred.RenderSentence(
            "No ... it`s too close to the end now to run away. `Justice` is almost complete.", 600, 60, align='vcentre')
        self.cutscenesurfs['cut3txt_005'] = gamefontred.RenderSentence(
            "When I lived in the world above the waves, I was not good enough for them.", 600, 60, align='vcentre')
        self.cutscenesurfs['cut3txt_006'] = gamefontred.RenderSentence(
            "Everywhere I went ... bars, restaurants, the subway, I was told:", 600, 60, align='vcentre')
        self.cutscenesurfs['cut3txt_007'] = gamefontgold.RenderSentence('"We can`t let you in here!"', 600, 60, align='vcentre')
        self.cutscenesurfs['cut3txt_008'] = gamefontred.RenderSentence("They told me I had fish odour.", 600, 60,
                                                                  align='vcentre')
        self.cutscenesurfs['cut3txt_009'] = gamefontred.RenderSentence(
            "Well now I will prove my worth to them! I`ve come too far to be stopped.", 600, 60, align='vcentre')
        self.cutscenesurfs['cut3txt_010'] = gamefontred.RenderSentence("There`s only one thing left to do ...", 600, 60,
                                                                  align='vcentre')

        self.cutscenesurfs['cut3txt_011'] = gamefontgreen.RenderSentence("Sir! No, not that ... it`s ... it`s too dangerous!",
                                                                    600, 60, align='vcentre')

        self.cutscenesurfs['cut3_backdrop'] = pygame.image.load(
            os.path.join(path, 'data', 'gfx', 'roboshark_bg.png')).convert()
        self.cutscenesurfs['cut3_backdrop'].set_colorkey((255, 0, 255))

        self.cutscenesurfs['cut3txt_012'] = gamefontred.RenderSentence("Silence! Release the Roboshark!", 600, 60,
                                                                  align='vcentre')

        self.cutscenesurfs['cut4_backdrop'] = pygame.image.load(
            os.path.join(path, 'data', 'gfx', 'cutscenefinal.png')).convert()
        self.cutscenesurfs['cut4_backdrop'].set_colorkey((255, 0, 255))

        self.cutscenesurfs['cut4_backdrop2'] = pygame.Surface((640, 480))
        self.cutscenesurfs['cut4_backdrop2'].fill((255, 0, 255))
        self.cutscenesurfs['cut4_backdrop2'].set_colorkey((255, 0, 255))
        self.cutscenesurfs['cut4_backdrop2'].blit(self.backdrop, (0, 0))

        self.cutscenesurfs['cut4txt_001'] = gamefontred.RenderSentence(
            "How did you get in here? You weren`t supposed to come in here!", 600, 60, align='vcentre')
        self.cutscenesurfs['cut4txt_002'] = gamefontred.RenderSentence("My secrets ... all ruined ... project `Justice` ...",
                                                                  600, 60, align='vcentre')
        self.cutscenesurfs['cut4txt_003'] = gamefontgold.RenderSentence("Wow! this is amazing! You mean you live down here?",
                                                                   600, 60, align='vcentre')
        self.cutscenesurfs['cut4txt_004'] = gamefontred.RenderSentence("Ahh ... yes I do ...", 600, 60, align='vcentre')
        self.cutscenesurfs['cut4txt_005'] = gamefontgold.RenderSentence(
            "I`ve never seen anything so cool. I mean, an underwater base is about as cool as it gets.", 600, 60,
            align='vcentre')
        self.cutscenesurfs['cut4txt_006'] = gamefontred.RenderSentence(
            "Well, yes ... hold on! You mean you`re not here to steal my secret recipe?", 600, 60, align='vcentre')
        self.cutscenesurfs['cut4txt_007'] = gamefontgold.RenderSentence("Ahhh, nope.", 600, 60, align='vcentre')
        self.cutscenesurfs['cut4txt_008'] = gamefontred.RenderSentence(
            "Then project `Justice` is safe! At last the world will taste my delicious oyster sauce.", 600, 60,
            align='vcentre')
        self.cutscenesurfs['cut4txt_009'] = gamefontred.RenderSentence(
            "I`ve been working down here on the perfect recipe for months. I`m going to call my delicous oyster sauce `Justice` and serve it to the whole world.",
            600, 60, align='vcentre')
        self.cutscenesurfs['cut4txt_010'] = gamefontred.RenderSentence(
            "I wanted to show the world that my culinary talents can make up for my hideous personal appearence.", 600, 60,
            align='vcentre')
        self.cutscenesurfs['cut4txt_011'] = gamefontgold.RenderSentence("What do you mean?", 600, 60, align='vcentre')
        self.cutscenesurfs['cut4txt_012'] = gamefontred.RenderSentence(
            "My hideous appearance. I have the body of a man and the head of a fish. Haven`t you noticed?", 600, 60,
            align='vcentre')
        self.cutscenesurfs['cut4txt_013'] = gamefontgold.RenderSentence(
            "Ah, no, I didn`t really see that ... now that you mention it ...", 600, 60, align='vcentre')
        self.cutscenesurfs['cut4txt_014'] = gamefontred.RenderSentence("Would you like to try some `Justice`?", 600, 60,
                                                                  align='vcentre')
        self.cutscenesurfs['cut4txt_015'] = gamefontgold.RenderSentence(
            "Sure, that would be great. I`ve got a couple of pounds of squid that I picked up on the way here. I`m starved!",
            600, 60, align='vcentre')

        self.cutscenesurfs['cut4txt_016'] = gamefontgold.RenderSentence(
            "Congratulations! Game Complete! Best Friends Forever ...", 600, 60, align='vcentre')

        for key in self.cutscenesurfs.keys():
            surf = self.cutscenesurfs[key]
            if type(surf) == type(True):
                raise NotImplementedError("Surface render failed cutscene data: %s" % (key))

        ###########################
        # Actual cutscene content

        # introcutscene_data = [[ ['intro_backdrop',['introtxt_001']] ],'none','titlescene',[]]
        # introcutscene_data = [[ ['intro_backdrop',['introtxt_001','introtxt_002','introtxt_003','introtxt_004']], \
        #    ['intro_backdrop',['introtxt_005','introtxt_006']]],'wind_effect','maingame',[True,"level_explore_001"]]

        self.introcutscene_data = [[['intro_backdrop', ['introtxt_001', 'introtxt_002', 'introtxt_003', 'introtxt_004']], \
                               ['intro_backdrop', ['introtxt_005', 'introtxt_006']]], 'wind_effect', 'titlescene', []]

        self.cutscene1_data = [[['cut1_backdrop', ['cut1txt_001', 'cut1txt_002', 'cut1txt_003']], \
                           ['cut1_backdrop_sil', ['cut1txt_004', 'cut1txt_005']]], 'none', 'maingame',
                          [True, "level_sharksandmines_004"]]

        self.cutscene2_data = [[['cut1_backdrop', ['cut2txt_001', 'cut2txt_002', 'cut2txt_003']], \
                           ['cut2_backdrop', ['cut2txt_004', 'cut2txt_005', 'cut2txt_006']]], 'none', 'maingame',
                          [True, "level_magnet_006"]]

        self.cutscene3_data = [[['cut1_backdrop', ['cut3txt_001', 'cut3txt_002', 'cut3txt_003']], \
                           ['cut2_backdrop',
                            ['cut3txt_004', 'cut3txt_005', 'cut3txt_006', 'cut3txt_007', 'cut3txt_008', 'cut3txt_009',
                             'cut3txt_010', 'cut3txt_011']], \
                           ['cut3_backdrop', ['cut3txt_012']]], 'none', 'maingame', [True, "level_sharkmagnet_008"]]

        self.cutscene5_data = [[['cut4_backdrop2', ['cut4txt_016']]], 'pamgaea', 'titlescene', []]

        self.cutscene4_data = [[['cut4_backdrop',
                            ['cut4txt_001', 'cut4txt_002', 'cut4txt_003', 'cut4txt_004', 'cut4txt_005', 'cut4txt_006',
                             'cut4txt_007', 'cut4txt_008', 'cut4txt_009', 'cut4txt_010', 'cut4txt_011', 'cut4txt_012',
                             'cut4txt_013', 'cut4txt_014', 'cut4txt_015']]], 'none', 'cutscene5', self.cutscene5_data]

        # logocutscene_data = [[ ['team_chimera',[]] ],'none','titlescene',[]]
        # logocutscene_data = [[ ['team_chimera',[]] ],'none','maingame',[True,"level_explore_001"]]
        self.logocutscene_data = [[['team_chimera', []]], 'none', 'introcutscene', self.introcutscene_data]
