"""Module for calculate game."""
from random import randint, choice
from operator import add, sub, mul

rules = 'What is the result of the expression?'


def round_data():
    """Code for engine."""
    first_num = randint(0, 100)
    second_num = randint(0, 100)
    operator, symb_operator = choice(((add, '+'), (sub, '-'), (mul, '*')))
    print('%s%s%s' % (first_num, symb_operator, second_num))
    return str(operator(first_num, second_num))
