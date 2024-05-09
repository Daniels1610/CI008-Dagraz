import numpy as np
from classes.players.Player import Player

class RandomComputerPlayer(Player):
    def __init__(self, letter) -> None:
        super().__init__(letter)

    def get_move(self, game) -> np.ndarray:
        U = game.actions()
        move = U[np.random.choice(U.shape[0], size=1, replace=False), :].flatten()
        print(f"BOT played: {move}")
        return move