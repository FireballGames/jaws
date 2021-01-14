class Thought:
    def __init__(self):
        self.current_thought = None

        self.queue = []
        self.to = 0
        self.thought_len = 0

    def reset(self):
        self.queue = []
        self.to = 0
        self.thought_len = 0

    def set_thought(self, thought, to):
        self.current_thought = thought

        self.queue = []  # [i for i in range(len(Resources.thoughtsurfs[thought]))]
        self.thought_len = to
        self.to = to

    def kill(self):
        self.current_thought = 'arrggh'

        self.queue = [0]
        self.thought_len = 45
        self.to = 30
