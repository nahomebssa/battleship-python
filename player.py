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

    
    def add_ship(self) -> None:
        '''
        Since there are 5 ships to add, this method iterates through the five options 
        changing their cell based on where the user wanted the starting coordinate in relation to 
        the orientation.
        '''

        # Created this list to handle putting ships on the board automatically.
        available_ships = ["Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer"]

        self.player_board.show_board()

        # The for loop below uses the ships in the available_ships to place them without user being asked for name.
        for ship in available_ships:

            self.ship_name = ship
            self.my_ship = Ship(ship)

            print(f"Place Ship: {ship}, Size: {self.my_ship.get_size()}")

            # while loop to handle user input validation for row and column. Might be repetitive?
            while True:
                try:
                    start_row = int(input("Please enter starting row (0-9): "))
                    if start_row < 0 or start_row > 9:
                        print("Oops, your number was not in range! Try again!")
                        continue
                    start_col = int(input("Please enter starting column (0-9): "))
                    if start_col < 0 or start_col > 9:
                        print("Oops, your number was not in range! Try again!")
                        continue
                except ValueError:
                    print("Oops, please enter a valid integer! Try again!")
                    continue
                break

            # while loop to handle user input validation for orientation selection.
            while True:
                orientation = input("Please enter 'v' for verically orientation or 'h' for horizontal orientation: ")
                if orientation != 'v' and orientation != "h":
                    print("Choose a correct orientation!")
                    continue

                if orientation == 'v':
                    if (start_row >= 0) and ((start_row + self.my_ship.get_size()) <= 9):
                        for pos in range(self.my_ship.get_size()):
                            self.my_ship.add_cell(tuple((start_row + pos, start_col)))
                            # Added the line below to manipulate and show the ship on the board!
                            self.player_board.board[start_row + pos][start_col] = "O"
                        self.ships_location.append(self.my_ship)

                else:
                    if (start_col >= 0) and ((start_col + self.my_ship.get_size()) <= 9):
                        for pos in range(self.my_ship.get_size()):
                            self.my_ship.add_cell(tuple((start_row, start_col + pos)))
                            # Added the line below to manipulate and show the ship on the board!
                            self.player_board.board[start_row][start_col + pos] = "O"
                        self.ships_location.append(self.my_ship)
                break

            self.player_board.show_board()

    def make_turn(self):





    def make_turn(self) -> tuple[int, int]:
        '''
        This method is used by this player to indicate where they want to place their attack.
        '''

        # Had to encase the input with int() because it's originally a string.
        x_target = int(input("Please enter x coordinate to attack: "))
        y_target = int(input("Please enter y coordinate to attack: "))

        # Had to add extra parentheses because I got an error without them. Returns a tuple now.
        return tuple((x_target, y_target))
    
    def attacked(self, target) -> None:

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

