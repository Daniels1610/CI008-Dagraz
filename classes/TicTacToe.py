import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from IPython.display import display

X_SYMBOL = 'X'
O_SYMBOL = 'O'
X_COLOR = 'b'
O_COLOR = 'r'
SYMBOL_SIZE = 70
X_POS = {0: 0.2, 1: 1.15, 2: 2.17}
Y_POS = {0: 2.20, 1: 1.20, 2: 0.15}

class Board():
    __graph_board : Figure   # Visual representation 
    __s : np.ndarray         # Board state
    __bin: tuple               # Tuple that contains 0s and 1s count from s
    __history: list            # Stores played moves
    __ply: int                 # Number of moves
    __dim: tuple               # Board dimensions


    def __init__(self, dim:tuple) -> Figure:
        self.__s = np.empty(dim, dtype=object)
        self.__graph_board = None
        self.__history = []
        self.__ply = 0
        self.__dim = dim
        self.set_bin()
        self.__init_board()
 
    # BOARD METHODS
    # Board Initialization
    def __init_board(self):
        """
        A helper function to plot Tic-Tac-Toe Board
        """
        plt.ioff()

        # Create a new figure
        self.__graph_board, ax = plt.subplots()
        self.__graph_board.set_facecolor('k')

        # Draw Board
        for i in range(1, self.__dim[0]):
            ax.plot([0, self.__dim[0]], [i, i], 'w-')
            ax.plot([i, i], [0,self.__dim[0]], 'w-')

        # Set the aspect of the plot to be equal to get a square grid
        ax.set_aspect('equal')

        # Remove axes
        ax.axis('off')
    
    # Resets board
    def init_state(self):
        self.__init__(self.__dim)

    # Visually display current game board
    def update_board(self, u:np.ndarray) -> Figure:
        x, y = u[0], u[1]
        if self.__s[x, y] is not None:
            symbol = X_SYMBOL if self.__s[x, y] == 1 else O_SYMBOL
            color = X_COLOR if symbol == X_SYMBOL else O_COLOR
            plt.text(X_POS[y], Y_POS[x], symbol, fontsize=SYMBOL_SIZE, color=color)


    # AGENT METHODS
        
    # Gets the player in turn to play from board state
    def player(self) -> str:
        if (self.isTerminal()): return 'Board is Filled'
        return 'X' if np.sum(self.__s == 1) <= np.sum(self.__s == 0) else 'O'

    # Executes board move (TRANSITION FUNCTION f(x,u))
    def make_move(self, x:np.ndarray):
        x = x.flatten()
        if self.__s[x[0], x[1]] is None:
            self.__s[x[0], x[1]] = 1 if self.player() == 'X' else 0
            self.__history.append(x)
            self.__ply += 1
            self.update_board(x)
        self.set_bin()

    # Reverts last move
    def undo_move(self, x:np.ndarray):
        self.__s[x[0], x[1]] = None

    # Get player's actions from given state (SPACE SEARCH U(x))
    def actions(self) -> np.ndarray:
        return np.transpose(np.where(self.__s == None))

    # From current board state, indicates if the board is filled
    def isTerminal(self) -> bool:
        if (np.sum(self.bin) == np.prod(self.__s.shape)): return True
        else: return False

    # TODO: Given a Terminal Board return the game's outcome
    
    # GETTERS
    @property
    def board(self) -> Figure:
        return self.__graph_board
    
    @property
    def state(self) -> np.ndarray:
        return self.__s
    
    @property
    def history(self) -> list:
        return self.__history
    
    @property
    def ply(self) -> int:
        return self.__ply
    
    # SETTERS
    def set_state(self, s:np.ndarray):
        self.__s = s
        self.set_bin()

    def set_bin(self):
        self.bin = np.bincount(self.__s[(self.__s != None)].astype(np.int8))

        
# Class Test
if (__name__ == "__main__"):
    # Board Initialization
    b = Board((3,3))
    init_board = b.state

    # Game continues while there are None values on the board
    while (np.any(b.state == None)):
        # Get available actions for player in turn
        U = b.actions()

        # Randomly selects one action from action space
        z = U[np.random.choice(U.shape[0], size=1, replace=False), :] 

        # Execute selected move
        move = b.make_move(z)
        
        # TODO: Given an In-Game checks if there is a winner


    print(f"MOVE HISTORY:\n{np.array(b.history).reshape(-1,2)}")
    print(f"FINAL BOARD:\n{b.state}")
    print(f"PLAYER TURN: {b.player()} ")
    print(f'IS TERMINAL: {b.isTerminal()}')
    plt.show()