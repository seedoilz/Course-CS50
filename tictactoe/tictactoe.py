"""
Tic Tac Toe Player
"""
import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count = 0
    for line in board:
        for entity in line:
            if entity is not None:
                count += 1
    if count % 2 == 1:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            if board[i][j] is None:
                possible_actions.add((i, j))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    result = copy.deepcopy(board)
    result[action[0]][action[1]] = player(board)
    return result


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(0, len(board)):
        target = board[i][0]
        count = 0
        for j in range(0, len(board[i])):
            if board[i][j] == target:
                count += 1
            else:
                break
            if count == 3:
                return target
    for j in range(0, len(board[0])):
        target = board[0][j]
        count = 0
        for i in range(0, len(board)):
            if board[i][j] == target:
                count += 1
            else:
                break
            if count == 3:
                return target

    target = board[0][0]
    count = 0
    for i in range(0, len(board)):
        if board[i][i] == target:
            count += 1
        else:
            break
        if count == 3:
            return target

    target = board[0][2]
    count = 0
    for i in range(0, len(board)):
        if board[i][2 - i] == target:
            count += 1
        else:
            break
        if count == 3:
            return target
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    else:
        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                if board[i][j] is None:
                    return False
        return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else:
            return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        if player(board) == X:
            value, optimal_action = max_value(board)
            return optimal_action
        else:
            value, optimal_action = min_value(board)
            return optimal_action


def max_value(board):
    if terminal(board):
        return utility(board), None
    v = -1000000
    act = None
    for action in actions(board):
        temp, temp_action = min_value(result(board, action))
        if temp > v:
            v = temp
            act = action
    return v, act


def min_value(board):
    if terminal(board):
        return utility(board), None
    v = 100000
    act = None
    for action in actions(board):
        temp, temp_action = max_value(result(board, action))
        if temp < v:
            v = temp
            act = action
    return v, act
