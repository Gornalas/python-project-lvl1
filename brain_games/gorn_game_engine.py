#!/usr/bin/env python3
"""Game engine."""
# -*- coding: utf-8 -*-
from brain_games import cli
from brain_games.scripts import brain_games

import prompt


def greeting(game):
    """First words."""
    brain_games.main()
    print(game.rules)
    name = cli.welcome_user()
    return name


def main_body(game):
    """Check user's answer."""
    name = greeting(game)
    correct = 3
    while correct:
        result = game.round_data()
        answer = prompt.string('Your answer: ')
        if answer != result:
            print('\n"' + answer + '" is wrong answer ;(. '
            'Correct answer was "' + result + '"')
            print("Let's try again, {}!\n".format(name))
            continue
        print('Correct!')
        correct -= 1
    print('\nCongratulations, {}!'.format(name))
