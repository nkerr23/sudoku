# input 9 by 9 array of nums
# 0 = empty space

import sys
import copy

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

# find all possibilities for each square and add to map
def find_possibilities(board):
    map = {}
    for r, row in enumerate(board):
        for c, item in enumerate(row):
            if item == 0:
                coord = (r, c)
                possible_vals = []
                for val in range(1,10):
                    if can_place_val(board, r, c, val):
                        possible_vals.append(val)
                map[coord] = possible_vals
    return map

# take in 9 by 9 array and list of tried squares
def solve_array(board, guessed_boards, index):
    map = find_possibilities(board)

    # check if solved
    if len(map) == 0:
        return board

    # find best possible square to guess for
    sorted_map = sorted(map, key=lambda key: len(map[key]))
    coord = sorted_map[0]
    value = map[coord]
    row = coord[0]
    col = coord[1]

    # check if a square failed i.e. must backtrack
    if len(value) == 0 or len(value) < index+1:
        board, index = guessed_boards.pop()
        return solve_array(board, guessed_boards, index)
    
     # if more than one value, add to guessed_boards for later
    if len(value) > 1:
        new_index = index+1
        guessed_boards.append([board, new_index])

    # try and put a value in the best possible square, return new board
    new_board = copy.deepcopy(board)
    new_board[row][col] = value[index]
    return solve_array(new_board, guessed_boards, 0)

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
    guessed_boards = []
    final = (solve_array(input, guessed_boards, 0))
    print(final)