"""Game engine."""
from brain_games import cli
from brain_games.scripts import brain_games

import prompt


def run(game, rounds = 3):
    """Check user's answer."""
    brain_games.main()
    print(game.RULES)
    name = cli.welcome_user()
    while rounds:
        question, correct_answer = game.round_data()
        print(question)
        print()
        answer = prompt.string('Your answer: ')
        if answer != correct_answer:
            print()
            print('"%s" is wrong answer ;(. '
                 'Correct answer was "%s"' % (answer, correct_answer))
            print("Let's try again, %s!" % (name))
            print()
            break
        print('Correct!')
        rounds -= 1
    else:
        print()
        print('Congratulations, %s!' % (name))
