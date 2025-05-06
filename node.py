class Node:
    def __init__(self, state, parent=None, g=0, heuristic_fn=None):
        self.state = state
        self.parent = parent
        self.g = g # Cost from start node to this node
        self.h = heuristic_fn(state) if heuristic_fn else 0 # Heuristic cost from this node to goal
        self.f = self.g + self.h

    def __lt__(self, other):    
        return self.f < other.f