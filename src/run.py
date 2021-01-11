#!/usr/bin/env python
"""
Used to run game
"""
from jaws.jaws import Jaws


def main():
    game = Jaws()
    game.play()
    game.stop()


if __name__ == "__main__":
    main()
