from ..font import GameFont


class FontResources:
    gold = None
    gold_small = None
    red = None
    red_small = None
    green = None

    def __init__(self, resources):
        # Fonts and text
        self.gold = GameFont(resources.load_font_image('broddmin_5x10_shad_yellow_2x.png'), (10, 20))
        self.gold_small = GameFont(resources.load_font_image('broddmin_5x10_shad_yellow_1x.png'), (5, 10))
        self.red = GameFont(resources.load_font_image('broddmin_5x10_shad_red_2x.png'), (10, 20))
        self.red_small = GameFont(resources.load_font_image('broddmin_5x10_shad_red_1x.png'), (5, 10))
        self.green = GameFont(resources.load_font_image('broddmin_5x10_shad_green_2x.png'), (10, 20))
