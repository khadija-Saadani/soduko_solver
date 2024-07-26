# 📝 Task-04: Sudoku Solver
A Python program that solves Sudoku puzzles using the backtracking algorithm. This project demonstrates how to use recursive algorithms and constraint validation to solve a classic puzzle game.
## Features
- Solves Sudoku Puzzles: Automatically finds solutions to Sudoku puzzles.
- Backtracking Algorithm: Uses backtracking to explore potential solutions.
- Validates Solutions: Ensures that numbers placed in the Sudoku grid adhere to Sudoku rules.
## How it works
- Initialization: The program starts with an empty or partially filled Sudoku grid.
- Finding an empty cell: It searches for an unoccupied cell in the grid.
- Trying numbers: For each empty cell, the algorithm attempts to fill it with numbers from 1 to 9.
- Checking validity: After placing a number, it checks if the placement is valid according to Sudoku rules (no repetition in row, column, or 3x3 subgrid).
- Recursion: If the number is valid, the function recursively calls itself to fill the next empty cell.
- Backtracking: If no valid number can be placed in a cell, the function removes the previous number, and tries the next possible number.
- Solution found: When all cells are filled with valid numbers, a solution is found, and the process terminates.
  
  ![sodukoo](https://github.com/khadija-Saadani/images/blob/main/sodukoo.png?raw=true)
 ### Helper Functions:
  - solve_sudoku(grid): Recursive function that solves the Sudoku puzzle.
  - is_valid(grid, row, col, num): Checks if placing num at (row, col) is valid according to Sudoku rules.
