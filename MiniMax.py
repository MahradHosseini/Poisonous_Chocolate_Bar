"""
Implementation of the Minimax algorithm
Yurekce Altin  2526085
Mahrad Hosseini 2528388
"""

"""
Method responsible for solving the minimax problem and returning the best move
"""


def mini_max_search(game):
    global node_count  # Using a global variable to track the count of nodes
    node_count = 0
    state = game.board
    # If AI is playing as Max (which means it was the first one to make a move), start from max-value function, else start from min-value function
    if game.player == 'max':
        _, move = max_value(game, state)
    else:
        _, move = min_value(game, state)

    print(f"Number of nodes visited by MiniMax Search: {node_count}")
    return move


"""
Method responsible for solving Minimax problem as a Max player, choosing a move with highest utility.
Returning the best move with its value
"""


def max_value(game, state):
    # Accessing the global variable node_count and incrementing it
    global node_count
    node_count += 1

    # If the game is in terminal state, return the utility
    if is_terminal(state):
        return utility(state, player='max'), None
    v = float('-inf')
    move = None

    # Calculate V value for every action possible in this state and choose the highest one
    for a in game.actions(state):
        v2, _ = min_value(game, game.result(state, a))
        if v2 > v:
            v, move = v2, a
    return v, move


"""
Method responsible for solving Minimax problem as a Min player, choosing a move with lowest utility.
Returning the best move with its value
"""


def min_value(game, state):
    # Accessing the global variable node_count and incrementing it
    global node_count
    node_count += 1

    # If the game is in terminal state, return the utility
    if is_terminal(state):
        return utility(state, player='min'), None
    v = float('inf')
    move = None

    # Calculate V value for every action possible in this state and choose the lowest one
    for a in game.actions(state):
        v2, _ = max_value(game, game.result(state, a))
        if v2 < v:
            v, move = v2, a
    return v, move


"""
Method responsible for checking if the state is a terminal state
"""


def is_terminal(state):
    return True if state[0][0] == '' else False


"""
Method responsible for retuning the utility of the current state
"""


def utility(state, player):
    if is_terminal(state):
        return 1 if player == 'max' else -1
    return 0
