import pygame

from .game import STATE_QUIT

FPS = 30


class Screen:
    def __init__(self, game, fps=FPS):
        self.game = game

        self.clock = pygame.time.Clock()
        self.fps = fps
        self.bg_color = (0, 0, 0)

        self.sys_font = pygame.font.SysFont(None, 25)
        self.large_text = pygame.font.Font('freesansbold.ttf', 50)

        self.buttons = []

    def after(self):
        pass

    def show(self):
        self.clock.tick(self.fps)

        # Read events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.state = STATE_QUIT
            self.events(event)

        # Controlling keys
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            self.game.state = STATE_QUIT

        self.key_event(keys)
        self.mouse_event(pygame.mouse.get_pos(), pygame.mouse.get_pressed())

        self.draw(self.game.window)

        pygame.display.update()
        # pygame.display.flip()

        self.after()

    def draw(self, window):
        if self.bg_color:
            window.fill(self.bg_color)

    def events(self, event):
        pass

    def key_event(self, keys):
        pass

    def mouse_event(self, pos, pressed):
        for button in self.buttons:
            button.mouse_event(pos, pressed)

    def message(self, font, text, pos=(0, 0), color=(0, 0, 0)):
        surface = font.render(text, True, color)
        rect = surface.get_rect()
        rect.center = pos
        self.game.window.blit(surface, rect)
