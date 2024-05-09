import copy
import math
import numpy as np
from classes.players.Player import Player
from algos.minimax import minimax, minimax_it
from algos.alfabeta import alfabeta_it

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
            # Alfa-Beta Pruning Search
            val, move, iterations, recursions = alfabeta_it(copy.deepcopy(game), 3, -math.inf, math.inf, 0, 0)
            print(f"Alfa-Beta played: {move}\n")
            print(f"Move Utility: {val}\n")
            print(f"ITERATIONS TO FIND BEST MOVE: {iterations}")
            print(f"RECURSIONS MADE: {recursions}")
            

            # Minimax Search
            # move = minimax_it(copy.deepcopy(game), 3)[1]
            # print(f"Minimax played: {move}\n")
            # print(f"ITERATIONS TO FIND BEST MOVE: {iterations}")
        return move