"""Module for calculate game."""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from brain_games import cli
from brain_games.scripts import brain_games
import random


def operator():


def calc():
	"""Find result of expression"""
	rand_first_num = random.randint(0,100)
	rand_second_num = random.randint(0,100)
	rand_operator = random.randint(0,2)
	check = 3
	print('What is the result of the expression?')
	while check:
		
	print("Congratulations, {}!\n".format(cli.name))

def main():
	"""Body of program."""
	brain_games.main()
