"""Script for calculate game."""
from brain_games import gorn_game_engine
from brain_games.games import calc


def main():
    """Body of program."""
    gorn_game_engine.run(calc)


if __name__ == '__main__':
    main()
