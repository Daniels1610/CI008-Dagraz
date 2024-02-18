from classes.Border import Border # Import required for Jupyter Notebook
# from Border import Border # Import required to perform Unit Testing
import numpy as np
import heapq

class PriorityQueue(Border): # Add (Border) to inherint constructor and methods
    def __init__(self):
        super().__init__()
        self.Q = []

    def put(self, state: tuple, priority: int):
        heapq.heappush(self.Q, (priority, state))

    def get(self):
        return heapq.heappop(self.Q)

    # Pops the smallest value from the Q
    def get_min(self):
        min_idx = np.argmin(self.Q)
        popped_val = self.Q[min_idx]
        del self.Q[min_idx]
        return popped_val
    
    def get_max(self):
        max_idx = np.argmax(self.Q)
        popped_val = self.Q[max_idx]
        del self.Q[max_idx]
        return popped_val