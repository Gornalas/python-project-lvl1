"""Module for interface brain-games."""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import prompt


def welcome_user():
    """Greeting for user."""
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
