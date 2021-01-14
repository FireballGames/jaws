import pygame


class MenuItem:
    MENU_ITEM_INACTIVE = 'INACTIVE'
    MENU_ITEM_ACTIVE = 'ACTIVE'

    def __init__(self, pos, surfaces, action=None):
        self.pos = pos
        self.state = self.MENU_ITEM_INACTIVE
        self.surfaces = surfaces
        self.action = action

    def draw(self, screen):
        screen.blit(self.surfaces[self.state], self.pos)

    def activate(self):
        self.state = self.MENU_ITEM_ACTIVE

    def deactivate(self):
        self.state = self.MENU_ITEM_INACTIVE


class Menu:
    def __init__(self, buttons, selected_index, controls):
        self.buttons = buttons
        self.selected_index = selected_index
        self.buttons[self.selected_index].activate()
        self.controls = controls

    def prev(self):
        self.buttons[self.selected_index].deactivate()
        self.selected_index = (self.selected_index - 1) % len(self.buttons)
        self.buttons[self.selected_index].activate()

    def next(self):
        self.buttons[self.selected_index].deactivate()
        self.selected_index = (self.selected_index + 1) % len(self.buttons)
        self.buttons[self.selected_index].activate()

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
