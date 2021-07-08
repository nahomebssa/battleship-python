from Ship import Ship
class Player: 
    '''
    This class defines a player who will play the game against another player. This class is able to add ships to the board.
    To ensure that ship position is hidden, we only store the ship coordinates and refer to them.
    Furthermore, we can remove a specific ship if the player wants to.
    This class will also enable us to know if a certain player has won the game.

    '''


    def __init__(self, playerName) -> None:

        self.playerName = playerName
        self.ships_location = dict()
    
    def add_ship(self) -> None:
        '''
        Since there are 5 ships to add, this method iterates through the five options 
        changing their cell based on where the user wanted the starting coordinate in relation to 
        the orientation.
        '''
        for _ in range(1, 6):

            self.ship_name = input("Please enter correct ship name: ")
            self.my_ship = Ship(self.ship_name)

            start_row = input("Please enter starting row: ")
            start_col = input("Please enter starting column: ")

            orientation = input("Please enter 'v' for verically orientation or 'h' for horizontal orientation: ")

            if orientation == 'v':
                if (start_row >= 0) and ((start_row + self.my_ship.get_size()) <= 9):
                    for pos in range(self.my_ship.get_size()):
                        self.my_ship.add_cell(tuple(start_row + pos, start_col))
                    self.ships_location[self.my_ship] = self.my_ship.get_size()
                
            elif orientation == 'h':
                if (start_col >= 0) and ((start_col + self.my_ship.get_size()) <= 9):
                    for pos in range(self.my_ship.get_size()):
                        self.my_ship.add_cell(tuple(start_row, start_col + pos))
                    self.ships_location[self.my_ship] = self.my_ship.get_size()
            else:
                print("Please enter correct orientation")





    def make_turn(self) -> tuple[int, int]:
        '''
        This method is used by this player to indicate where they want to place their attack.
        '''

        x_target = input("Please enter x coordinate to attack: ")
        y_target = input("Please enter y coordinate to attack: ")

        return tuple(x_target, y_target)
    
    def attacked(self, target: tuple[int, int]) -> None:

        '''
        This checks where the spot targeted by opponent had this player's ship,
        if so, we decrement it's length (this is similar to checking if ship has sunk using Ship.has_sunk method)
        '''
        if len(self.ships_location) != 0:
            for ship in self.ships_location:
                if ship.receive_attack(target) == True:
                    self.ships_location[ship] -= 1

            
    
    
    def any_remaining_ships(self) -> None:
        '''
        Checkes if all this player's ships have been sunk
        '''
        return len(self.ships_location) == 0
    
