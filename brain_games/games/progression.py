"""Module for progression game."""
from random import randint

rules = 'What number is missing in the progression?'


def round_data():
    """Code for engine."""
    start_num = randint(1, 10)
    step_num = randint(1, 10)
    stop_num = step_num * 10 + start_num
    array = list(range(start_num, stop_num, step_num))
    miss_num = randint(0, 9)
    correct_answer = str(array[miss_num])
    array[miss_num] = '..'
    question = array
    return question, correct_answer
