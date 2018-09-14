class Camera:
    def __init__(self, screen_size, sticky=0.33):
        self.x = -1
        self.y = -1
        self.width, self.height = screen_size
        self.sticky = sticky

        self.x_max = 0
        self.y_max = 0

    def update(self, focus):
        if (focus[0] - self.x) > self.sticky * self.width / 2:
            self.x = focus[0] - self.sticky * self.width / 2
        elif (focus[0] - self.x) < -self.sticky * self.width / 2:
            self.x = focus[0] + self.sticky * self.width / 2
        if (focus[1] - self.y) > self.sticky * self.height / 2:
            self.y = focus[1] - self.sticky * self.height / 2
        elif (focus[1] - self.y) < -self.sticky * self.height / 2:
            self.y = focus[1] + self.sticky * self.height / 2

        if self.x < self.width / 2:
            self.x = self.width / 2
        elif self.x > (self.x_max - self.width / 2):
            self.x = self.x_max - self.width / 2
        if self.y < self.height / 2:
            self.y = self.height / 2
        elif self.y > (self.y_max - self.height / 2):
            self.y = self.y_max - self.height / 2
