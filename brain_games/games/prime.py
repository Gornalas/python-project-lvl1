"""Module for prime game."""
from random import randint

rules = "Answer 'yes' if given number is prime. Otherwise answer 'no'"


def round_data():
    """Code for engine."""
    rand_num = randint(2, 100)
    print(rand_num)
    if rand_num <= 3:
        return 'yes'
    for x in range(2, rand_num):
        if rand_num % x == 0:
            return 'no'
    return 'yes'
