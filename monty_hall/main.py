import argparse
from dataclasses import dataclass

from monty_hall.game import MontyHallGame
from monty_hall.representation import win, lose


@dataclass
class GameArguments:
    number_doors: int
    number_games: int
    switcheroo: bool


def get_ascii(output: bool):
    if output:
        return win
    return lose


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="MontyHallGame",
        description="Plays the Monty Hall Game",
    )
    parser.add_argument("-d", "--number-doors", default=3, type=int)
    parser.add_argument("-g", "--number-games", type=int, default=1)
    parser.add_argument(
        "-s",
        "--switcheroo",
        type=bool,
        default=False,
        action=argparse.BooleanOptionalAction,
    )
    args = parser.parse_args()

    game_arguments = GameArguments(
        number_doors=args.number_doors,
        number_games=args.number_games,
        switcheroo=args.switcheroo,
    )

    game = MontyHallGame(number_doors=game_arguments.number_doors)

    for _ in range(game_arguments.number_games):
        result = game.play(switcheroo=game_arguments.switcheroo)
        print(get_ascii(output=bool(result)))
