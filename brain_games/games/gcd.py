#!/usr/bin/env python3
"""Module for GCD game."""
# -*- coding: utf-8 -*-
from random import randint

rules = 'Find the greatest common divisor of given numbers.'


def nod(fnum, snum):
    """Find gcd."""
    while fnum != 0 and snum != 0:
        if fnum > snum:
            fnum %= snum
        else:
            snum %= fnum
    return (fnum + snum)


def round_data():
    """Code for engine."""
    first_num = randint(1, 100)
    second_num = randint(1, 100)
    print(str(first_num) + ' ' + str(second_num))
    result = str(nod(first_num, second_num))
    return result
