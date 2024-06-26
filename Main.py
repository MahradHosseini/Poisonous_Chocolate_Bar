"""
Implementation of the main loop of the game.
Yurekce Altin  2526085
Mahrad Hosseini 2528388
"""

from Game import *
from MiniMax import *

"""
The main method which is responsible for running the game in general
"""
if __name__ == "__main__":

    # Getting mode from user and checking for errors
    mode = int(input("Which mode do you want to play?\nHuman vs. AI [1]\nHuman vs. Human [2]\n"))
    if mode not in (1, 2):
        raise ValueError("Invalid mode")

    # Getting chocolate bar size from user and checking for errors
    row, column = map(int, input("Enter the number of rows and columns with a space in between:\n").split())
    if column <= 0 or row <= 0:
        raise ValueError("Invalid row or column")

    # Getting poison position from user and checking for errors
    poison_row, poison_column = map(int, input(
        "Enter the row and column of the poisonous tile with a space in between:\n").split())
    if poison_row not in range(0, row) or poison_column not in range(0, column):
        raise ValueError("Invalid poison location")

    print("----------------------\n----------------------\n\nWelcome to Poisonous Chocolate Bar!\n")
    print("Your initial board is:")
    game = Game(row, column, poison_row, poison_column)  # Initializing game object
    game.print_board()
    turn = 1

    # mode 1: AI vs. Human
    if mode == 1:
        print("You've entered AI mode.....")
        # If user chose to player first turn will be 1, otherwise 2
        turn = int(input("Would you like to start first?\nYes [1]\nNo [2]\n"))

        while not game.is_game_over():
            if turn == 1:
                # Getting move input
                move_row, move_column = map(int, input("Make your move (Row Column):\n").split())
                if game.is_move_valid(move_row, move_column):
                    game.make_move(move_row, move_column)
                    game.change_player()  # Changing the player from min to max or vice versa
                    game.print_board()
                    turn = 2  # Passing the turn to the other player
                else:
                    raise ValueError("Invalid player move")
            else:
                print("AI's turn")
                # Calling Minimax Search Algo to make a move
                move_row, move_column = mini_max_search(game)
                if game.is_move_valid(move_row, move_column):
                    game.make_move(move_row, move_column)
                    game.change_player()  # Changing the player from min to max or vice versa
                    game.print_board()
                    turn = 1  # Passing the turn to the other player
                else:
                    raise ValueError("Invalid AI move")

        # Checking whose turn it was at the terminal state to decide on the winner
        if turn == 1:
            print("You won!")
        else:
            print("You lost!")

    # Mode 2: Human vs. Human
    else:
        print("You've entered multiplayer mode......")
        # Getting players' names input
        player1 = str(input("Enter Player 1 name: "))
        player2 = str(input("Enter Player 2 name: "))

        while not game.is_game_over():
            if turn == 1:
                # Getting move input
                move_row, move_column = map(int, input(f"{player1} make your move (Row Column):\n").split())
                if game.is_move_valid(move_row, move_column):
                    game.make_move(move_row, move_column)
                    game.print_board()
                    turn = 2  # Passing the turn to the other player
                else:
                    raise ValueError(f"Invalid move {player1}!")
            else:
                # Getting move input
                move_row, move_column = map(int, input(f"{player2} make your move (Row Column):\n").split())
                if game.is_move_valid(move_row, move_column):
                    game.make_move(move_row, move_column)
                    game.print_board()
                    turn = 1  # Passing the turn to the other player
                else:
                    raise ValueError(f"Invalid move {player2}!")

        # Checking whose turn it was at the terminal state to decide on the winner
        if turn == 1:
            print(f"{player1} won!")
        else:
            print(f"{player2} won!")
