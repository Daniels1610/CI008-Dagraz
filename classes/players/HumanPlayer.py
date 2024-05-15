import numpy as np
from classes.players.Player import Player


class HumanPlayer(Player):
    def __init__(self, letter) -> None:
        super().__init__(letter)
    def get_move(self, game) -> np.ndarray:
         valid_square = False
         move = None
         while not valid_square:
             move = np.array([int(x) for x in input(f"It's Human Player Turn!: ").split()])
             try:
                 if move not in game.actions():
                     raise ValueError
                 valid_square = True
             except ValueError:
                 print("Invalid Square. Try Again")
         return move 