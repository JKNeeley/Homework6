import time

# Define the board as a list of lists
board1 = [
    [0, 0, 1, 0, 0, 2, 0, 0, 0],
    [0, 0, 5, 0, 0, 6, 0, 3, 0],
    [4, 6, 0, 0, 0, 5, 0, 0, 0],
    [0, 0, 0, 1, 0, 4, 0, 0, 0],
    [6, 0, 0, 8, 0, 0, 1, 4, 3],
    [0, 0, 0, 0, 9, 0, 5, 0, 8],
    [8, 0, 0, 0, 4, 9, 0, 5, 0],
    [1, 0, 0, 3, 2, 0, 0, 0, 0],
    [0, 0, 9, 0, 0, 0, 3, 0, 0]
]

board2 = [
    [0, 0, 5, 0, 1, 0, 0, 0, 0],
    [0, 0, 2, 0, 0, 4, 0, 3, 0],
    [1, 0, 9, 0, 0, 0, 2, 6, 0],
    [2, 0, 0, 0, 3, 0, 0, 0, 0],
    [0, 4, 0, 0, 0, 0, 7, 0, 0],
    [5, 0, 0, 0, 0, 7, 0, 1, 0],
    [0, 0, 0, 6, 0, 3, 0, 0, 0],
    [0, 8, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 7, 0, 0, 5, 0]
]

board3 = [
    [6, 7, 0, 0, 0, 0, 0, 0, 0],
    [0, 2, 5, 0, 0, 0, 0, 0, 0],
    [0, 9, 0, 5, 6, 0, 2, 0, 0],
    [3, 0, 0, 0, 8, 0, 9, 0, 0],
    [0, 0, 0, 0, 0, 0, 8, 1, 0],
    [0, 0, 0, 4, 7, 0, 0, 0, 0],
    [0, 0, 8, 6, 0, 3, 0, 9, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0],
    [1, 0, 6, 0, 5, 0, 0, 7, 0]
]

def print_board(board):
    for row in board:
        print(' '.join(map(str, row)))

def is_valid(board, row, col, num):
    # Check if the number is not already in the same row, column, or 3x3 grid
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True

def find_empty_cell(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col
    return None

def mrv_degree_heuristic(board):
    # MRV: Choose the variable with the fewest remaining values (0's)
    min_values = 10
    min_var = None
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                count = sum(1 for num in range(1, 10) if is_valid(board, row, col, num))
                if count < min_values:
                    min_values = count
                    min_var = (row, col)

    # Degree Heuristic: Among variables with the same MRV, choose the one with the most constraints on remaining variables
    max_degree = -1
    selected_var = None
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                if (row, col) == min_var:
                    continue
                count = 0
                for i in range(9):
                    for j in range(9):
                        if board[i][j] == 0:
                            if is_valid(board, row, col, 0) and (i != row or j != col):
                                count += 1
                if count > max_degree:
                    max_degree = count
                    selected_var = (row, col)

    if selected_var:
        return selected_var
    return min_var

def forward_checking(board, row, col, num, domains):
    for i in range(9):
        # Update the domains of variables in the same row and column
        if board[row][i] == 0:
            domains[row][i][num] = False
        if board[i][col] == 0:
            domains[i][col][num] = False

    # Update the domain of variables in the same 3x3 grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == 0:
                domains[i][j][num] = False

def backtracking_search(board):
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return True  # All cells filled, puzzle solved

    row, col = empty_cell

    selected_var = mrv_degree_heuristic(board)
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            forward_checking(board, row, col, num, domains)
            if backtracking_search(board):
                assignments.append((selected_var, sum(1 for num in domains[row][col] if domains[row][col][num]), sum(1 for i in range(9) if board1[row][i] == 0 and any(domains[row][i])), num))
                return True
            board[row][col] = 0  # If the current assignment doesn't lead to a solution, backtrack

    return False  # No valid assignment found

# Initialize the domains for each variable as all numbers from 1 to 9
domains = [[[True] * 10 for _ in range(9)] for _ in range(9)]

start_time = time.time()

assignments = []

# Solve board 1
print("Board 1:")
if backtracking_search(board1):
    print_board(board1)
else:
    print("No solution found for Board 1")
print("Execution time (seconds):", time.time() - start_time)

if len(assignments) >= 4:
    print("First 4 variable assignments:")
    for i in range(4):
        (row, col), domain_size, degree, value = assignments[i]
        print(f"Variable: ({row}, {col}), Domain Size: {domain_size}, Degree: {degree}, Value: {value}")


# Reset the domains for the next board
domains = [[[True] * 10 for _ in range(9)] for _ in range(9)]

start_time = time.time()

assignments = []

# Solve board 2
print("\nBoard 2:")
if backtracking_search(board2):
    print_board(board2) 
else:
    print("No solution found for Board 2")
print("Execution time (seconds):", time.time() - start_time)

if len(assignments) >= 4:
    print("First 4 variable assignments:")
    for i in range(4):
        (row, col), domain_size, degree, value = assignments[i]
        print(f"Variable: ({row}, {col}), Domain Size: {domain_size}, Degree: {degree}, Value: {value}")

# Reset the domains for the next board
domains = [[[True] * 10 for _ in range(9)] for _ in range(9)]

start_time = time.time()

assignments = []

# Solve board 3
print("\nBoard 3:")
if backtracking_search(board3):
    print_board(board3)
else:
    print("No solution found for Board 3")
print("Execution time (seconds):", time.time() - start_time)

if len(assignments) >= 4:
    print("First 4 variable assignments:")
    for i in range(4):
        (row, col), domain_size, degree, value = assignments[i]
        print(f"Variable: ({row}, {col}), Domain Size: {domain_size}, Degree: {degree}, Value: {value}")


### Results ###
# Board 1:
# 3 7 1 4 8 2 6 9 5
# 9 2 5 7 1 6 8 3 4
# 4 6 8 9 3 5 7 1 2
# 5 8 3 1 6 4 9 2 7
# 6 9 2 8 5 7 1 4 3
# 7 1 4 2 9 3 5 6 8
# 8 3 7 6 4 9 2 5 1
# 1 5 6 3 2 8 4 7 9
# 2 4 9 5 7 1 3 8 6
# Execution time (seconds): 0.4250798225402832
# First 4 variable assignments:
# Variable: (8, 8), Domain Size: 8, Degree: 0, Value: 6
# Variable: (8, 8), Domain Size: 7, Degree: 0, Value: 8
# Variable: (8, 7), Domain Size: 10, Degree: 0, Value: 1
# Variable: (8, 5), Domain Size: 8, Degree: 0, Value: 7

# Board 2:
# 4 3 5 2 1 6 8 7 9
# 8 6 2 7 9 4 1 3 5
# 1 7 9 3 8 5 2 6 4
# 2 1 7 4 3 9 5 8 6
# 3 4 8 5 6 1 7 9 2
# 5 9 6 8 2 7 4 1 3
# 7 5 1 6 4 3 9 2 8
# 9 8 3 1 5 2 6 4 7
# 6 2 4 9 7 8 3 5 1
# Execution time (seconds): 0.8206908702850342
# First 4 variable assignments:
# Variable: (8, 8), Domain Size: 9, Degree: 0, Value: 1
# Variable: (8, 8), Domain Size: 9, Degree: 0, Value: 3
# Variable: (8, 6), Domain Size: 7, Degree: 0, Value: 8
# Variable: (8, 5), Domain Size: 10, Degree: 0, Value: 9

# Board 3:
# No solution found for Board 3
# Execution time (seconds): 157.12316417694092
