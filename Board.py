from Ship import Ship

class Board:
# 10 x 10 board
def build_game_board(board):
    for item in range(10):
        board.append(["O"] * 10)

def show_board(board):
    for row in board:
        print(" ".join(row))

# Defining ships locations
def load_game(board):
    print("BATTLESHIP")
    del board[:]
    build_game_board(board)
    show_board(board)
ship_points = load_game(game_board)
