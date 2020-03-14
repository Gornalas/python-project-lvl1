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
