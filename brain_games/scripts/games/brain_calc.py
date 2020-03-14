"""Module for calculate game."""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from brain_games import gorn_game_engine
from brain_games.scripts import brain_games


def calc():
    """Find result of expression."""
    print('What is the result of the expression?\n')
    gorn_game_engine.calc()


def main():
    """Body of program."""
    brain_games.main()
    calc()
