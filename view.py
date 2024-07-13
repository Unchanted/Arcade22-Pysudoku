import tkinter as tk
from board import Board

BG_COLOR = 'white'
DIMENSION = 9
WINDOW_SIZE = 800
WINDOW_OFFSET = 25
BUTTON_WIDTH = 20

LEFT_BUTTON_PADDING = (0, 34)
RIGHT_BUTTON_PADDING = (34, 0)
INNER_BUTTON_PADDING = (34, 34)

class View:

    def __init__(self, sudoku_solver, examples, master):
        ''' Creates a View object that creates an interface using tkinter for the user.
            This view is capable of displaying the board contents, has an example board
            for the user, and also receives an inputted sudoku board. '''
        self.master = master
        self.master.title('Sudoku Solver')
        self.sudoku_solver = sudoku_solver
        self.examples = examples
        self.current_board = None
        
        self._canvas = tk.Canvas(self.master, width = WINDOW_SIZE,
                                 height = WINDOW_SIZE, background = BG_COLOR)                                 
        self._canvas.pack()
        
        self.rectangle_height = (WINDOW_SIZE - WINDOW_OFFSET * 2) / DIMENSION
        self.create_grid()
        self.create_buttons()
        
    def run(self):
        self.master.mainloop()

    def create_grid(self):
        ''' Draws the Sudoku board outline. '''
        # Outlines each 3x3 grid (9 Total)
        for i in range(3):
            for j in range(3):
                x1 = (self.rectangle_height * i * 3) + WINDOW_OFFSET
                y1 = (self.rectangle_height * j * 3) + WINDOW_OFFSET
                x2 = (self.rectangle_height * ((i + 1) * 3 )) + WINDOW_OFFSET
                y2 = (self.rectangle_height * ((j + 1) * 3 )) + WINDOW_OFFSET
                self._canvas.create_rectangle(x1, y1, x2, y2, width = 5)
            
        # Individual Square for each square on the board
        for i in range(DIMENSION):
            for j in range(DIMENSION):
                x1 = (self.rectangle_height * i) + WINDOW_OFFSET
                y1 = (self.rectangle_height * j) + WINDOW_OFFSET
                x2 = (self.rectangle_height * (i + 1)) + WINDOW_OFFSET
                y2 = (self.rectangle_height * (j + 1)) + WINDOW_OFFSET
                self._canvas.create_rectangle(x1, y1, x2, y2, width = 2)

    def create_buttons(self):
        ''' Creates the buttons that are used by the user on the interface. '''
        self._frame = tk.Frame(self.master, bg = BG_COLOR, width=400, height=100)
        self._frame.pack(fill='x')
        
        self.button1 = tk.Button(self._frame, text = "Solve Board", command=self._solve, width = BUTTON_WIDTH)
        self.button1.pack(side='left', padx = LEFT_BUTTON_PADDING)
        
        self.button2 = tk.Button(self._frame, text = "Example Board 1", command=self._board_one, width = BUTTON_WIDTH)
        self.button2.pack(side='left', padx = INNER_BUTTON_PADDING)
        
        self.button3 = tk.Button(self._frame, text = "Input Board", command=self._input_board, width = BUTTON_WIDTH)
        self.button3.pack(side='left', padx = INNER_BUTTON_PADDING)

        self.button4 = tk.Button(self._frame, text = "Reset Board", command=self._reset, width = BUTTON_WIDTH)
        self.button4.pack(side='left', padx = RIGHT_BUTTON_PADDING)

    # Button Commands #
    def _solve(self):
        ''' Solves the current board that the user is requested to be solved. '''
        if self.current_board != None:
            solution = self.sudoku_solver.solve(Board(self.current_board))
            self._canvas.delete(tk.ALL)
            self.create_grid()
            self.current_board = solution.get_board()
            self._draw_board()
            
    def _board_one(self):
        ''' Draws the board one example to the GUI. '''
        self.current_board = self.examples.board_one()
        self._new_board()

    def _input_board(self):
        ''' Need to implement another board example. '''
        #self.current_board = self.examples.board_two()
        self.input_window = tk.Toplevel()
        self.input_window.wm_title("Board Input")

        self.entry_labels = []
        self._draw_entries()
        
        b = tk.Button(self.input_window, text = "Submit Board (MUST BE VALID)", command = self._acquire_input_board)
        b.grid(row = DIMENSION + 2, column = 0, columnspan = 9)

    def _acquire_input_board(self):
        ''' Acquires the input board, destroys the toplevel window and then displays the board to the UI. '''
        self.current_board = self._new_2d_board()
        self.input_window.destroy()
        self._new_board()

    def _new_2d_board(self):
        ''' Initializes a 2d array of the board given the value of the entry labels so that we can display it. '''
        new_board = []

        for i in range(DIMENSION):
            new_row = []
            for j in range(DIMENSION):
                input_value = self.entry_labels[i][j].get()

                if len(input_value) == 0:
                    new_row.append(0)
                else:
                    new_row.append(int(input_value))
            
            new_board.append(new_row)
        
        return new_board
    
