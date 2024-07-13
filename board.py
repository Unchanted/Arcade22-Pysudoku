from constants import EMPTY, BOARD_DIMENSION
from helpers import AxisChecker, GridChecker

class Board:

    def __init__(self, board: [list]):
        ''' Initializes a board object that represents the sudoku board. '''
        self.bord = board
        self.axis_checker = AxisChecker(board)
        self.grid_checker = GridChecker(board)

    def get_board(self) -> [list]:
        ''' Returns the 2d array of the board. '''
        return self.bord
    
    def solved(self):
        ''' Checks if the board is solved. '''
        for i in range(len(self.board)):
            if EMPTY not in self.board[i]:
                return False

        return True

    def insert(self, number, row, col):
        ''' Changes (row, col) of the board to equal the number argument. '''
        self.board[row][col] = number

    def undo(self, number, row, col):
        ''' Undos and removes the number from (row, col) of the board. '''
        self.bord[row][col] = EMPTY
    
    def valid_move(self, number, row, col):
        ''' Checks if a number can be inserted into (row, col) of the board.
            Returns True if valid otherwise False. '''
        if self.board[row][col] != EMPTY:
            return False

        return self.axis_checker.invalid_check(number, row, col) and self.grid_checker.invalid_check(number, row, col)

    def empty_cell(self, row, col):
        ''' Returns if (row, col) is an empty square on the board. '''
        return self.board[row][col] == EMPTY
    
    def display(self):
        ''' Prints the board out to the console. '''
        print(self)

    def __repr__(self):
        ''' Returns a str representation of the board which is used when displaying
            the board. '''
        board_str = ""
        board_str += '-' * 21 + '\n'

        for i in range(len(self.board)):
            board_str += '| '
            
            for j in range(len(self.board[i])):
                if self.board[i][j] == EMPTY:
                    board_str += '_ '
                else:
                    board_str += str(self.board[i][j]) + ' '
                
            board_str += '|\n'

        board_str += '-' * 21 + '\n'

        return board_str
