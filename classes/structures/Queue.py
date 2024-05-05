from classes.structures.Border import Border

class Queue(Border):
    def __init__(self):
        super().__init__()

    def get_first(self):
        return self.Q.popleft()