"""Module for even-odd game."""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from brain_games import cli
import random

def even_odd_game():
	"""Check on even-odd."""
	print('Answer "yes" if number even otherwise answer "no".')
	check = 3
	while check:
		rand_num = random.randint(0,100)
		print(rand_num)
		user_answer = int(cli.even_odd())
		if user_answer == (rand_num % 2):
			print('Correct!')
			check -= 1
		elif user_answer == 1:
			print("\n'no' is wrong answer ;(. Correct answer was 'yes'")
			print("Let's try again, {}!\n".format(cli.name))
		elif user_answer == 0:
			print("\n'yes' is wrong answer ;(. Correct answer was 'no'")
			print("Let's try again, {}!\n".format(cli.name))
		else:
			print("\nYou're wrong. You can enter only 'yes' or 'no'")
			print("Let's try again, {}!\n".format(cli.name))
	print("Congratulations, {}!\n".format(cli.name))


def main():
	"""Body of program."""
	cli.welcome_user()
	even_odd_game()
