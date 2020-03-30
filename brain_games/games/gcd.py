"""Module for GCD game."""
from random import randint

RULES = 'Find the greatest common divisor of given numbers.'


def round_data():
    """Code for engine."""
    first_num = randint(1, 100)
    second_num = randint(1, 100)
    question = '%s %s' % (first_num, second_num)
    while first_num != 0 and second_num != 0:
        if first_num > second_num:
            first_num %= second_num
        else:
            second_num %= first_num
    right_answer = str(first_num + second_num)
    return question, right_answer
