

import heapq
from UniformCostNode import UniformCostNode
from AStarMisplacedTileNode import AStarMisplacedTileNode
from AStartManhattanDistanceNode import AStarManhattanDistanceNode

def enqueue(queue, node):
    for node in queue:
        queue.append(node)
    queue.sort() # Sort the queue based on the total cost
    return queue

def expand(node, NodeClass):
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
            neighborList.append(NodeClass(new_state,node,node.cost + 1)) 
    return neighborList     

def print_solution(node):
    """
    Print the solution path from the root node to the goal node.
    """
    path = []
    while node:
        path.append(node.state)
        node = node.parent
    for state in reversed(path):
        for i in range(0,9,3):
            print(state[i:i+3])
        print()

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
    while queue:
        node = heapq.heappop(queue) # Pop the node with the lowest total cost

        if goal_test(node.state):
            print(f"Solution found! Depth: {node.g}, Nodes expanded: {expanded}, Max queue size: {max_q}")
            return node
        if tuple(node.state) in visited:
            continue   # Skip already visited states
        visited.add(tuple(node.state))
        print(f"Expanding node with state: {node.state}, Cost: {node.g}, Heuristic: {node.h}")
        # print_state(node)
        for i in range(0,9,3):
            print(node.state[i:i+3])
        print()
        if goal_test(node.state):
            print("Goal state reached!")
            return node
        childenodes = expand(node, NodeClass) # Expand the current node
        queueing_function(queue, childenodes) # Enqueue the children nodes
    return None


def main():
    print("Welcome to the Zi's 8 Puzzle Solver!")
    print("Input '1' to use a default sample puzzle ,or '2' to enter your own puzzle.")
    mode = input("Please enter your choice: ")
    default_puzzle = [1,2,3,0,5,6,7,8,4]
    if mode == '1':
        puzzle = default_puzzle
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
        search = general_search(initial_state,enqueue, UniformCostNode)
    elif choice == '2':
        search = general_search(initial_state,enqueue, AStarMisplacedTileNode)
    elif choice == '3':
        search = general_search(initial_state,enqueue, AStarManhattanDistanceNode)
    else:
        print("Invalid choice. Exiting.")
        return

    if search:
        print("Solution found!")
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

if __name__ == "__main__":
    main()    