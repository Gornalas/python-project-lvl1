"""Module for prime game."""
from random import randint

rules = "Answer 'yes' if given number is prime. Otherwise answer 'no'"


def is_prime(num):
    """Check on prime."""
    check = 2
    while num % check != 0:
        check += 1
    return check == num


def round_data():
    """Code for engine."""
    rand_num = randint(2, 100)
    question = rand_num
    right_answer = is_prime(rand_num)
    if right_answer:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return question, right_answer
