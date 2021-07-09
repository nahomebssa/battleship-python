from Ship import Ship

class Board:
# 10 x 10 board

    def __init__(self):
      self.board = []

    def build_game_board(self):
        for item in range(10):
            self.board.append(["-"] * 10),

    def show_board(self):
        for row in self.board:
            print(" ".join(row))

    def load_game(self):
        print("BATTLESHIP")
        print("\033[1m0 1 2 3 4 5 6 7 8 9 \033[1m")

# load_game(board)
# build_game_board()
# show_board(board)
