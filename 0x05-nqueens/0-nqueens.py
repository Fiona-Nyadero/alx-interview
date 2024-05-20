#!/usr/bin/python3
'''Module implements the Nqueens puzzle'''
import sys


def is_safe(board, row, col):
    '''Checks if position on board is safe for Queens'''
    for f in range(row):
        if board[f] == col or \
           board[f] - f == col - row or \
           board[f] + f == col + row:
            return False
    return True


def solve_nqueens(board, row, n):
    '''Places n no. of Queens on board recursively'''
    if row == n:
        print_board(board, n)
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(board, row + 1, n)
            board[row] = -1


def print_board(board, n):
    '''Prints out the board with n Queens on stdout'''
    solve = []
    for f in range(n):
        solve.append([f, board[f]])
    print(solve)


def main():
    '''Entry point of the program'''
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be an integer")
        sys.exit(1)

    if n < 4:
        print("N must be 4 and above")
        sys.exit(1)

    board = [-1] * n
    solve_nqueens(board, 0, n)


if __name__ == "__main__":
    main()
