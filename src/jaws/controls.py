import pygame

LEFT = 0
RIGHT = 1


class Controls:
    def __init__(self, controls):
        self.controls = controls
        self.l = 0
        self.r = 0
        self.u = 0
        self.d = 0
        self.fire = False

    def event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == self.controls["L"]:
                self.l = 1
            elif event.key == self.controls["R"]:
                self.r = 1
            elif event.key == self.controls["U"]:
                self.u = 1
            elif event.key == self.controls["D"]:
                self.d = 1
            elif event.key == self.controls["Fire"]:
                self.fire = True
        elif event.type == pygame.KEYUP:
            if event.key == self.controls["L"]:
                self.l = 0
            elif event.key == self.controls["R"]:
                self.r = 0
            elif event.key == self.controls["U"]:
                self.u = 0
            elif event.key == self.controls["D"]:
                self.d = 0
            elif event.key == self.controls["Fire"]:
                pass
