"""
Implementation of the game of Poisoned Chocolate Bar
Yurekce Altin  2526085
Mahrad Hosseini 2528388
"""

import copy

"""
The Game class holding everything related to the game
"""


class Game:
    def __init__(self, row, column, poison_row, poison_column):
        # Create a row by column grid
        # Python stores and accesses board in matrix format for example:
        # 5x4 matrix:
        # [
        #  [a11, a12, a13, a14],
        #  [a21, a22, a23, a24],
        #  [a31, a32, a33, a34],
        #  [a41, a42, a43, a44],
        #  [a51, a52, a53, a54]
        # ]

        self.board = [['O' for _ in range(column)] for _ in range(row)]
        self.board[poison_row][poison_column] = 'P'
        self.row = row
        self.column = column
        self.poison_row = poison_row
        self.poison_column = poison_column
        self.player = 'max'  # max starts

    """
    Method responsible for printing the board
    """

    def print_board(self):
        print("Board:")
        for row in self.board:
            print(' '.join(row))
        print()

    """
    Method responsible for checking if the move is valid
    """

    def is_move_valid(self, row, column):
        return True if 0 <= row < self.row and 0 <= column < self.column and (
                self.board[row][column] == 'O' or self.board[row][column] == 'P') else False

    """
    Method responsible for making the move and removing the eaten tiles
    """

    def make_move(self, row, column):
        for i in range(row, self.row):
            for j in range(column, self.column):
                self.board[i][j] = ''
        return True

    """
    Method responsible for checking if the poison tile is eaten
    """

    def is_game_over(self):
        return True if self.board[0][0] == '' else False

    """
    Method responsible for returning whose turn it is (Min or Max)
    """

    def to_move(self):
        return self.player

    """
    Method responsible for returning all the actions possible at a given state
    """

    def actions(self, state):
        actions = [(i, j) for i in range(self.row) for j in range(self.column) if state[i][j] != '']
        return actions

    """
    Method responsible for returning the result of making a specific move at a specific state
    """

    def result(self, state, action):
        row, column = action
        state_new = copy.deepcopy(state)
        for i in range(row, self.row):
            for j in range(column, self.column):
                state_new[i][j] = ''
        return state_new

    """
    Method responsible for switching the player from Min to Max or vice versa
    """

    def change_player(self):
        self.player = 'max' if self.player == 'min' else 'min'
