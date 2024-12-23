# input 9 by 9 array of nums
# 0 = empty space

import sys

# return true if item doesn't exist in row, false otherwise
def check_row (board, row, value):
    for item in board[row]:
        if item == value:
            return False
    return True

# return true if item doesn't exist in col, false otherwise  
def check_column (board, col, value):
    for row in board:
        if row[col] == value:
            return False
    return True

# return true if item doesn't exist in 3x3 square, false otherwise
def check_square (board, row, col, value):
    for i in range((row%3)*3, 3):
        for j in range((col%3)*3, 3):
            if board[i][j] == value:
                return False
    return True

# take in 9 by 9 array
def solve_array (board):
    # create function that adds checks what it can add to the first corner
    return 0

def main():
    # ensure 1 argument
    if (len(sys.argv) != 2):
        sys.exit("Incorrect number of arguments provided")

    # array must be 9x9 for this sudoku solver, return error if incorrect size
    if len(sys.argv[1]) != 9:
        sys.exit("Array is not the correct size, must be 9x9.")
    for item in sys.argv[1]:
        if (len(item) != 9):
            sys.exit("Array is not the correct size, must be 9x9.")
    
    # run solver script
    solve_array(sys.argv[1])

if __name__ == "__main__":
    input = [[0, 0, 0, 0, 1, 0, 0, 0, 0],
             [0, 0, 8, 3, 0, 0, 0, 0, 0],
             [0, 0, 9, 0, 0, 2, 0, 1, 3],
             [2, 0, 0, 0, 4, 0, 7, 0, 0],
             [0, 4, 0, 6, 3, 0, 0, 5, 0],
             [9, 0, 0, 8, 0, 0, 0, 0, 0],
             [0, 6, 0, 0, 0, 0, 0, 0, 1],
             [0, 0, 0, 0, 5, 0, 6, 0, 4],
             [0, 0, 0, 2, 8, 0, 0, 3, 0]]
    solve_array(input)
    
    # main