import pygame


class Fade:
    def __init__(self, ticks, smooth=False):
        self.ticks = ticks
        self.smooth = smooth

        self.direction = None
        self.ticks_elapsed = 0
        self.finished_in = False
        self.finished_out = False
        self.running = False
        self.alpha = 255
        self.music_fade = False

    def update(self):
        if not self.running:
            return
        if self.direction == 'in' and not self.finished_in:
            self.ticks_elapsed += 1
            if self.ticks_elapsed > self.ticks:
                self.finished_in = True
            else:
                if self.smooth:
                    self.alpha = 255 * (1.0 - (self.ticks_elapsed / float(self.ticks)))
                else:
                    self.alpha = 255 * (1.0 - ((5 * (self.ticks_elapsed / 5)) / float(self.ticks)))
        elif self.direction == 'out' and not self.finished_out:
            self.ticks_elapsed += 1
            if self.ticks_elapsed > self.ticks:
                self.finished_out = True
            else:
                if self.smooth:
                    self.alpha = 255 * (self.ticks_elapsed / float(self.ticks))
                else:
                    self.alpha = 255 * ((5 * (self.ticks_elapsed / 5)) / float(self.ticks))
                if self.music_fade:
                    pygame.mixer.music.set_volume(0.5 * (1.0 - (self.ticks_elapsed / float(self.ticks))))

    def fade_in(self):
        self.direction = 'in'
        self.ticks_elapsed = 0
        self.finished_in = False
        self.finished_out = False
        self.running = True
        self.alpha = 255

    def fade_out(self, music_fade=False):
        self.direction = 'out'
        self.ticks_elapsed = 0
        self.finished_in = False
        self.finished_out = False
        self.running = True
        self.music_fade = music_fade

    def reset(self):
        self.direction = None
        self.ticks_elapsed = 0
        self.finished_in = False
        self.finished_out = False
        self.running = False
        self.alpha = 255
        self.music_fade = False
