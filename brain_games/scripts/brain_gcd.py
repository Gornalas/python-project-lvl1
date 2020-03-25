"""Script for gcd game."""
from brain_games import gorn_game_engine
from brain_games.games import gcd


def main():
    """Body of program."""
    gorn_game_engine.run(gcd)


if __name__ == '__main__':
    main()
