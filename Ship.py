class Ship:
    """
    Class to represent a ship on the board, represented as
    a collection (set) of cells
    """

    __name: str
    __size: int
    __cells: set[tuple[int, int]]
    __cells_attacked: set[tuple[int, int]]

    __SHIP_TYPES = {
        "carrier": 5,
        "battleship": 4,
        "cruiser": 3,
        "submarine": 3,
        "destroyer": 2,
    }

    def __init__(self, name: str):
        self.__name = name
        self.__size = Ship.__SHIP_TYPES[self.__name.lower()]
        self.__cells = set()
        self.__cells_attacked = set()

    def get_name(self) -> str:
        return self.__name

    def get_size(self) -> int:
        return self.__size

    def get_cells(self) -> set[tuple[int, int]]:
        return self.__cells

    def get_cells_attacked(self) -> set[tuple[int, int]]:
        return self.__cells_attacked

    def add_cell(self, cell: tuple[int, int]):
        self.__cells.add(cell)

    def has_sunk(self) -> bool:
        """
        Determines whether this ship has been sunk
        """
        return len(self.__cells) == 0

    def receive_attack(self, cell: tuple[int, int]) -> bool:
        """
        Removes the incoming cell from this ship's set of cells
        @param cell The cell which was requested to receive the attack
        @returns True if the cell was attacked, false otherwise
        """
        if cell in self.__cells:
            self.__cells.remove(cell)
            self.__cells_attacked.add(cell)
            return True
        return False

    def __str__(self) -> str:
        return "#"

    def __repr__(self) -> str:
        return f"Ship{{{self.__name}, {self.__size}}}"

    def get_cells__for_testing(self) -> set[tuple[int, int]]:
        return self.__cells

    def get_cells_attacked__for_testing(self) -> set[tuple[int, int]]:
        return self.__cells_attacked
