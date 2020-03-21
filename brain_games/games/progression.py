#!/usr/bin/env python3
"""Module for progression game."""
# -*- coding: utf-8 -*-

from random import randint

rules = 'What number is missing in the progression?'


def round_data():
    """Code for engine"""
    start_num = randint(1, 10)
    step_num = randint(1, 10)
    stop_num = step_num * 10 + start_num
    array = list(range(start_num, stop_num, step_num))
    miss_num = randint(0, 9)
    result = str(array[miss_num])
    array[miss_num] = '..'
    for index in array:
        print(index, end=' ')
    print()
    return result
