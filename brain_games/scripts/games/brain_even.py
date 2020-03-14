"""Module for even-odd game."""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from brain_games import gorn_game_engine
from brain_games.scripts import brain_games


def even_odd_game():
    """Check on even-odd."""
    print('Answer "yes" if number even otherwise answer "no".')
    gorn_game_engine.even()


def main():
    """Body of program."""
    brain_games.main()
    even_odd_game()
