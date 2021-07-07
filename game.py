import os
import sys
from time import sleep
from player import Player
from ship import Ship
from board import Board

class Game():

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.current_player = None
        self.next_player = None
        self.round = 0

    def get_current_player(self):
        players = [self.player1, self.player2]
        return players[self.round % len(players)]

    def get_next_player(self):
        players = [self.__player_1, self.__player_2]
        return players[(self.round + 1) % len(players)]

    def clear_screen():

        if os.name == 'posix':
            _ = os.system('clear')
        else:
            _ = os.system('cls')

    def play():
        """
        while True:
            #Clear Screen
            clear_screen()
            sleep(1)

            current_player = self.get_current_player()
            current_player.get_board()

            print(f"{current_player}'s turn!")
        """