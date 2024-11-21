def is_safe(n, x, y, board):
    return 0 <= x < n and 0 <= y < n and board[x][y] == -1

def solve_knights_tour(n, board, x, y, move_x, move_y, movecount):
    if movecount == n * n:
        return True  # All cells visited
    
    # Try all 8 possible moves (Warnsdorff's heuristic could be applied here for efficiency)
    for i in range(8):
        next_x = x + move_x[i]
        next_y = y + move_y[i]

        if is_safe(n, next_x, next_y, board):
            board[next_x][next_y] = movecount

            if solve_knights_tour(n, board, next_x, next_y, move_x, move_y, movecount + 1):
                return True  # If moving to next position leads to a solution, return True
            
            # Backtrack if the move doesn't work
            board[next_x][next_y] = -1
    
    return False  # Return False if no solution found after trying all moves

def knights_tour(n, start_x, start_y):
    board = [[-1]*n for _ in range(n)]  # Initialize board with -1 (unvisited)

    # Possible knight moves (8 possible moves)
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]

    board[start_x][start_y] = 0  # Mark the starting position

    if solve_knights_tour(n, board, start_x, start_y, move_x, move_y, 1):
        for row in board:
            print(" ".join(map(str, row)))
    else:
        print("No Solution Exists")

# Input from the user
n = int(input("Enter the size of the chessboard (N): "))
start_x = int(input("Enter the starting x-coordinate (0 to N-1): "))
start_y = int(input("Enter the starting y-coordinate (0 to N-1): "))

knights_tour(n, start_x, start_y)
