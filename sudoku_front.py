# from tkinter import Tk
from sudoku_utils import * 
import tkinter as tk
from tkinter.font import Font
import pprint
import time
from tkinter import messagebox
from sudoku_solver import CSP_with_MRV , is_consistent

# TODO - Write a function tp
# TODO - Add buttons for speed-up and speed-down
# TODO - LOOK INTO MORE SOLVING ALGOS
# TODO - Add functionality to navigate using arrows

class Board_config:
    def __init__(self):
        self.margin = 40    #top and left margin
        self.box_w = 50     #width of each box
        self.box_space = 2  #box_space
        self.box_w_plus_space = self.box_w + self.box_space
        self.extra_space = 4

        # The puzzle variable
        # puzzle[0] is the first row
        self.puzzle = [
                        [5,3,0,0,7,0,0,0,0],
                        [6,0,0,1,9,5,0,0,0],
                        [0,9,8,0,0,0,0,6,0],
                        [8,0,0,0,6,0,0,0,3],
                        [4,0,0,8,0,3,0,0,1],
                        [7,0,0,0,2,0,0,0,6],
                        [0,6,0,0,0,0,2,8,0],
                        [0,0,0,4,1,9,0,0,5],
                        [0,0,0,0,8,0,0,7,9]
        ]

    def create_root(self):
        """Set up the window features for tkinter object"""
        root = tk.Tk()
        root.title('Sudoku')
        root.geometry('680x630+350+50') # widthXheight topx+topy
        root.resizable(False, False)
        root.configure(background='black')
        self.root = root
        return root

    def create_grid(self):
        """Render the grid in the window"""
        self.hv15 = Font(family="Helvetica", size=15)
        self.squares = {}
        callback = root.register(only_digits)  # registers a Tcl to Python callback
        for i in range(9):
            for j in range(9):
                if ( (i//3) + (j//3) ) % 2 == 0:
                    color = "#f2b6cb"
                else: color = "#a2bede"
                e = tk.Entry(self.root,justify='center',font = self.hv15,bg = color)

                curr_x = self.margin + i * (self.box_w_plus_space) + (i//3) * self.extra_space
                curr_y = self.margin + j * (self.box_w_plus_space) + (j//3) * self.extra_space


                e.configure(validate="key", validatecommand=(callback, "%P")) 

                e.place(
                        x = curr_x  ,y = curr_y ,
                        width=self.box_w , height = self.box_w,
                    )
                # Store the entry object for further access
                self.squares[(i,j)] = e

    def transfer_board(self):
        "Transfer the puzzle-list to the UI"
        for i in range(9):
            for j in range(9):
                e = self.squares[(i,j)]
                e.delete(0  , 1)
                if self.puzzle[j][i] != 0:
                    e.insert( 0  ,  str(self.puzzle[j][i] ) )

    def update_variable_board(self):
        '''Get the board status in the self.puzzle variable'''
        for i in range(9):
            for j in range(9):
                e = self.squares[(i,j)]
                no = e.get()
                if len(no)== 0:     no = 0
                else:            no = int( e.get() )
                self.puzzle[j][i] = no
        # pprint.pprint(self.puzzle)

    def UpdateEntry(self,i,j):
        #Update the entry/square at location (i,j)
        e = self.squares[(i,j)]
        e.delete(0  , 1)
        if self.puzzle[j][i] != 0:
            e.insert( 0  ,  str(self.puzzle[j][i]) )
        e.update()

    def create_buttons(self):
        """Render the buttons in the window"""
        self.btn_top_margin = 25    # btn_top_margin
        self.btn_height = 50        
        self.btn_width = 100
        self.btn_space = 40

        #Create the clear button
        clear_btn_left_margin = 100
        clearBtn = tk.Button(self.root , text = 'Clear',command = self.clear_board)      
        clearBtn.place(
                        x = clear_btn_left_margin  ,
                        y = self.margin + 9 * (self.box_w_plus_space) + self.btn_top_margin,
                        width=  self.btn_width  , height = self.btn_height,
                    )
                
        #Create the solve button
        solve_btn_left_margin = clear_btn_left_margin + self.btn_width + self.btn_space
        clearBtn = tk.Button(self.root , text = 'SOLVE',command = self.visualize_backtracking_soln)      
        clearBtn.place(
                        x = solve_btn_left_margin  ,
                        y = self.margin + 9 * (self.box_w_plus_space) + self.btn_top_margin,
                        width=  self.btn_width  , height = self.btn_height,

                    )

        #Create the Quit button
        Quit_btn_left_margin = clear_btn_left_margin + 2*(self.btn_width + self.btn_space)
        QuitBtn = tk.Button(self.root , text = 'Quit',command =  self.root.quit)      
        QuitBtn.place(
                        x = Quit_btn_left_margin  ,
                        y = self.margin + 9 * (self.box_w_plus_space) + self.btn_top_margin,
                        width=  self.btn_width  , height = self.btn_height,
                    )
        
        #Create the Instant solve button
        common_right_margin = 20
        common_top_margin = 50
        rBtns_left_margin =  self.margin + 9 * (self.box_w_plus_space) + common_right_margin
        inter_btn_space = 20

        InstantBtn = tk.Button(self.root , text = 'Instant Solve',command = self.instant_soln) #self.root.quit)      
        InstantBtn.place(
                        x = rBtns_left_margin ,
                        y = common_top_margin  ,
                        width=  self.btn_width  , height = self.btn_height,
                    )

    def clear_board(self):
        "Action for the clear button. Clears the entire grid"
        for i in range(9):
            for j in range(9):
                e = self.squares[(i,j)] #Get the entry object e
                e.delete(first=0,last=2)

    def visual_backtracker(self):
        self.transfer_board()
        for i in range(9):
            for j in range(9):
                if self.puzzle[i][j] == 0:
                    for no in range(1,10):
                        if is_consistent(self.puzzle, i,j,no):
                            self.puzzle[i][j] = no
                            self.UpdateEntry(i,j)
                            if self.isSolnFound : return
                            self.visual_backtracker()
                            if self.isSolnFound : return
                            self.puzzle[i][j] = 0
                    return
        # pprint.pprint(self.puzzle)
        self.isSolnFound = True

    def visualize_backtracking_soln(self):
        self.update_variable_board()
        if is_puzzle_valid(self.puzzle):
            self.transfer_board()
            self.isSolnFound = False
            self.visual_backtracker()
        else:
            messagebox.showerror("Error","Invalid Sudoku Puzzle.\nPlease enter valid Puzzle!")

    def visual_CP_solver(self,var_domains:list):
            i ,j = self.MRV_solver.select_Unassigned_var(var_domains)
            if i != -1: 
                for no in var_domains[i*9 + j]:
                    if is_consistent(self.puzzle,i,j,no):

                        self.puzzle[i][j] = no #Assign the no to the cell
                        self.UpdateEntry(i,j)

                        new_var_domains = var_domains.copy()
                        new_var_domains[i*9+j] = -1 # it is assigned so no domain required 
                        new_var_domains = self.MRV_solver.reduce_var_domains(self.puzzle,i,j,new_var_domains)
                        
                        # Recurse only if all of the domains of un-assigned variables are non-empty 
                        if new_var_domains == False: pass
                        else: self.visual_CP_solver(new_var_domains)
                            
                        if self.isSolnFound : return
                        # self.UpdateEntry(i,j)
                        self.puzzle[i][j] = 0  # Un-assign the cell
                        
                return
            self.isSolnFound = True
            pprint.pprint(self.puzzle)

    def visualize_CP_soln(self):
        self.update_variable_board()
        if is_puzzle_valid(self.puzzle):
            self.transfer_board()
            self.isSolnFound = False
            self.MRV_solver = CSP_with_MRV()
            var_domains = self.MRV_solver.get_puzzle_domains(self.puzzle)
            self.visual_CP_solver(var_domains)
        else:
            messagebox.showerror("Error","Invalid Sudoku Puzzle.\nPlease enter valid Puzzle!")

    def instant_soln(self):
        '''Instantly solve the board without visualization'''
        self.update_variable_board()
        if is_puzzle_valid(self.puzzle):
            self.isSolnFound = False
            obj = CSP_with_MRV()   #Create an instance
            obj.solve_sudoku(self.puzzle)  
            self.puzzle = obj.sudoku_soln 
            self.transfer_board() # Transer solution on the grid
        else:
            messagebox.showerror("Error","Invalid Sudoku Puzzle.\nPlease enter valid Puzzle!")
    

if __name__ == "__main__":

    #Instantiate the window
    window = Board_config()

    root = window.create_root()
    window.create_grid()
    window.create_buttons()

    #Mainloop
    root.mainloop()

    