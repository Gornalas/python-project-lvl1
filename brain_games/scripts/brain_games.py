"""Project 1-lvl1."""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from brain_games import cli
from brain_games.scripts import brain_even


def greet(what):
    """First word for console."""
    print('Welcome to the {}!\n'.format(what))


def main():
    """Body of program."""
    greet('Brain Games')
    cli.welcome_user()
    

if __name__ == '__main__':
    main()
