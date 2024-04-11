# Minimax Algorithm for Tic-Tac-Toe Game
import math
import numpy as np
import copy
from classes.Game import TicTacToe

def minimax(board, depth):
    if board.is_terminal() or depth == 0:
        return board.utility(), None

    best_value = -math.inf if board.player() == 'X' else math.inf
    best_move = None

    current_state = copy.deepcopy(board.state)
    for move in board.actions():
        board.set_state(current_state)
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


if __name__ == "__main__":
    b = TicTacToe((3,3))
    b.make_move(np.array([2,1]))
    b.make_move(np.array([1,1]))
    b.make_move(np.array([2,2]))
    print(b.state)
    print(minimax(copy.deepcopy(b), 5))
    b.init_state()
    