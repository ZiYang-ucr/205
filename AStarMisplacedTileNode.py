class AStarMisplacedTileNode:
    def __init__(self, state, parent=None, g=0):
        self.state = state
        self.parent = parent
        self.g = g # Cost from start node to this node
        self.h = self.misplaced_tiles() # Heuristic cost (number of misplaced tiles)
        self.total_cost = self.g + self.h

    def misplaced_tiles(self):
        """
        Calculate the number of misplaced tiles.
        """
        goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
        return sum(1 for i, tile in enumerate(self.state) if tile != 0 and tile != goal_state[i])

    def __lt__(self, other):    
        return self.total_cost < other.total_cost