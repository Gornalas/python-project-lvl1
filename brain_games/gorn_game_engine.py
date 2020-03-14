"""Game engine."""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from brain_games import cli
from random import randint, choice
from operator import add, sub, mul
import prompt
correct = 3

def check(user_answer, result):
	global correct
	if user_answer == result:
		print('Correct!')
		correct -= 1
	else:
		print("\n" + str(user_answer) + " is wrong answer ;(. Correct answer was " + str(result))
		print("Let's try again, {}!\n".format(cli.name))


def calc():
	global correct
	while correct:
		first_num = randint(0,100)
		second_num = randint(0,100)
		operator, symb_operator = choice(((add, "+"), (sub, "-"), (mul, "*")))
		print(str(first_num) + symb_operator + str(second_num))
		user_answer = prompt.integer(prompt = "Your answer: ")
		result = operator(first_num, second_num)
		check(user_answer, result)
	print("Congratulations, {}!\n".format(cli.name))


def even():
	global correct
	while correct:
		rand_num = randint(0,100)
		print(rand_num)
		user_answer = prompt.string(prompt = "Your answer: ")
		if rand_num % 2 == 0:
			result = 'yes'
		else:
			result = 'no'
		check(user_answer, result)
	print("Congratulations, {}!\n".format(cli.name))


def nod(fnum, snum):
	while fnum != 0 and snum != 0:
		if fnum > snum:
			fnum %= snum
		else:
			snum %= fnum
	return (fnum + snum)


def gcd():
	global correct
	while correct:
		first_num = randint(1,100)
		second_num = randint(1,100)
		print(str(first_num) + " " + str(second_num))
		user_answer = prompt.integer(prompt = "Your answer: ")
		result = nod(first_num, second_num)
		check(user_answer, result)
	print("Congratulations, {}!\n".format(cli.name))


def progression():
	global correct
	while correct:
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
		check(user_answer, result)
	print("Congratulations, {}!\n".format(cli.name))


def result_prime(num):
	if num <= 3:
		return 'yes'
	for x in range(2, num):
		if num % x == 0:
			return 'no'
	return 'yes'


def prime():
	global correct
	while correct:
		rand_num = randint(2,100)
		print(rand_num)
		user_answer = prompt.string('Your answer: ')
		result = result_prime(rand_num)
		check(user_answer, result)
	print("Congratulations, {}!\n".format(cli.name))

