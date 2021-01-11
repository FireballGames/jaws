import pygame


class Director:
    """Basic class to control screen

    If the class has public attributes, they may be documented here
    in an ``Attributes`` section and follow the same formatting as a
    function's ``Args`` section. Alternatively, attributes may be documented
    inline with the attribute's declaration (see __init__ method below).

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attributes:
        screen(Surface): Screen to control
        clock(Clock): Clock to work with time
        fps(int): Frames per second
        time(int): ???
        framerate(int): ???
        frame(int): ???
        elapsed(int): ???
        __state(int): Current Director's state
        scene: ???
        scenes(dict): ???

    """

    __STATE_QUIT = 0
    __STATE_INTRO = 1
    __STATE_RUN = 2
    __STATE_PAUSED = 3
    __STATE_GAME_OVER = 4

    def __init__(self, screen, fps):
        """Constructor for Director class.

        Initializes Director's attributes.

        Note:
            Do not include the `self` parameter in the ``Args`` section.

        Args:
            screen(Surface): Screen to control
            fps(int): Frames per second

        """
        self.screen = screen

        self.clock = pygame.time.Clock()
        self.fps = fps
        self.time = 0
        self.framerate = 0
        self.frame = 0
        self.elapsed = 0

        self.__state = self.__STATE_INTRO

        self.scene = None
        self.scenes = dict()

    @property
    def is_running(self):
        """bool: If Director is running."""
        return self.__state != self.__STATE_QUIT

    def __update_framerate(self):
        self.time = self.clock.tick(self.fps)
        """
        self.framerate = 1000.0 / self.time
        self.frame += 1
        self.elapsed += self.time
        """

    def __process_events(self):
        # Exit events
        events = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            else:
                events.append(event)

        # Detect events
        self.scene.event(events)

    def __update_scene(self):
        # Update scene
        self.scene.update()

        # Draw the screen
        self.scene.draw(self.screen)

        """
        while self.state == STATE_INTRO:
            self.intro_screen.show()
        while self.state == STATE_RUN:
            self.main_screen.show()
        while self.state == STATE_PAUSED:
            self.pause_screen.show()
        while self.state == STATE_GAME_OVER:
            self.game_over_screen.show()
        """

        """
        b_movie = False
        movie_framerate = 15
        outnumoffset = 0
        if b_movie and self.frame % (self.fps / movie_framerate) == 0:
            filename = "screens/screen_%04d.jpg" % (self.frame / (self.fps / movie_framerate) + outnumoffset)
            pygame.image.save(self.screen, filename)
            # pygame.image.save(self.screen,"screens/screen_%04d.png"%(self.frame/(self.fps/movie_framerate) + outnumoffset))
        """

        pygame.display.update()
        # pygame.display.flip()

    def play(self):
        """Director's main loop.

        Runs main loop while not stopped.

        Processes events, performs actions, updates scene and draws it on the screen.

        """
        while self.is_running:
            self.__update_framerate()
            self.__process_events()
            self.__update_scene()

    def add_scene(self, name, scene):
        """Add scene.

        Args:
            name: Scene name.
            scene: Scene to add.

        """
        self.scenes[name] = scene

    def set_scene(self, name, *options):
        """Load scene.

        If no such scene - quits

        Args:
            name: Name of scene to load.
            options: Scene options.

        """
        scene = self.scenes.get(name)

        if scene is None:
            self.quit()
            return

        self.scene = scene
        self.scene.load(*options)

    def quit(self):
        """Stops main loop.

        """
        self.__state = self.__STATE_QUIT
