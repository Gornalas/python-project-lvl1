"""Module for interface brain-games."""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import prompt

name = "Username"


def welcome_user():
    """Greeting for user."""
    global name
    name = prompt.string('May I have your name? ')
    print('Hello, {}!\n'.format(name))


def even_odd():
    """Interface for games even-odd."""
    answer = prompt.string('Your answer: ')
    if answer == 'yes':
        return 0
    elif answer == 'no':
        return 1
    else:
        return 2

