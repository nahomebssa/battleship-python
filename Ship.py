class Ship:

    __name: str
    __size: tuple[int, int]
    __cells: set[tuple[int, int]]
    __cells_attacked: set[tuple[int, int]]

    __SHIP_TYPES = {
        "Carrier": 5,
        "Battleship": 4,
        "Cruiser": 3,
        "Submarine": 3,
        "Destroyer": 2,
    }

    def __init__(self, name: str):
        self.__name = name
        self.__size = Ship.__SHIP_TYPES[self.__name]
        self.__cells = set()
        self.__cells_attacked = set()

    
    def get_name(self) -> str:
        return self.__name

    def get_size(self) -> tuple[int, int]:
        return self.__size

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
        @param cell The cell
        @returns True if the cell was attacked, false otherwise
        """
        if cell in self.__cells:
            self.__cells.remove(cell)
            self.__cells_attacked.add(cell)
            return True
        return False
        


