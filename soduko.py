def print_grid(grid):
    #Display the Sudoku grid in an easy-to-read format.
    for row in grid:
        print(" ".join(str(num) if num != 0 else "." for num in row))

def is_valid(grid, row, col, num):
    #Verify if placing a number in a specific position is allowed.
    # Check the row and column
    for i in range(9):
        if grid[row][i] == num or grid[i][col] == num:
            return False
    # Check the 3x3 sub-grid
    start_row, start_col = row - row % 3, col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False
    return True

def solve_sudoku(grid):
    #Solve the Sudoku puzzle using a backtracking approach.
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:  # Look for an empty cell
                for num in range(1, 10):  # Attempt to place digits 1-9
                    if is_valid(grid, row, col, num):
                        grid[row][col] = num
                        if solve_sudoku(grid):
                            return True  # Return True immediately after finding a solution
                        grid[row][col] = 0  # Backtrack
                return False  # If no number works, return False
    return True  # If no empty cells found, puzzle is solved

def main():
    #Main function to run the Sudoku solver.
    # Example Sudoku puzzle (0 indicates empty cells)
    sudoku_grid = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    print("\nInitial Sudoku grid:")
    print_grid(sudoku_grid)

    if solve_sudoku(sudoku_grid):
        print("\nSudoku grid after solving:")
        print_grid(sudoku_grid)
    else:
        print("\nNo solution could be found")

if __name__ == "__main__":
    main()