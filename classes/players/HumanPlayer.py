import numpy as np
from classes.players.Player import Player

class HumanPlayer(Player):
    def __init__(self, letter) -> None:
        super().__init__(letter)

    def get_move(self, game) -> np.ndarray:
        valid_square = False
        move = None
        while not valid_square:
            col = int(input(f"It's Human Player Turn!: "))

            try:
                if col < 0 and col > game.state.shape[1]:
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Invalid Column. Try Again")

        m = []
        for move in game.actions():
            if move[1] == col:
                m.append(move)
        return m[-1]