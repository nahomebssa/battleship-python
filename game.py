import os
import random
import sys
from player import Player
from ship import Ship
from board import Board

class Game():

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.current_player = None
        self.next_player = None

    def choose_first_player(self):
        self.current_player = random.choice([self.player1, self.player2])

        if self.current_player == self.player1:
            self.next_player = self.player2
        else:
            self.next_player = self.player1


