"""Script for even-odd game."""
from brain_games import gorn_game_engine
from brain_games.games import even


def main():
    """Body of program."""
    gorn_game_engine.run(even)


if __name__ == '__main__':
    main()
