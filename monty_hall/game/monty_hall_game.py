import random


class MontyHallGame:
    def __init__(self, number_doors: int = 3):
        self.number_doors = number_doors

    def play(self, switcheroo: bool = False) -> int:
        available_doors = tuple(range(1, self.number_doors + 1))

        player_door = self._get_random_door()
        prize_door = self._get_random_door()
        goat_door = tuple(
            filter(lambda door: door not in [player_door, prize_door], available_doors)
        )[0]

        if switcheroo:
            player_door = tuple(
                filter(
                    lambda door: door not in [player_door, goat_door], available_doors
                )
            )[0]

        return int(self._win(player_door=player_door, prize_door=prize_door))

    def _get_random_door(self) -> int:
        return random.randint(1, self.number_doors)

    @staticmethod
    def _win(player_door: int, prize_door: int) -> bool:
        if player_door == prize_door:
            return True
        return False
