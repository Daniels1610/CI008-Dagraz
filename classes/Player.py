import math
import copy
import numpy as np

class Player():
    def __init__(self, letter) -> None:
        self.letter = letter

    def get_move(self, game):
        pass

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
    

class RandomComputerPlayer(Player):
    def __init__(self, letter) -> None:
        super().__init__(letter)

    def get_move(self, game) -> np.ndarray:
        U = game.actions()
        move = U[np.random.choice(U.shape[0], size=1, replace=False), :].flatten()
        print(f"BOT played: {move}")
        return move
    

class SmartComputerPlayer(Player):
    def __init__(self, letter) -> None:
        super().__init__(letter)

    def get_move(self, game):
        if game.actions().shape[0] == 9:
            U = game.actions()
            move = U[np.random.choice(U.shape[0], size=1, replace=False), :].flatten()
        else:
            move = self.minimax(copy.deepcopy(game), 3)[1]
            print(f"Minimax played: {move}\n")
        return move
    
    def minimax(self, board, depth):
        if board.is_terminal() or depth == 0:
            return board.utility(), None

        best_value = -math.inf if board.player() == 'X' else math.inf
        best_move = None

        current_state = copy.deepcopy(board.state)
        for move in board.actions():
            board.set_state(current_state)
            board.make_move(move)
            val, _ = self.minimax(copy.deepcopy(board), depth - 1)
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
        
    
