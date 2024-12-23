# input n by n array of nums
# 0 = empty space

import sys
import copy
import math

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

# return true if item doesn't exist in root(n)xroot(n) square, false otherwise
def check_square (board, row, col, value, n):
    size = int(math.sqrt(n))
    row_start = (row//size)*size
    col_start = (col//size)*size
    for i in range(row_start, row_start+size):
        for j in range(col_start, col_start+size):
            if board[i][j] == value:
                return False
    return True

# return true if can place the num in that square, false otherwise
def can_place_val(board, row, col, value, n):
    if check_row(board, row, value):
        if check_column(board, col, value):
            if check_square(board, row, col, value, n):
                return True
    return False

# find all possibilities for each square and add to map
def find_possibilities(board, n):
    map = {}
    for r, row in enumerate(board):
        for c, item in enumerate(row):
            if item == 0:
                coord = (r, c)
                possible_vals = []
                for val in range(1,n+1):
                    if can_place_val(board, r, c, val, n):
                        possible_vals.append(val)
                map[coord] = possible_vals
    return map

# take in n by n array and list of tried squares
def solve_array(board, guessed_boards, index, n):
    map = find_possibilities(board, n)

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
        return solve_array(board, guessed_boards, index, n)
    
     # if more than one value, add to guessed_boards for later
    if len(value) > 1:
        new_index = index+1
        guessed_boards.append([board, new_index])

    # try and put a value in the best possible square, return new board
    new_board = copy.deepcopy(board)
    new_board[row][col] = value[index]
    return solve_array(new_board, guessed_boards, 0, n)

def main():
    # ensure 1 argument
    if (len(sys.argv) != 2):
        sys.exit("Incorrect number of arguments provided")

    # array must be nxn (n is square) for this sudoku solver, return error if incorrect size
    size = len(sys.argv[1])
    root = math.sqrt(size)
    if not root.is_integer():
        sys.exit("Array size must be a square number.")
    for item in sys.argv[1]:
        if len(item) != size:
            sys.exit("Array must be a square.")
    
    # run solver script
    solve_array(sys.argv[1], [], size)

if __name__ == "__main__":
    main()

'''
input = [[0,0,0,0,1,0,0,0,0],[0,0,8,3,0,0,0,0,0],[0,0,9,0,0,2,0,1,3],[2,0,0,0,4,0,7,0,0],[0,4,0,6,3,0,0,5,0],[9,0,0,8,0,0,0,0,0],[0,6,0,0,0,0,0,0,1],[0,0,0,0,5,0,6,0,4],[0,0,0,2,8,0,0,3,0]]
    
    input2 = [[2, 0, 0, 0],
              [0, 0, 0, 3],
              [4, 0, 0, 0],
              [0, 0, 0, 1]]
    
    #print(can_place_val(input, 0, 0, 4))
    guessed_boards = []
    final = (solve_array(input, guessed_boards, 0, 9))
    print(final)

    #print(check_square(input2, 0, 2, 3, 4))
'''
    
    