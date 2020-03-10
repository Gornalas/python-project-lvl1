"""Module for GCD game."""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from brain_games import cli
from brain_games.scripts import brain_games
from random import randint
import prompt


def nod(fnum, snum):
	while fnum != 0 and snum != 0:
		if fnum > snum:
			fnum %= snum
		else:
			snum %= fnum
	return (fnum + snum)


def gcd():
	"""Find result of expression"""
	check = 3
	print('Find the greatest common divisor of given numbers.\n')
	while check:
		first_num = randint(1,100)
		second_num = randint(1,100)
		print(str(first_num) + " " + str(second_num))
		user_answer = prompt.integer(prompt = "Your answer: ")
		result = nod(first_num, second_num)
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
	gcd()

