from collections import deque
from typing import Union

class Border():
    __Q : deque

    def __init__(self) -> None:
        self.Q = deque()

    def insert(self, state: Union[int, tuple]):
        self.Q.append(state)

    def get_first(self):
        return self.Q.pop()
    
    def size(self):
        return len(self.Q)
    
    def display(self):
        print(self.Q)