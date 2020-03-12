"""Module for progression game."""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from brain_games import cli
from brain_games.scripts import brain_games
from random import randint
import prompt


def progression():
	"""Find missing integer"""
	check = 3
	print('What number is missing in the progression?\n')
	while check:
		start_num = randint(1,10)
		step_num = randint(1,10)
		stop_num = step_num * 10 + start_num
		array = list(range(start_num, stop_num, step_num))
		miss_num = randint(0, 9)
		result = array[miss_num]
		array[miss_num] = ".."

		for index in array:
			print(index, end = ' ')
		print()
		user_answer = prompt.integer(prompt = "Your answer: ")
		if user_answer == result:
			print('Correct!')
			check -= 1
		else:
			print(str(user_answer) + " is wrong answer ;(. Correct answer was " + str(result))
			print("Let's try again, {}!\n".format(cli.name))
	print("Congratulations, {}!\n".format(cli.name))

def main():
	"""Body of program."""
	brain_games.main()
	progression()

