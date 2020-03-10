check = 3
while check:
	first_num = randint(0,100)
	second_num = randint(0,100)
	operator, symb_operator = choice(((add, "+"), (sub, "-"), (mul, "*")))
	print(str(first_num) + symb_operator + str(second_num))
	user_answer = prompt.integer(prompt = "Your answer: ")
	result = # computer answer
	if user_answer == result:
		print('Correct!')
		check -= 1
	else:
		print(str(user_answer) + " is wrong answer ;(. Correct answer was " + str(result))
		print("Let's try again, {}!\n".format(cli.name))
print("Congratulations, {}!\n".format(cli.name))
