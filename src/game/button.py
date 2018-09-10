import pygame


class Button:
    def __init__(self):
        self.color = (0, 0, 0)
        self.hover_color = (0, 0, 0)
        self.rect = (0, 0, 100, 100)

        self.hover = False

        self.font = pygame.font.Font('freesansbold.ttf', 20)
        self.caption = ""
        self.text_color = (0, 0, 0)

    def draw(self, surface):
        pos = (
            self.rect[0] + (self.rect[2] / 2),
            self.rect[1] + (self.rect[3] / 2),
        )

        text_surface = self.font.render(self.caption, True, self.text_color)
        rect = text_surface.get_rect()
        rect.center = pos

        color = self.color
        if self.hover:
            color = self.hover_color
        pygame.draw.rect(surface, color, self.rect)
        surface.blit(text_surface, rect)

    def collide(self, pos):
        if self.rect[0] < pos[0] < self.rect[0] + self.rect[2]:
            if self.rect[1] < pos[1] < self.rect[1] + self.rect[3]:
                return True
        return False

    def action(self):
        pass

    def mouse_event(self, pos, pressed):
        self.hover = self.collide(pos)
        if self.hover and pressed[0]:
            if self.action:
                self.action()
