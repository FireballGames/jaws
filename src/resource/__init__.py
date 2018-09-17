import os
import pygame


class Resources:
    path = ""

    music_paths = dict()

    @classmethod
    def load_image(cls, filename="", colorkey=None):
        image = pygame.image.load(os.path.join(cls.path, filename)).convert()
        image.set_colorkey((255, 0, 255))
        return image

    @classmethod
    def add_music(cls, name, filename):
        cls.music_paths[name] = os.path.join(cls.path, filename)

    @classmethod
    def load_font_image(cls, filename=""):
        return cls.load_image(os.path.join('img', 'font', filename))
