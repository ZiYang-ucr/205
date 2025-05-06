

import heapq
from UniformCostNode import UniformCostNode
from AStarMisplacedTileNode import AStarMisplacedTileNode
from AStarManhattanDistanceNode import AStarManhattanDistanceNode

def enqueue(queue, children):
    for child in children:
        heapq.heappush(queue, child) # Add the child node to the queue
    return queue

def expand(node, NodeClass):
    moveLists = [(-1, 0), (1, 0), (0, -1), (0, 1)] # Up, Down, Left, Right
    idx = node.state.index(0)
    x,y = divmod (idx, 3) # Get the row and column of the empty space
    neighborList = []
    max_g = node.g 
    for dx, dy in moveLists:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3: # Check if the new position is within bounds
            new_idx = new_x * 3 + new_y
            new_state = node.state[:]
            new_state[idx], new_state[new_idx] = new_state[new_idx], new_state[idx]
            child = NodeClass(new_state, node, node.g + 1) # Create a new child node
            neighborList.append(child) # Add the child node to the neighbor list
            max_g = max(max_g ,child.g) # Update the maximum g value
    return neighborList, max_g     



def goal_test(state):  
    """
    Check if the current state is the goal state.
    """
    return state == [1, 2, 3, 4, 5, 6, 7, 8, 0]

def general_search(initial_state, NodeClass, queueing_function):
    """
    Perform a search using the specified node class and queueing function.
    """
    root = NodeClass(initial_state)
    queue = [root]
    heapq.heapify(queue) # Convert the list to a heap
    max_q = 1 # Initialize max queue size to 1
    expanded = 0
    visited = set()
    max_depth_reached = 0 # Initialize max depth reached to 0
    while queue:
        max_q = max(max_q, len(queue)) # Update the maximum queue size
        node = heapq.heappop(queue) # Pop the node with the lowest total cost
        expanded += 1 # Increment the expanded node count
        
        if goal_test(node.state):
            print(f"Solution found! Depth: {node.g}, Nodes expanded: {expanded}, Max queue size: {max_q}")
            print("Max depth reached:", max_depth_reached)
            return node
        if tuple(node.state) in visited:
            continue   # Skip already visited states
        visited.add(tuple(node.state))
        print(f"Expanding node with state: {node.state}, Cost: {node.g}, Heuristic: {node.h}")
        # print_state(node)
        for i in range(0,9,3):
            print(node.state[i:i+3])
        print()
        childenodes,max_child_g = expand(node, NodeClass) # Expand the current node
        max_depth_reached = max(max_depth_reached, max_child_g) # Update the maximum depth reached
        queueing_function(queue, childenodes) # Enqueue the children nodes

    return None


def main():
    print("Welcome to the Zi's 8 Puzzle Solver!")
    print("Input '1' to use a default sample puzzle ,or '2' to enter your own puzzle.")
    mode = input("Please enter your choice: ")
    default_puzzle = [1,2,3,0,5,6,7,8,4]
    if mode == '1':
        initial_state = default_puzzle
    elif mode == '2':
        initial_state = []
        print("Please enter the puzzle row by row, using 0 for the empty space.")
        for i in range(3):
            row = input(f"Enter row {i+1} (3 numbers separated by spaces): ")
            initial_state.extend(map(int, row.split()))
    else:
        print("Invalid choice. Exiting.")
        return
    print("Select the algorithm to use:")
    print("1. Uniform Cost Search") 
    print("2. A* Search with the Misplaced Tile heuristic")
    print("3. A* Search with the Manhattan Distance heuristic")         
    choice = input("Please enter your choice: ")
    if choice == '1':
        search = general_search(initial_state,UniformCostNode,enqueue)
    elif choice == '2':
        search = general_search(initial_state,AStarMisplacedTileNode,enqueue)
    elif choice == '3':
        search = general_search(initial_state,AStarManhattanDistanceNode,enqueue)
    else:
        print("Invalid choice. Exiting.")
        return

    if search:
        print_solution(search)
    else:
        print("Failed to reach the goal.")


def print_solution(node):
    """
    Print the solution path from the root node to the goal node.
    """
    path = []
    while node:
        path.append(node.state)
        node = node.parent
    print("Solution path:")    
    for state in reversed(path):
        for i in range(0,9,3):
            print(state[i:i+3])
        print()
    print(f"Total moves: {len(path) - 1}") # Exclude the initial state from the move count

if __name__ == "__main__":
    main()    