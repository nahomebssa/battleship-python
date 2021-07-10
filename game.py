import os
from time import sleep
from player import Player
from Ship import Ship
from Board import Board


class Game:

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.round = 0

    def get_current_player(self):
        players = [self.player1, self.player2]
        return players[self.round % len(players)]

    def get_next_player(self):
        players = [self.player1, self.player2]
        return players[(self.round + 1) % len(players)]

    def clear_screen(self, duration=2):

        if os.name == 'posix':
            _ = os.system('clear')
        else:
            _ = os.system('cls')
        sleep(duration)

    def play(self):
        is_running = True
        winner = None

        while is_running:
            '''
            Clears the screen
            '''
            self.clear_screen()

            '''
            # Retrieves the current player's board and alerts them that it's their turn.
            '''
            print(len(self.get_next_player().ships_location))
            self.get_next_player().print_board()
            print(self.get_current_player().playerName + "'s turn!")

            '''
            # Current player selects where they want to attack, and it's stored in a variable.
            '''
            selected_coordinates = self.get_current_player().make_turn()

            ''' 
            If there is a hit on the next player's board, the current player is told so. 
            If not, they're told it was a miss.
            '''
            if self.get_next_player().attacked(selected_coordinates):
                print("It was a hit!")
                sleep(2)
                if self.get_current_player().any_remaining_ships():
                    winner = self.get_next_player()
                    is_running = False

                if self.get_next_player().any_remaining_ships():
                    winner = self.get_current_player()
                    is_running = False
            else:
                print("It's a miss!")
                sleep(2)
            '''
            Increment the round variable to be used in the get_current_player() and get_next_player() methods.
            '''
            self.round += 1

        return winner

