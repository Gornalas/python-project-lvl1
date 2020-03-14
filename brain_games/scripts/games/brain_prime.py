"""Module for prime game."""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from brain_games import gorn_game_engine
from brain_games.scripts import brain_games


def prime():
	"""Check on prime."""
	print('Answer "yes" if given number is prime. Otherwise answer "no".')
	gorn_game_engine.prime()


def main():
	"""Body of program."""
	brain_games.main()
	prime()

