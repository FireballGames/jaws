# from game.states import STATE_QUIT, STATE_RUN


"""
class MainScreen(Screen):
    def __init__(self, game):
        super().__init__(game, FPS)
        self.bg_color = WHITE

        self.car = Car()
        self.thing = Thing()

        self.start()

    def start(self):
        self.car = Car()
        self.thing = Thing()

    def draw(self, window):
        super().draw(window)

        self.thing.move()
        if self.car.collision(self.thing):
            self.car.game_over()

        self.car.draw(window, self.car.x, self.car.y)
        self.thing.draw(window)

        self.dodged(self.thing.count)

        if self.car.state == self.car.STATE_GAME_OVER:
            self.game.state = STATE_GAME_OVER

    def key_event(self, keys):
        if keys[pygame.K_RIGHT]:
            self.car.move(self.car.RIGHT)
        if keys[pygame.K_LEFT]:
            self.car.move(self.car.LEFT)
        if keys[pygame.K_p]:
            self.game.state = STATE_PAUSED

    def dodged(self, count):
        text = self.sys_font.render("Dodged: {}".format(count), True, BLACK)
        self.game.window.blit(text, (0, 0))


class Pause(Screen):
    def __init__(self, game):
        super().__init__(game, 15)
        self.bg_color = None

        button = PauseButton()
        button.action = self.unpause

        self.buttons = [
            button,
        ]

    def draw(self, window):
        super().draw(window)

        pos = WIDTH / 2, HEIGHT / 2
        self.message(self.large_text, "Pause", pos, BLACK)

        for button in self.buttons:
            button.draw(window)

    def unpause(self):
        self.game.state = STATE_RUN


class Crash(Screen):
    def __init__(self, game):
        super().__init__(game, 15)
        self.bg_color = None

    def draw(self, window):
        super().draw(window)

        pos = WIDTH / 2, HEIGHT / 2
        self.message(self.large_text, "Game Over", pos, BLACK)
        pygame.display.update()

    def after(self):
        time.sleep(2)
        self.game.state = STATE_RUN

        self.game.main_screen = MainScreen(self.game)


class TutorialScreen(Screen):
    def __init__(self, game):
        super().__init__(game)
        self.bg_color = BLACK

    def draw(self, window):
        super().draw(window)

        pixels = pygame.PixelArray(window)

        import math
        for t in range(255):
            t1 = t / 20
            x1 = int(50 * math.cos(t1) + 255)
            y1 = int(50 * math.sin(t1) + 255)
            pixels[x1][y1] = (255, 128, 128)

            t2 = t / 10
            x2 = int(100 * math.cos(t2) + 255)
            y2 = int(100 * math.sin(t2) + 255)
            pixels[x2][y2] = (128, 128, 255)

            pygame.draw.line(window, (255, 255, 255), (x1, y1), (x2, y2))

        pixels[10][20] = GREEN
        pixels[10][30] = RED
        pixels[10][40] = BLUE

        pygame.draw.line(window, BLUE, (100, 200), (300, 450), 5)
        pygame.draw.rect(window, RED, (400, 400, 50, 25))
        pygame.draw.circle(window, GREEN, (150, 150), 75)
        pygame.draw.polygon(window, WHITE, ((25, 75), (76, 125), (250, 375)))
"""
