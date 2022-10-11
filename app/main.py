class Ship:
    def __init__(self, start: tuple[int], end: tuple[int]) -> None:
        self._count_alive_decks = (end[0] - start[0]) + (end[1] - start[1]) + 1
        self._fired_decks = set()

    def fire(self, row: int, column: int) -> str:
        cell = (row, column)

        if cell in self._fired_decks:
            return "Miss!"

        self._fired_decks.add(cell)
        self._count_alive_decks -= 1
        return {0: "Sunk!"}.get(self._count_alive_decks, "Hit!")

    def deck_alive(self, row: int, column: int) -> bool:
        cell = (row, column)

        if cell in self._fired_decks:
            return False

        return True


class Battleship:
    def __init__(self, ships: list[tuple]) -> None:
        self.field = {}

        for start, end in ships:
            ship = Ship(start, end)

            for coord_x in range(start[1], end[1] + 1):
                self.field[(start[0], coord_x)] = ship

            for coord_y in range(start[0], end[0] + 1):
                self.field[(coord_y, start[1])] = ship

    def fire(self, location: tuple) -> str:
        if location not in self.field:
            return "Miss!"

        return self.field[location].fire(*location)

    def draw_field(self) -> None:
        for i in range(10):
            for j in range(10):
                cell = (i, j)
                if cell in self.field:
                    if self.field[cell].deck_alive(i, j):
                        print("□", end="")
                    else:
                        print("*", end="")
                else:
                    print("~", end="")
            print()
