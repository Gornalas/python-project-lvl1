#!/usr/bin/env python3
"""Module for interface brain-games."""
# -*- coding: utf-8 -*-
import prompt


def welcome_user():
    """Greeting for user."""
    name = prompt.string('May I have your name? ')
    print('Hello, {}!\n'.format(name))
    return name
