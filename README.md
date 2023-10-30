# Homework 6

The given code solves Sudoku puzzles using Constraint Satisfaction Problem (CSP) techniques, particularly backtracking search with Minimum Remaining Values (MRV) and Degree Heuristic, as well as forward checking. 

## CSP Problem Formulation: 

### Variables: 
Each variable corresponds to a cell in the Sudoku board. The variables are represented as a pair (row, col) to identify the position of the cell in the grid.

### Domains: 
The domain for each variable is the set of numbers from 1 to 9, representing the possible values that can be assigned to a cell.

### Constraints: 
- All different values within the same row.
- All different values within the same column.
- All different values within the same 3x3 subgrid.

## Implementation of Forward Checking:
The forward_checking function is used to perform forward checking after assigning a value to a variable. It updates the domains for other variables by marking the assigned value as unavailable in the same row, column, and 3x3 grid.

## Implementation of Backtracking Search with MRV and Degree Heuristic:

### MRV (Minimum Remaining Values): 
This heuristic selects the variable with the fewest remaining values (0's) in its domain. In the code, mrv_degree_heuristic function finds the variable with the MRV heuristic.

### Degree Heuristic: 
Among variables with the same MRV, this heuristic selects the one with the most constraints on the remaining variables. In the code, it is implemented within the mrv_degree_heuristic function.

### Backtracking Search: 
The main solving function is backtracking_search. It recursively tries to assign values to variables following the MRV and Degree Heuristic. It also uses forward checking to reduce the domains of other variables when an assignment is made. If it reaches a solution or finds an inconsistency, it backtracks.

## Execution:
The code solves three Sudoku puzzles (board1, board2, and board3) using the backtracking search algorithm with the specified heuristics and forward checking. It prints the solved Sudoku grids if a solution is found and provides the execution time. Additionally, it records the first four variable assignments, including the variable position, domain size, degree, and assigned value.

## Results

### Board 1:
3 7 1 4 8 2 6 9 5 <br>
9 2 5 7 1 6 8 3 4 <br>
4 6 8 9 3 5 7 1 2 <br>
5 8 3 1 6 4 9 2 7 <br>
6 9 2 8 5 7 1 4 3 <br>
7 1 4 2 9 3 5 6 8 <br>
8 3 7 6 4 9 2 5 1 <br>
1 5 6 3 2 8 4 7 9 <br>
2 4 9 5 7 1 3 8 6 <br>
- Execution time (seconds): 0.4250798225402832
- First 4 variable assignments:
-- Variable: (8, 8), Domain Size: 8, Degree: 0, Value: 6
-- Variable: (8, 8), Domain Size: 7, Degree: 0, Value: 8
-- Variable: (8, 7), Domain Size: 10, Degree: 0, Value: 1
-- Variable: (8, 5), Domain Size: 8, Degree: 0, Value: 7

### Board 2:
4 3 5 2 1 6 8 7 9 <br>
8 6 2 7 9 4 1 3 5 <br>
1 7 9 3 8 5 2 6 4 <br>
2 1 7 4 3 9 5 8 6 <br>
3 4 8 5 6 1 7 9 2 <br>
5 9 6 8 2 7 4 1 3 <br>
7 5 1 6 4 3 9 2 8 <br>
9 8 3 1 5 2 6 4 7 <br>
6 2 4 9 7 8 3 5 1 <br>
- Execution time (seconds): 0.8206908702850342
- First 4 variable assignments:
-- Variable: (8, 8), Domain Size: 9, Degree: 0, Value: 1
-- Variable: (8, 8), Domain Size: 9, Degree: 0, Value: 3
-- Variable: (8, 6), Domain Size: 7, Degree: 0, Value: 8
-- Variable: (8, 5), Domain Size: 10, Degree: 0, Value: 9

Board 3:
- No solution found for Board 3
- Execution time (seconds): 157.12316417694092
