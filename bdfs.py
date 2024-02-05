# BFS & DFS integrated into one Algorithm

from classes.Stack import Stack
from classes.Queue import Queue
from typing import Union
import pandas as pd
import numpy as np

"""
Agent Actions (Clockwise):
- Up : (x-1, y)
- Right : (x, y+1)
- Down : (x+1, y)
- Left : (x, y-1)
"""

def f(x: tuple, u: tuple):
    return np.add(x,u)

def U(state: tuple, maze_dim: tuple) -> np.ndarray:
    U = []
    if not (state[0] - 1 < 0): U.append((-1,0))  # aMove Up
    if not (state[1] + 1 > maze_dim[1] - 1): U.append((0,1))  # Move Right
    if not (state[0] + 1 > maze_dim[0] - 1): U.append((1,0))  # Move Down
    if not (state[1] - 1 < 0): U.append((0,-1))  # Move Left
    return np.array(U)
  
def get_index(state: tuple, maze_dim: tuple):
    return (state[0] * (maze_dim[1])) + state[1]

def BDFS(Q: Union[Stack, Queue], init_x: tuple, target_x: tuple, maze_data: np.ndarray) -> np.ndarray:
    visited_maze = np.copy(maze_data) 
    maze_dim = maze_data.shape
    Q.insert(init_x); visited_maze.put(get_index(init_x, maze_dim), 2)
    while Q.size() != 0:
        x = Q.get_first() # Current State
        if x[0] == target_x[0] and x[1] == target_x[1]:
            return True, visited_maze, Q # SUCCESS
        for u in U(x, maze_dim):
            next_x = f(x,u)
            if visited_maze[next_x[0],next_x[1]] == 2: continue
            elif visited_maze[next_x[0],next_x[1]] == 0:
                visited_maze.put(get_index(next_x, maze_dim), 2)
                Q.insert(next_x)
    return False, visited_maze, Q # FAILURE

# DFS execution
s = Stack()
status, visited_maze, Q_s = BDFS(s, (6,0), (3,3), pd.read_csv('datasets/maze_01.csv', header=None).to_numpy())
print(f"Maze has solution to target state? : {status}\n")

# Uncomment to use BFS implementation
# q = Queue()
# status, visited_maze, Q_s = BDFS(s, (6,0), (3,3), pd.read_csv('datasets/maze_01.csv', header=None).to_numpy())
# print(f"Maze has solution to target state? : {status}\n")