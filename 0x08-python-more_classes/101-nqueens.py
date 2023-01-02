#!/usr/bin/python3

import sys

def solve_n_queens(n, board, col):
    if col == n:
        """ All queens have been placed. Print the solution."""
        print_board(board)
        return True

    """ Try placing the queen in each row of the current column."""
    for row in range(n):
        if is_safe(board, row, col):
            """ Place the queen and recursively search for a solution."""
            board[row][col] = 1
            if solve_n_queens(n, board, col + 1):
                return True
            """ Backtrack: remove the queen and try the next row."""
            board[row][col] = 0

    return False

def is_safe(board, row, col):
    """ Check if the queen can be placed in the given row and column safely.
     Check each column in the same row."""
    for c in range(col):
        if board[row][c] == 1:
            return False
    """ Check each row in the same column."""
    for r in range(len(board)):
        if board[r][col] == 1:
            return False
    """ Check the diagonal up to the left."""
    r, c = row, col
    while r >= 0 and c >= 0:
        if board[r][c] == 1:
            return False
        r -= 1
        c -= 1
    """ Check the diagonal up to the right."""
    r, c = row, col
    while r >= 0 and c < len(board):
        if board[r][c] == 1:
            return False
        r -= 1
        c += 1
    """ Check the diagonal down to the left."""
    r, c = row, col
    while r < len(board) and c >= 0:
        if board[r][c] == 1:
            return False
        r += 1
        c -= 1
    """ Check the diagonal down to the right."""
    r, c = row, col
    while r < len(board) and c < len(board):
        if board[r][c] == 1:
            return False
        r += 1
        c += 1
    return True

def print_board(board):
    """ Print the board in the required format."""
    for row in board:
        print(" ".join(map(str, row)))

def main(n):
    if not n.isdigit():
        print("N must be a number")
        sys.exit(1)
    n = int(n)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    """ Initialize the board with all positions empty."""
    board = [[0 for _ in range(n)] for _ in range(n)]
    if not solve_n_queens(n, board, 0):
        print("No solutions found")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    main(sys.argv[1])

