#!/usr/bin/env python3
"""Module for prime game."""
# -*- coding: utf-8 -*-
from random import randint

rules = "Answer 'yes' if given number is prime. Otherwise answer 'no'"


def result_prime(num):
    """checking on prime."""
    if num <= 3:
        return 'yes'
    for x in range(2, num):
        if num % x == 0:
            return 'no'
    return 'yes'


def round_data():
    """Code for engine."""
    rand_num = randint(2, 100)
    print(rand_num)
    result = result_prime(rand_num)
    return result
