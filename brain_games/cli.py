"""Module for interface brain-games."""
import prompt


def welcome_user():
    """Greeting for user."""
    name = prompt.string('May I have your name? ')
    print('Hello, %s\n' % (name))
    return name
