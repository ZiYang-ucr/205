class UniformCostNode:
    def __init__(self, state, parent=None, g=0):
        self.state = state
        self.parent = parent
        self.g = g # Cost from start node to this node
        self.h = 0 # Heuristic cost (0 for uniform cost search)
        self.total_cost = self.g + self.h

    def __lt__(self, other):    
        return self.total_cost < other.total_cost