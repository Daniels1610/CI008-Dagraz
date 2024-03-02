import numpy as np
from typing import Union

"""
Agent Actions (Clockwise):
- Up : (x-1, y)
- NorthEast : (x-1, y+1)
- Right : (x, y+1)
- SouthEast : (x+1, y+1)
- Down : (x+1, y)
- SouthWest : (x+1, y-1)
- Left : (x, y-1)
- NorthWest : (x-1, y-1)
"""

# Von Neuman Neighborhood (4 Moves)
def U(state: tuple, maze_dim: tuple) -> np.ndarray:
    U = []
    if not (state[0] - 1 < 0): U.append((-1,0))               # Move Up
    if not (state[1] + 1 > maze_dim[1] - 1): U.append((0,1))  # Move Right
    if not (state[0] + 1 > maze_dim[0] - 1): U.append((1,0))  # Move Down
    if not (state[1] - 1 < 0): U.append((0,-1))               # Move Left
    return np.array(U)

# Moore's Neighborhood (8 Moves)
def Um(state: tuple, maze_dim: tuple) -> np.ndarray:
    U = []
    # Move North (Up)
    if not (state[0] - 1 < 0): U.append((-1,0))
    # Move NorthEast
    if not (state[0] - 1 < 0) and not (state[1] + 1 > maze_dim[1] - 1): U.append((-1, 1))  
    # Move East (Right)
    if not (state[1] + 1 > maze_dim[1] - 1): U.append((0,1))  
    # Move SouthEast 
    if not (state[0] + 1 > maze_dim[0] - 1) and not (state[1] + 1 > maze_dim[1] - 1): U.append((1, 1))
    # Move South (Down)
    if not (state[0] + 1 > maze_dim[0] - 1): U.append((1,0))
    # Move SouthWest
    if not (state[0] + 1 > maze_dim[0] - 1) and not (state[1] - 1 < 0): U.append((1, -1))                              
    # Move West (Left)
    if not (state[1] - 1 < 0): U.append((0,-1))
    # Move NorthWest
    if not (state[0] - 1 < 0) and not (state[1] - 1 < 0): U.append((-1,-1))                              
    return np.array(U)

def f(x: tuple, u: tuple):
    return tuple(np.add(x,u))

def get_index(state: tuple, maze_dim: tuple):
    return (state[0] * (maze_dim[1])) + state[1]

def is_diagonal(action: tuple):
    return not (action[0] == 0 or action[1] == 0)

def manhattan_distance(p1:tuple, p2:tuple) -> int:
    return np.abs(p1[0] - p2[0]) + np.abs(p1[1] - p2[1])

def euclidean_distance(p1:tuple, p2:tuple) -> Union[float, int]:
    return np.sqrt(np.power(p1[0] - p2[0],2) + np.power(p1[1] - p2[1],2))