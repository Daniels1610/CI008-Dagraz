# Alfa-Beta Pruning Algorithm for Tic-Tac-Toe Game
import math
import numpy as np
import copy
from classes.Game import Board


def alfabeta(board, depth:np.int8, alpha, beta, iterations):
    a = alpha; b = beta

    if board.is_terminal() or depth == 0:
        return board.utility(), None, iterations

    best_value = -math.inf if board.player() == 'X' else math.inf
    best_move = None

    for move in board.actions():
        iterations += 1
        board.make_move(move)
        val, _, iterations = alfabeta(copy.deepcopy(board), depth - 1, alpha, beta, iterations)
        board.undo_move()

        if board.player() == 'X':
            if val > best_value:
                best_value = val
                best_move = move
            a = np.maximum(a, val)
            if a >= b: break
        else:
            if val < best_value:
                best_value = val
                best_move = move
            b = np.minimum(b, val)
            if a >= b: break
    return best_value, best_move, iterations


# Alfa-Beta Pruning Testing
if __name__ == "__main__":
    b = Board((3,3))
    b.make_move(np.array([2,1]))
    b.make_move(np.array([1,1]))
    b.make_move(np.array([2,2]))
    print(b.state)
    print(alfabeta(copy.deepcopy(b), 7, -math.inf, math.inf, 0))
    b.init_state()