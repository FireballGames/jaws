import pygame


class Fade:
    """Fade control.

    Attributes:
        duration (int): Fade duration
        smooth (bool): Smooth fade
        direction ('in'|'out'): Fade direction
        ticks (int): Ticks to fade
        has_finished (bool): Fade has finished
        is_running (bool): Fade is running
        alpha (int): Alpha level of surface to fade
        music (bool): ...

    """

    FADE_IN = 'in'  #: Direction to fade in
    FADE_OUT = 'out'  #: Direction to fade out

    def __init__(self, ticks, smooth=False):
        """Initialize fade.

        Args:
            ticks (int): Ticks to fade.
            smooth (bool, optional): Smooth fade.

        """
        self.__duration = ticks
        self.__smooth = smooth

        self.direction = None
        self.__ticks = 0
        self.has_finished = False
        self.is_running = False
        self.alpha = 255
        self.__music = False

    def __next_tick(self, direction):
        self.__ticks += 1

        if self.__ticks > self.__duration:
            self.has_finished = True
            return

        if self.__smooth:
            value = self.__ticks
        else:
            value = 5 * (self.__ticks / 5)

        if direction == self.FADE_IN:
            progress = 1.0 - (value / float(self.__duration))
        elif direction == self.FADE_OUT:
            progress = value / float(self.__duration)
        else:
            progress = 0

        self.alpha = 255 * progress
        if self.__music:
            pygame.mixer.music.set_volume(0.5 * progress)

    def update(self):
        """Update fade.

        """

        if not self.is_running:
            return

        if self.has_finished:
            return

        return self.__next_tick(self.direction)

    def fade_in(self, music=False):
        self.direction = self.FADE_IN
        self.__ticks = 0
        self.has_finished = False
        self.is_running = True
        self.alpha = 255
        self.__music = music

    def fade_out(self, music=False):
        self.direction = self.FADE_OUT
        self.__ticks = 0
        self.has_finished = False
        self.is_running = True
        self.alpha = 0
        self.__music = music

    def reset(self):
        self.direction = None
        self.__ticks = 0
        self.__has_finished = False
        self.__is_running = False
        self.__alpha = 255
        self.__music = False
