class EightPuzzleProblem:
    def __init__(self, initial_state):
        self.initial_state = initial_state
        self.goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0] # Goal state

    def goal_test(self, state):
        """
        Check if the current state is the goal state.
        """
        return state == self.goal_state

    def expand(self, node, NodeClass, heuristic_fn=None):
        moveLists = [(-1, 0), (1, 0), (0, -1), (0, 1)] # Up, Down, Left, Right
        idx = node.state.index(0)
        x,y = divmod (idx, 3) # Get the row and column of the empty space
        neighborList = []
        for dx, dy in moveLists:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 3 and 0 <= new_y < 3: # Check if the new position is within bounds
                new_idx = new_x * 3 + new_y
                new_state = node.state[:]
                new_state[idx], new_state[new_idx] = new_state[new_idx], new_state[idx]
                h = heuristic_fn(new_state) if heuristic_fn else 0 # uniform cost search uses 0
                neighborList.append(NodeClass(new_state, parent=node,g=node.g + 1, h=h)) 
        return neighborList        
            