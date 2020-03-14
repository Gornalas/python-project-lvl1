"""Module for progression game."""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from brain_games import gorn_game_engine
from brain_games.scripts import brain_games


def progression():
    """Find missing integer."""
    print('What number is missing in the progression?\n')
    gorn_game_engine.progression()


def main():
    """Body of program."""
    brain_games.main()
    progression()
