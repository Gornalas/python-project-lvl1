#!/usr/bin/env python3
"""Module for even-odd game."""
# -*- coding: utf-8 -*-
import random

rules = "Answer 'yes' if number even otherwise answer 'no'."


def round_data():
    """Code for engine"""
    ask = random.randint(1, 50)
    print (ask)
    result = ''
    if ask % 2 == 0:
        result = 'yes'
    else:
        result = 'no'
    return result
