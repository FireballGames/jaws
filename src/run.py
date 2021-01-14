#!/usr/bin/env python
"""
Used to run game
"""
from jaws import Jaws


def main():
    game = Jaws()
    print("Game intialized")
    game.play()
    print("Game stopped")
    game.stop()


if __name__ == "__main__":
    main()
