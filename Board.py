class Board:

    """
    This class is used to define a Board that is 10x10.
    Each player is expected to have an instance of this board.
    """

    def __init__(self):
        self.board = []

    def build_game_board(self):
        empty_water = "-"
        for item in range(10):
            self.board.append([empty_water] * 10),

    def show_board(self):
        for row in self.board:
            print(" ".join(row))

    def clear_board(self):
        del self.board[:]
        self.build_game_board()


'''   
    print something like this in the main.py
                                                               01
    todo: numbers on left side (may create complication) e.g. 0--
                                                              1--
                                                              
    Plan on implementing soon using the code below:
        def load_game(self):
        print("BATTLESHIP")
        print("\033[1m0 1 2 3 4 5 6 7 8 9 \033[1m")
'''
