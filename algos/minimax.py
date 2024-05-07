# Minimax Algorithm for Tic-Tac-Toe Game
import math
import copy
import numpy as np
from classes.Game import Board

def minimax(board, depth):
    if board.is_terminal() or depth == 0:
        return board.utility(), None

    best_value = -math.inf if board.player() == 'X' else math.inf
    best_move = None

    for move in board.actions():
        board.make_move(move)
        val, _ = minimax(copy.deepcopy(board), depth - 1)
        board.undo_move()

        if board.player() == 'X':
            if val > best_value:
                best_value = val
                best_move = move
        else:
            if val < best_value:
                best_value = val
                best_move = move

    return best_value, best_move

def minimax_it(board, depth, iterations):
    if board.is_terminal() or depth == 0:
        return board.utility(), None, iterations

    best_value = -math.inf if board.player() == 'X' else math.inf
    best_move = None

    for move in board.actions():
        iterations += 1
        board.make_move(move)
        val, _, iterations = minimax(copy.deepcopy(board), depth - 1, iterations)
        board.undo_move()

        if board.player() == 'X':
            if val > best_value:
                best_value = val
                best_move = move
        else:
            if val < best_value:
                best_value = val
                best_move = move

    return best_value, best_move, iterations

if __name__ == "__main__":
    b = Board((3,3))
    b.make_move(np.array([2,1]))
    b.make_move(np.array([1,1]))
    b.make_move(np.array([2,2]))
    print(b.state)
    print(minimax(copy.deepcopy(b), 5))
    b.init_state()
    