"""Module for calculate game."""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from brain_games import cli
from brain_games.scripts import brain_games
from random import randint, choice
from operator import add, sub, mul
import prompt


def calc():
	"""Find result of expression"""
	check = 3
	print('What is the result of the expression?\n')
	while check:
		first_num = randint(0,100)
		second_num = randint(0,100)
		operator, symb_operator = choice(((add, "+"), (sub, "-"), (mul, "*")))
		print(str(first_num) + symb_operator + str(second_num))
		user_answer = prompt.integer(prompt = "Your answer: ")
		result = operator(first_num, second_num)
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
	calc()

