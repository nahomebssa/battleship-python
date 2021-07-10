from game import Game
from player import Player

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

    game.clear_screen()

    print(f"{player2.playerName}, place your ships!")
    player2.add_ship()

    player1.player_board.clear_board()
    player2.player_board.clear_board()

    game.clear_screen()

    winner_of_game = game.play()

    print(f"The winner of this game is: {winner_of_game.player_name}!")


if __name__ == '__main__':
    main()

