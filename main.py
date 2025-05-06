


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



def main():
    print("Welcome to the Zi's 8 Puzzle Solver!")
    print("Input '1' to use a default sample puzzle ,or '2' to enter your own puzzle.")
    mode = input("Please enter your choice: ")
    default_puzzle = [1,2,3,0,5,6,7,8,4]
    if mode == '1':
        puzzle = default_puzzle
    elif mode == '2':
        puzzle = []
        print("Please enter the puzzle row by row, using 0 for the empty space.")
        for i in range(3):
            row = input(f"Enter row {i+1} (3 numbers separated by spaces): ")
            puzzle.extend(map(int, row.split()))
    else:
        print("Invalid choice. Exiting.")
        return
    print("Select the algorithm to use:")
    print("1. Uniform Cost Search") 
    print("2. A* Search with the Misplaced Tile heuristic")
    print("3. A* Search with the Manhattan Distance heuristic")         
    choice = input("Please enter your choice: ")
    # if choice == '1':
    #     search = UniformCostSearch(puzzle)
    # elif choice == '2':
    #     search = AStarMisplaced(puzzle)
    # elif choice == '3':
    #     search = AStarManhattan(puzzle)
    # else:
    #     print("Invalid choice. Exiting.")
    #     return
    
    # if search.solve():
    #     print("Solution found!")
    #     print_solution(search)
    #     print(f"Solution depth was {node.cost}")
    #     print(f"Number of nodes expanded: {expanded}")
    #     print(f"Max queue size: {max_q}")
    # else:
    #     print("Failed to reach the goal.")

if __name__ == "__main__":
    main()    