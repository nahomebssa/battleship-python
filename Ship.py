class ShipOrientation:
    
    __orientation: str
    
    def __init__(self, orientation):
        self.__orientation = orientation
    
    def get_orientation(self):
        return self.__orientation
    
    def __str__(self):
        return self.__orientation
    
    def __repr__(self):
        return f"ShipOrientation{{{self.__orientation}}}"

# Static instances of possible orientations
ShipOrientation.VERTICAL = ShipOrientation("vertical")
ShipOrientation.HORIZONTAL = ShipOrientation("horizontal")

class Ship:

    """
    Constructs a ship.
    @param name The name of the ship
    @param size The size of the ship in the format (rows, columns)
    @param start_cell The cell from which to start building the ship
    @param orientation The orientation of the ship, either vertical or horizontal
    @return The constructed ship
    """
    def __init__(self, name: str, size: tuple[int, int], start_cell: tuple[int, int], orientation = ShipOrientation.HORIZONTAL): pass

    
    # Getters and setters

    """
    @returns The name of the ship
    """
    def get_name(self) -> str: pass

    """
    @returns The size of the ship in the format (rows, cols)
    """
    def get_size(self) -> tuple[int, int]: pass
    
    """
    @returns The cell from which the ship starts, in the format (x, y)
    """
    def get_start_cell(self) -> tuple[int, int]: pass

    """
    @returns An instance of the ShipOrientation class, either HORIZONTAL or VERTICAL
    """
    def get_ship_orientation(self) -> ShipOrientation: pass

    """
    @returns A set of all cells which the ship occupies
    """
    def get_cell_locations(self) -> set[tuple[int, int]]: pass



    # Ship methods

    """
    @param cell The cell to check against the ship
    @returns True if the cell lands on the ship, and false if it doesn't
    """
    def cell_falls_on_ship(self, cell: tuple[int, int]) -> bool: pass
    
    """
    Removes the cell from this ship's set of cells
    @param cell The cell
    @returns True if the cell was attacked, false otherwise
    """
    def attack(self, cell: tuple[int, int]): bool

    """
    Detects if the ship was hit
    @returns True if the ship was hit, false otherwise
    """
    def hitDetection(self): bool
