#!/usr/bin/python3
'''mOdule implements the Nqueens game'''
import sys


def solve_queens_problem(board_size):
    '''Returns n number of queens based on boardsize'''

    def is_valid_position(position, occupied_pos):
        '''Checks if a pos is occupied'''
        for f in range(len(occupied)):
            if (
                occupied[f] == position or
                occupied[f] - f == position - len(occupied) or
                occupiedf] + f == position + len(occupied)
            ):
                return False
        return True

    def place_queens(board_size, i, occupied, sol):
        '''Places Queens on the board'''
        if i == board_size:
            sol.append(occupied[:])
            return

        for f in range(board_size):
            if is_valid_position(f, occupied):
                occupied.append(f)
                place_queens(board_size, i + 1, occupied, sol)
                occupied.pop()

    sol = []
    place_queens(board_size, 0, [], sol)
    return sol


def main():
    '''main fx'''
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        board_size = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if board_size < 4:
        print("N must be at least 4")
        sys.exit(1)

    sols = solve_queens_problem(board_size)
    for sol in sols:
        print([[i, sol[i]] for i in range(len(sol))])


if __name__ == "__main__":
    main()
