import copy
import math
import numpy as np
from classes.players.Player import Player
from classes.algos.minimax import minimax

class SmartComputerPlayer(Player):
    def __init__(self, letter) -> None:
        super().__init__(letter)

    def get_move(self, game):
        if game.actions().shape[0] == 9:
            U = game.actions()
            corner_filter = np.array([[0,0],[0,2],[2,0],[2,2]])
            is_corner = np.all(np.isin(U, corner_filter), axis=1)
            corner_moves = U[is_corner]
            move = corner_moves[np.random.choice(corner_moves.shape[0], size=1, replace=False), :].flatten()
            print(f"Minimax played: {move}\n")
        else:
            move = minimax(copy.deepcopy(game), 3)[1]
            print(f"Minimax played: {move}\n")
        return move