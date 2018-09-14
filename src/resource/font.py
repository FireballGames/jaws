import os
import sys
import pygame

from . import JawsResources


class GameFont:
    keys = list('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ? = abcdefghijklmnopqrstuvwxyz+,-.!"#$%&`():')

    def __init__(self, filename, size):
        self.image = JawsResources.load_image(os.path.join('img', filename))

        self.rects = dict()
        for i in range(8):
            for j in range(10):
                k = self.keys[i * 10 + j]
                self.rects[k] = [j * size[0], i * size[1], size[0], size[1]]
        self.rects['i'][2] = size[1] / 5
        self.rects['l'][2] = size[1] / 5

    def render(self, text, max_x, max_y, align='left'):
        surface = pygame.Surface((max_x, max_y))
        surface.fill((255, 0, 255))
        surface.convert()
        surface.set_colorkey((255, 0, 255))

        text_height = self.rects['A'][3]
        max_lines = max_y / text_height
        line_dist = 0
        line = 0
        offsets = []
        v_offset = 0

        if align in ['centre', 'vcentre']:
            for word in text.split(' '):
                letters = word.split()[0] + ' '
                word_size = sum([self.rects[l][2] for l in letters])
                if word_size > max_x:
                    return False
                if (line_dist + word_size) >= max_x:
                    line += 1
                    offsets.append((max_x - line_dist) / 2)
                    line_dist = 0
                    if line == max_lines:
                        return False
                for let in letters:
                    line_dist += self.rects[let][2]
                if word[-1] == '\n':
                    line += 1
                    offsets.append((max_x - line_dist) / 2)
                    line_dist = 0
            offsets.append((max_x - line_dist) / 2)
            v_offset = max_y / 2 - ((line + 1) * text_height) / 2
            line_dist = 0
            line = 0

        for word in text.split(' '):
            letters = word.split()[0] + ' '
            word_size = sum([self.rects[let][2] for let in letters])
            if word_size > max_x:
                return False
            if (line_dist + word_size) >= max_x:
                line += 1
                line_dist = 0
                if line == max_lines:
                    return False
            for l in letters:
                if align == 'centre':
                    surface.blit(self.image, (line_dist + offsets[line], text_height * line), area=self.rects[l])
                elif align == 'vcentre':
                    surface.blit(self.image, (line_dist + offsets[line], text_height * line + v_offset), area=self.rects[l])
                else:
                    surface.blit(self.image, (line_dist, text_height * line), area=self.rects[l])
                line_dist += self.rects[l][2]
            if word[-1] == '\n':
                line += 1
                line_dist = 0
        return surface


class FontResources(JawsResources):
    gold = None
    gold_small = None
    red = None
    red_small = None
    green = None

    @classmethod
    def load(cls, path, screen_size):
        super().load(path, screen_size)

        # Fonts and text
        cls.gold = GameFont('broddmin_5x10_shad_yellow_2x.png', (10, 20))
        cls.gold_small = GameFont('broddmin_5x10_shad_yellow_1x.png', (5, 10))
        cls.red = GameFont('broddmin_5x10_shad_red_2x.png', (10, 20))
        cls.red_small = GameFont('broddmin_5x10_shad_red_1x.png', (5, 10))
        cls.green = GameFont('broddmin_5x10_shad_green_2x.png', (10, 20))
