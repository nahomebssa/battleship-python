from game import Game
from player import Player

"""
This is the main file that needs to be executed in order to play the game.
"""

def main():

    print("Welcome to Battleship!")
    print()

    player1 = Player(input("Player 1, please enter your name: "))
    player2 = Player(input("Player 2, please enter your name: "))

    game = Game(player1, player2)

    print("Time to place your ships!")
    print()

    print(f"{player1.playerName}, place your ships!")
    player1.add_ship()

    print(f"Here's your board, {player1.playerName}!")
    player1.print_board()
    input("Press enter to continue: ")

    game.clear_screen()

    print(f"{player2.playerName}, place your ships!")
    player2.add_ship()

    print(f"Here's your board, {player2.playerName}!")
    player2.print_board()
    input("Press enter to continue: ")

    player1.player_board.clear_board()
    player2.player_board.clear_board()

    game.clear_screen()

    winner_of_game = game.play()

    print(f"The winner of this game is: {winner_of_game.playerName}!")


if __name__ == '__main__':
    main()

