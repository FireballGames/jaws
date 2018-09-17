"""
class Thing:
    def __init__(self):
        self.x = random.randrange(WIDTH)
        self.y = -600
        self.width = 100
        self.height = 100

        self.speed = 8

        self.color = BLACK

        self.count = 0

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))

    def reset(self):
        self.y = -self.height
        self.x = random.randrange(WIDTH)

    def move(self):
        self.y += self.speed
        if self.y > HEIGHT:
            self.count += 1
            # self.speed += 1
            self.width += (self.count * 1.2)
            self.reset()
"""


"""
class Car:
    LEFT = 0
    RIGHT = 1

    SPEED = 5

    STATE_PLAY = 0
    STATE_GAME_OVER = STATE_GAME_OVER

    def __init__(self):
        self.image = Resource.image('car')
        self.x = WIDTH * .48
        self.y = HEIGHT * .8

        self.width = 73

        self.state = self.STATE_PLAY

    def move(self, direction):
        if direction == self.LEFT:
            self.x -= self.SPEED
        elif direction == self.RIGHT:
            self.x += self.SPEED

    def collision(self, thing):
        if self.x < MIN_X or self.x > MAX_X - self.width:
            return True

        if self.y >= thing.y + thing.height:
            return False
        if self.x + self.width < thing.x:
            return False
        return self.x < thing.x + thing.width

    def draw(self, window, x, y):
        window.blit(self.image, (x, y))

    def game_over(self):
        self.state = self.STATE_GAME_OVER
"""


"""
class GreenButton(Button):
    def __init__(self):
        super().__init__()
        self.rect = (50, HEIGHT - 100, 100, 50)
        self.caption = "GO!"

        self.hover_color = BRIGHT_GREEN
        self.color = GREEN


class RedButton(Button):
    def __init__(self):
        super().__init__()
        self.rect = (WIDTH - 150, HEIGHT - 100, 100, 50)
        self.caption = "Quit"

        self.hover_color = BRIGHT_RED
        self.color = RED


class PauseButton(Button):
    def __init__(self):
        super().__init__()
        self.rect = (50, HEIGHT - 100, 100, 50)
        self.caption = "Continue"

        self.hover_color = BRIGHT_GREEN
        self.color = GREEN
"""
