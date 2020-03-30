"""Module for even-odd game."""
from random import randint

RULES = "Answer 'yes' if number even otherwise answer 'no'."


def round_data():
    """Code for engine."""
    ask = randint(1, 100)
    question = ask
    right_answer = 'no'
    if ask % 2 == 0:
        right_answer = 'yes'
    return question, right_answer
