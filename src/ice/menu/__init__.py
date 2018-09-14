import pygame


class MenuItem:
    def __init__(self, pos, surface_on, surface_off, action=None):
        self.pos = pos
        self.on = False
        self.surface_on = surface_on
        self.surface_off = surface_off
        self.action = action

    def draw(self, screen):
        if self.on:
            screen.blit(self.surface_on, self.pos)
        else:
            screen.blit(self.surface_off, self.pos)


class Menu:
    def __init__(self, buttons, selected_index, controls):
        self.buttons = buttons
        self.selected_index = selected_index
        self.buttons[self.selected_index].on = True
        self.controls = controls

    def prev(self):
        self.buttons[self.selected_index].on = False
        self.selected_index = (self.selected_index - 1) % len(self.buttons)
        self.buttons[self.selected_index].on = True

    def next(self):
        self.buttons[self.selected_index].on = False
        self.selected_index = (self.selected_index + 1) % len(self.buttons)
        self.buttons[self.selected_index].on = True

    def event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == self.controls["U"]:
                self.prev()
            elif event.key == self.controls["D"]:
                self.next()
            if event.key == self.controls["Fire"] or event.key == pygame.K_RETURN:
                self.buttons[self.selected_index].action()

    def draw(self, screen):
        for b in self.buttons:
            b.draw(screen)
