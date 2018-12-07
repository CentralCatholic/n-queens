#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

def clone(board):
    new_board = []
    for i in range(len(board)):
        row = []
        for j in range(len(board)):
            row.append(board[i][j])
        new_board.append(row)
    return new_board

def new_board(n):
    board = []
    for i in range(n):
        board.append(n*[False])
    return board

# does add a queen on this square invalidate
# the chessboard?
def is_valid(board, i, j):
    print 'trying ', i, ', ', j
    # check to see if there are any queens
    # in this row to the left
    row = board[i]
    for has_queen in row[:j]:
        if has_queen:
            return False

    # check to see if there are any queens
    # in this row to the right
    row = board[i]
    for has_queen in row[j+1:]:
        if has_queen:
            return False

    # check to see if there are any queens
    # in this column above
    for row in range(0, i):
        has_queen = board[row][j]
        if has_queen:
            return False

    # check to see if there are any queens
    # in this column from below
    for row in range(i+1, len(board)):
        has_queen = board[row][j]
        if has_queen:
            return False

    for row, col in zip(range(i, -1, -1), range(j,-1, -1)): 
        has_queen = board[row][col]
        if has_queen: 
            return False

    for row, col in zip(range(i, len(board), 1), range(j, len(board), 1)): 
        has_queen = board[row][col]
        if has_queen: 
            return False

    for row, col in zip(range(i, -1, -1), range(j, len(board), 1)): 
        has_queen = board[row][col]
        if has_queen: 
            return False

    for row, col in zip(range(i, len(board), 1), range(j, -1, -1)): 
        has_queen = board[row][col]
        if has_queen: 
            return False
    return True

def solve(board, count):
    n = len(board)
    if n == count:
        return [board]
    solutions = []

    for column in range(n):
        if is_valid(board, count, column):
            # then place the queen on the board
            possible_solution = clone(board)
            possible_solution[count][column] = True
            solutions_for_this_row= solve(clone(possible_solution), count+1)
            solutions = solutions + solutions_for_this_row
    return solutions

def n_queens():
    board = new_board(4)
    solutions = solve(board, 0)
    #for config in solutions:
    #    print_chessboard(config)
    #print len(solutions)
    
def main():
    n_queens()

def print_chessboard(board):
    n = len(board)
    bottom_row = '╚' + (2*n*'═')
    padding = int(math.ceil(math.log10(n))) +1
    preamble = build_preamble(n, board)
    suffix = build_suffix(n)
    print preamble + (padding * ' ') + bottom_row + '\n' + suffix

def build_preamble(n, board):
    preamble = ''
    digits = int(math.ceil(math.log10(n)))
    for i in range(n-1, -1, -1):
        row_contents = build_ith_row(board, i)
        preamble += str(i).center(digits, ' ') + ' ║ ' + row_contents + '\n'
    return preamble

def build_ith_row(board, i):
    row = ''
    for has_queen in board[i]:
        character = '…'
        if has_queen:
            character = '♛'
        row = row + character + ' '
    return row

def build_suffix(n):
    padding = int(math.ceil(math.log10(n))) + 3
    row = ''
    for i in range(n):
        row += str(i) + ' '
    return (padding* ' ') + row

if __name__ == '__main__':
    main()
