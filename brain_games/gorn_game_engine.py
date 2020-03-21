"""Game engine."""
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
        correct_answer = game.round_data()
        answer = prompt.string('Your answer: ')
        if answer != correct_answer:
            print('\n"%s" is wrong answer ;(. Correct answer was "%s"' % (answer, correct_answer))
            print("Let's try again, %s!\n" % (name))
            continue
        print('Correct!')
        correct -= 1
    print('\nCongratulations, %s!\n' % (name))
