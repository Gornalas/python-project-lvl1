"""Module for prime game."""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from brain_games import cli
from brain_games.scripts import brain_games
from random import randint
import prompt


def result_prime(num):
	if num <= 3:
		return 'yes'
	for x in range(2, num):
		if num % x == 0:
			return 'no'
	return 'yes'


def prime():
	"""Check on prime."""
	print('Answer "yes" if given number is prime. Otherwise answer "no".')
	check = 3
	while check:
		rand_num = randint(2,100)
		print(rand_num)
		user_answer = prompt.string('Your answer: ')
		result = result_prime(rand_num)
		if user_answer == result:
			print('Correct!')
			check -= 1
		else:
			print("\n'" + str(user_answer) + "' is wrong answer ;(. Correct answer was '" + str(result) + "'")
			print("Let's try again, {}!\n".format(cli.name))
	print("Congratulations, {}!\n".format(cli.name))


def main():
	"""Body of program."""
	brain_games.main()
	prime()
