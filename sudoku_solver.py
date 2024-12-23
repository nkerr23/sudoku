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

# return true if can place the num in that square, false otherwise
def can_place_val(board, row, col, value):
    if check_row(board, row, value):
        if check_column(board, col, value):
            if check_square(board, row, col, value):
                return True
    return False

# return the next empty square, if non existent, return None
def find_empty_square(board):
    for r, row in enumerate(board):
        for c, item in enumerate(row):
            if item == 0:
                return [r, c]
    return [None, None]

# try and fill the spot, if can't, return None
def fill_spot(board, row, col):
    for val in range(1,9):
        if can_place_val(board, row, col, val):
            board[row][col] = val
            return board
    return [[None]]

# take in 9 by 9 array
def solve_array(board, filled_squares): # filled squares is a list of filled squares
    cur_board = board
    cur = filled_squares[-1]
    print(cur)
    
    # check if solved
    if cur[0] == None:
        return cur_board
    
    # try and put a value in the next empty square, if works, return new board
    new_board = fill_spot(cur_board, cur[0], cur[1])
    if new_board[0][0] != None:
        new = find_empty_square(cur_board)
        filled_squares.append(new)
        return solve_array(new_board, filled_squares)
    
    # if no value could fit in the current square, try prev square again with new val
    filled_squares.pop()
    return solve_array(cur_board, filled_squares)

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
    input = [
            [0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 8, 3, 0, 0, 0, 0, 0],
            [0, 0, 9, 0, 0, 2, 0, 1, 3],
            [2, 0, 0, 0, 4, 0, 7, 0, 0],
            [0, 4, 0, 6, 3, 0, 0, 5, 0],
            [9, 0, 0, 8, 0, 0, 0, 0, 0],
            [0, 6, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 5, 0, 6, 0, 4],
            [0, 0, 0, 2, 8, 0, 0, 3, 0]]
    
    #print(can_place_val(input, 0, 0, 4))
    first = find_empty_square(input)
    filled_squares = [first]
    final = (solve_array(input, filled_squares))
    print(final)
    
    # main