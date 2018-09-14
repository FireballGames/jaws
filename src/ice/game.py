#!/usr/bin/python

"""
game.py - main in-game scene classes
"""


class ProgressData:
    def __init__(self):
        self.current_level = "level_"
        self.filename = ""

    def load(self):
        with open(self.filename, "r") as f:
            self.current_level = f.readline().split()[0]

    def save(self):
        with open(self.filename, "w") as f:
            f.write('{}\n'.format(self.current_level))

    def reset(self):
        self.current_level = "level_"
