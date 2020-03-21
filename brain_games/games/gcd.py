"""Module for GCD game."""
from random import randint

rules = 'Find the greatest common divisor of given numbers.'


def round_data():
    """Code for engine."""
    first_num = randint(1, 100)
    second_num = randint(1, 100)
    print('%s %s' % (first_num, second_num))
    while first_num != 0 and second_num != 0:
        if first_num > second_num:
            first_num %= second_num
        else:
            second_num %= first_num
    return str(first_num + second_num)
