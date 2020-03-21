"""Module for even-odd game."""
from random import randint

rules = "Answer 'yes' if number even otherwise answer 'no'."


def round_data():
    """Code for engine."""
    ask = randint(1, 100)
    print(ask)
    if ask % 2 == 0:
        return 'yes'
    return 'no'
