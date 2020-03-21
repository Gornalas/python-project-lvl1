#!/usr/bin/env python3
"""Module for calculate game."""
# -*- coding: utf-8 -*-
from random import randint, choice
from operator import add, sub, mul

rules = 'What is the result of the expression?'


def round_data():
    """Code for engine"""
    first_num = randint(0, 100)
    second_num = randint(0, 100)
    operator, symb_operator = choice(((add, '+'), (sub, '-'), (mul, '*')))
    print(str(first_num) + symb_operator + str(second_num))
    result = str(operator(first_num, second_num))
    return result
