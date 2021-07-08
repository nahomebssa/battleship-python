from Ship import Ship

class Board:
# 10 x 10 board
  board = []

  def build_game_board(board):
    for item in range(10):
        board.append(["O"] * 10),

  def show_board(board):
      for row in board:

        print(" ".join(row))

  def load_game(board):
    print("BATTLESHIP")
    print("\033[1m0 1 2 3 4 5 6 7 8 9 \033[1m")

  def clear_board(board):
    del board[:]
    build_game_board(board)
    show_board(board)

  load_game(board)
  build_game_board(board)
  show_board(board)
