class AStarManhattanDistanceNode:
    def __init__(self, state, parent=None, g=0):
        self.state = state
        self.parent = parent
        self.g = g # Cost from start node to this node
        self.h = self.manhattan_distance() # Heuristic cost (Manhattan distance)
        self.total_cost = self.g + self.h

    def manhattan_distance(self):
        goal_positions = {
            1: (0, 0), 2: (0, 1), 3: (0, 2),
            4: (1, 0), 5: (1, 1), 6: (1, 2),
            7: (2, 0), 8: (2, 1), 0: (2, 2)
        }
        distance = 0
        for i, tile in enumerate(self.state):
            if tile != 0:
                goal_x, goal_y = goal_positions[tile] # Get the goal position of the tile
                current_x, current_y = divmod(i, 3) # Get the current position of the tile
                distance += abs(goal_x - current_x) + abs(goal_y - current_y)  # Calculate the Manhattan distance
        return distance        

    def __lt__(self, other):    
        return self.total_cost < other.total_cost