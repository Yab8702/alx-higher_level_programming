#!/usr/bin/python3
"""Solves the N-queens puzzle"""


import sys


class NQueensSolver:
    """
    NQueensSolver class solves the N Queens problem on an N x N chessboard.
    """

    def __init__(self, board_size):
        """
        Initialize the NQueensSolver object.

        Args:
            board_size (int): The size of the chessboard.
        """
        self.board_size = board_size
        self.solutions = []

    def solve(self):
        """
        Solve the N Queens problem and print the solutions.
        """
        self._recursive_solve([], 0)
        self._print_solutions()

    def _recursive_solve(self, current_solution, row):
        """
        Recursive function to solve the N Queens problem.

        Args:
            current_solution (list): The current partial solution.
            row (int): The current row being considered.

        """
        if row == self.board_size:
            self.solutions.append(current_solution.copy())
        else:
            for col in range(self.board_size):
                if self._is_valid_move(current_solution, row, col):
                    current_solution.append(col)
                    self._recursive_solve(current_solution, row + 1)
                    current_solution.pop()

    def _is_valid_move(self, current_solution, row, col):
        """
        Check if placing a queen at the given position is a valid move.

        Args:
            current_solution (list): The current partial solution.
            row (int): The row to check.
            col (int): The column to check.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        for r, c in enumerate(current_solution):
            if c == col or abs(row - r) == abs(col - c):
                return False
        return True

    def _print_solutions(self):
        """
        Print the solutions to the N Queens problem.
        """
        for solution in self.solutions:
            print(self._format_solution(solution))

    def _format_solution(self, solution):
        """
        Format the solution in the desired format.

        Args:
            solution (list): The solution to format.

        Returns:
            list: The formatted solution.
        """
        formatted_solution = []
        for row, col in enumerate(solution):
            formatted_solution.append([row, col])
        return formatted_solution


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    brd_size = int(sys.argv[1])
    if brd_size < 4:
        print("N must be at least 4")
        sys.exit(1)

    solver = NQueensSolver(brd_size)
    solver.solve()
