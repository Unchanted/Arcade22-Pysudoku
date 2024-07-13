from board import Board
from copy import deepcopy

EMPTY = 0
BOARD_DIMENSION = 9
BACKTRACKING = 0

class Solver:
    ''' Solver object that can solve a Sudoku board using specified algorithms. '''

    def __init__(self):
        self.solution = None

    def solve(self, sudoku_board: Board, algorithm=BACKTRACKING) -> Board:
        ''' Solves the Sudoku board using the specified algorithm (default is backtracking). '''
        if algorithm == BACKTRACKING:
            self.solution = self.backtracking(sudoku_board)
        return self.solution

    def backtracking(self, sudoku_board):
        ''' Solves the Sudoku board using the backtracking algorithm. '''
        if sudoku_board.solved():
            return sudoku_board

        board_copy = deepcopy(sudoku_board)

        for i in range(BOARD_DIMENSION):
            for j in range(BOARD_DIMENSION):
                if board_copy.empty_cell(i, j):
                    for number in range(1, BOARD_DIMENSION + 1):
                        if board_copy.valid_move(number, i, j):
                            board_copy.insert(number, i, j)
                            result = self.backtracking(board_copy)
                            if result:
                                return result
                            board_copy.undo(number, i, j)
                    return None  # No valid number found, backtrack

        return None  # No solution found
