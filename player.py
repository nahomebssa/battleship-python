from Ship import Ship
from Board import Board


class Player: 
    '''
    This class defines a player who will play the game against another player. This class is able to add ships to the board.
    To ensure that ship position is hidden, we only store the ship coordinates and refer to them.
    Furthermore, we can remove a specific ship if the player wants to.
    This class will also enable us to know if a certain player has won the game.
    '''

    # Added the self.player_board.build_game_board() to build the board
    # Changed board name to "player_board" instead of "board" to avoid confusion with Board class.
    def __init__(self, playerName) -> None:
        self.playerName = playerName
        self.ships_location = []
        self.player_board = Board()
        self.player_board.build_game_board()

    
    def get_ship_config(self) -> tuple[int, int, str]:
        """
        Returns a ship config, which is a 3-tuple of the starting row, col, and orientation
        @returns 3-tuple of ship config
        """
        start_row = None
        start_col = None
        orientation = None

        while True:
            try:
                start_row = int(input("Please enter starting row (0-9): "))
                start_col = int(input("Please enter starting column (0-9): "))
                orientation = input("Please enter 'v' for verically orientation or 'h' for horizontal orientation: ")
                
                # Checks if all user inputs are valid
                if start_row not in range(10) or start_col not in range(10) or orientation not in ['v', 'h']:
                    print("Invalid input. Please ensure starting coordinates or orientation are correct. Try again ")

            except ValueError:
                print("Oops, please enter a valid integer! Try again!")
            
            else:
                break   # break out of the while loop


        return (start_row, start_col, orientation)
            
    def validate_ship_config(self, ship_config: tuple[int, int, str], ship_size: int) -> bool:
        """
        Checks the ship_config is not out of bounds
        @returns True if the ship is not out of bounds, false otherwise
        """
        start_row, start_col, orientation = ship_config
        if orientation == 'v':
            return (start_row + ship_size) in range(10)
        elif orientation == 'h':
            return (start_col + ship_size) in range(10)
        pass

    def make_cells(self, ship_config: tuple[int, int, str], ship_size: int):
        """
        Create a set of cells that will potentially be added to a ship
        """
        start_row, start_col, orientation = ship_config
        cells: set[tuple[int, int]] = set()
        
        if orientation == 'v':
            for pos in range(ship_size):
                cells.add((start_row + pos, start_col))
        
        elif orientation == 'h':
            for pos in range(ship_size):
                cells.add((start_row, start_col + pos))
            
        return cells


    def place_cell_on_board(self, cell: tuple[int, int]):
        """
        Places a cell on the board, using the Board instance
        """
        x, y = cell
        self.player_board.board[x][y] = "O"

    def add_ship(self) -> None:
        '''
        Since there are 5 ships to add, this method iterates through the five options 
        changing their cell based on where the user wanted the starting coordinate in relation to 
        the orientation.
        '''

        # Created this list to handle putting ships on the board automatically.
        available_ships = ["Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer"]

        # keep track of cells on the board
        placed_cells = set()
        

        # self.player_board.show_board()

        # The for loop below uses the ships in the available_ships to place them without user being asked for name.
        for ship_name in available_ships:
            
            self.player_board.show_board()

            ship = Ship(ship_name)
            self.ships_location.append(ship)
            
            print(f"Place Ship: {ship_name}, Size: {ship.get_size()}")

            # starting row and column, and orientation
            ship_config: tuple[int, int, str] = self.get_ship_config()
            
            # make sure the ship_config is valid, aka
            # the ship fits on the board
            while not self.validate_ship_config(ship_config, ship.get_size()):
                print("ship will be built out of bounds, try again")
                ship_config = self.get_ship_config()

            # get the cells this ship will occupy
            cells: set[tuple[int, int]] = self.make_cells(ship_config, ship.get_size())

            while len(placed_cells.intersection(cells)) > 0:

                print("**collision detected**!")
                print("Please choose another starting coordinate: ")

                # remake the ship, with a different starting cell
                ship_config = self.get_ship_config()

                # make sure the ship_config is valid, aka
                # the ship fits on the board
                while not self.validate_ship_config(ship_config, ship.get_size()):
                    ship_config = self.get_ship_config()

                cells = self.make_cells(ship.get_size(), ship_config)

            # cells now contains non-colliding cells, safe to place on the board
            for cell in cells:
                placed_cells.add(cell)  # keep track of placed cells
                ship.add_cell(cell)     # place cells on ship
                self.place_cell_on_board(cell)   # place cells on board



            # while loop to handle user input validation for row and column. Might be repetitive?
            """
            while True:

                try:

                    start_row = int(input("Please enter starting row (0-9): "))
                    start_col = int(input("Please enter starting column (0-9): "))
                    orientation = input("Please enter 'v' for verically orientation or 'h' for horizontal orientation: ")
                    
                    # Checks if all user inputs are valid
                    if (start_row < 0) or (start_row > 9) or (start_col < 0) or (start_col > 9) or ((orientation != 'v') and (orientation != "h")):
                        print("Invalid input. Please ensure starting coordinates or orientation are correct. Try again ")
                        continue


                except ValueError:
                    print("Oops, please enter a valid integer! Try again!")
                    continue
                    
                else:
                    if orientation == 'v':
                        if ((start_row + ship.get_size()) <= 9):

                            # Places ships assuming either ship size is (x, 1) or (1, x)
                            for pos in range(ship.get_size()):

                                cell_to_add = tuple((start_row, start_col + pos))

                                if len(self.ships_location) != 0:
                                    
                                    #Iterates through ship cells checking if desired coordinate has already being placed
                                    for ship_name in self.ships_location:
                                        cell_to_add = tuple((start_row + pos, start_col))
                                        if cell_to_add in ship_name.get_cells():
                                            print("Please choose another starting coordinate: ")
                                            continue

                                    ship.add_cell(cell_to_add)
                                ship.add_cell(cell_to_add)
                                # Added the line below to manipulate and show the ship on the board!
                                self.player_board.board[start_row + pos][start_col] = "O"
                            self.ships_location.append(ship)

                    else:
                        if ((start_row + ship.get_size()) <= 9):

                            # Places ships assuming either ship size is (x, 1) or (1, x)
                            for pos in range(ship.get_size()):

                                cell_to_add = tuple((start_row, start_col + pos))

                                if len(self.ships_location) != 0:
                                    #Iterates through ship cells checking if desired coordinate has already being placed
                                    for ship_name in self.ships_location:
                                        if cell_to_add in ship_name.get_cells():
                                            print("Please choose another starting coordinate: ")
                                            continue
                                        
                                    ship.add_cell(cell_to_add)
                                ship.add_cell(cell_to_add)
                                # Added the line below to manipulate and show the ship on the board!
                                self.player_board.board[start_row][start_col + pos] = "O"
                            self.ships_location.append(ship)
                self.player_board.show_board()
                break
                """

                



    def make_turn(self):
        '''
        This method is used by this player to indicate where they want to place their attack.
        '''

        # Had to encase the input with int() because it's originally a string.
        x_target = int(input("Please enter x coordinate to attack: "))
        y_target = int(input("Please enter y coordinate to attack: "))

        # Had to add extra parentheses because I got an error without them. Returns a tuple now.
        return tuple((x_target, y_target))
    
    def attacked(self, target) -> bool:

        '''
        This checks where the spot targeted by opponent had this player's ship,
        if so, we decrement it's length (this is similar to checking if ship has sunk using Ship.has_sunk method)
        '''

        # Boolean flag to keep up with whether or not a ship has been attacked.
        was_attacked = False

        if len(self.ships_location) != 0:
            for ship in self.ships_location:
                if ship.receive_attack(target) == True:
                    # Flag changed to True since it's been attacked.
                    was_attacked = True
                    # The attacked part of the is marked with an X.
                    self.player_board.board[target[0]][target[1]] = "X"
                    if ship.has_sunk() == True:
                        self.ships_location.pop(ship)

        return was_attacked

    def any_remaining_ships(self) -> None:
        '''
        Checks if all this player's ships have been sunk
        '''
        return len(self.ships_location) == 0

    def print_board(self):
        self.player_board.show_board()
