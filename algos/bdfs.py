# BFS & DFS integrated into one Algorithm
from classes.structures.Stack import Stack
from classes.structures.Queue import Queue
from typing import Union
from support.maze_agent import get_index, U, f
import pandas as pd
import numpy as np

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
status, visited_maze, Q_s = BDFS(s, (6,0), (3,3), pd.read_csv('../datasets/mazes/maze_01.csv', header=None).to_numpy())
print(f"Maze has solution to target state? : {status}\n")

# Uncomment to use BFS implementation
# q = Queue()
# status, visited_maze, Q_s = BDFS(s, (6,0), (3,3), pd.read_csv('datasets/maze_01.csv', header=None).to_numpy())
# print(f"Maze has solution to target state? : {status}\n")