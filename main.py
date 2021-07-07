class Ship: pass

class Board: pass

class Player: 
    '''
    This class defines a player who will play the game against another player. This class is able to add ships to the board.
    To ensure that ship position is hidden, we only store the ship coordinates and refer to them.
    Furthermore, we can remove a specific ship if the player wants to.
    This class will also enable us to know if a certain player has won the game.
    '''
    def __init__(self, playerName, shipClass, boardClass, playerScore = 0) -> None:
        self.playerName = playerName
        self.playerScore = playerScore
        # Currently looking for ways to pass a class as a parameter if that is possible. Furthermore, want to create a global dict
        self.board = boardClass
        self.ships = shipClass
        self.ship_location = dict()
    
    def add_ship(self, ships) -> None:
        
        for _ in range(0, 6):
            orientation = input("Please enter v or h for vertical or horizontal orientation respectively: ")

            while (orientation != 'v') or (orientation != 'h'):
                print("Invalid orientation")
                orientation = input("Please enter v or h for vertical or horizontal orientation respectively: ")
            if orientation == 'v':
                print("Please note that ships will be built top -> down")
                placement = tuple(input("Please specify starting coordinate i.e (0, 0): "))
                for _ in range(ships.length):
                    if ships.name not in ship_location:
                        ship_location[ships.name] = [placement]
                    else:
                        ship_location[ships.name].append((placement[0], placement[1] + 1))

            elif orientation == 'h':
                print("Please note that ships will be built left -> right")
                placement = tuple(input("Please specify which row to place ship, i.e 0-9: "))
                for _ in range(ships.length):
                    if ships.name not in ship_location:
                        ship_location[ships.name] = [placement]
                    else:
                        ship_location[ships.name].append((placement[0] + 1, placement[1]))

    def remove_ship(self, ship_name) -> None:

        if ship_name in ship_location:
            ship_location.pop(ship_name)
        else:
            print("No such ship")
    
    def any_ships_remaining(self) -> bool:

        if len(ship_location) != 0:
            return True
        else:
            return False



class Game: pass
