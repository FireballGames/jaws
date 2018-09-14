import pygame


class GameScene:
    def __init__(self, game):
        self.game = game

    def load(self, *args):
        raise NotImplementedError("on_switchto abstract method must be defined in subclass.")

    def update(self):
        raise NotImplementedError("on_update abstract method must be defined in subclass.")

    def event(self, event):
        raise NotImplementedError("on_event abstract method must be defined in subclass.")

    def key_event(self, keys):
        pass

    def mouse_event(self, pos, pressed):
        pass

    def draw(self, surface):
        raise NotImplementedError("on_draw abstract method must be defined in subclass.")


class Screen(GameScene):
    def __init__(self, game):
        super().__init__(game)

        self.bg_color = (0, 0, 0)

        self.sys_font = pygame.font.SysFont(None, 25)
        self.large_text = pygame.font.Font('freesansbold.ttf', 50)

        self.buttons = []

    def message(self, font, text, pos=(0, 0), color=(0, 0, 0)):
        surface = font.render(text, True, color)
        rect = surface.get_rect()
        rect.center = pos
        self.game.window.blit(surface, rect)

    def load(self, *args):
        pass

    def update(self):
        pass

    def event(self, event):
        # Controlling keys
        keys = pygame.key.get_pressed()
        self.key_event(keys)

        self.mouse_event(pygame.mouse.get_pos(), pygame.mouse.get_pressed())

    def key_event(self, keys):
        if keys[pygame.K_ESCAPE]:
            self.game.quit()

    def mouse_event(self, pos, pressed):
        for button in self.buttons:
            button.mouse_event(pos, pressed)

    def draw(self, surface):
        if self.bg_color:
            surface.fill(self.bg_color)
