"""Module for GCD game."""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from brain_games import gorn_game_engine
from brain_games.scripts import brain_games


def gcd():
    """Find result of expression."""
    print('Find the greatest common divisor of given numbers.\n')
    gorn_game_engine.gcd()


def main():
    """Body of program."""
    brain_games.main()
    gcd()
