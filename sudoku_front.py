# from tkinter import Tk
import tkinter as tk
from tkinter.font import Font

class Board_config:

    def __init__(self):
        self.margin = 40    #top and left margin
        self.box_w = 50     #width of each box
        self.box_space = 5  #box_space
        self.box_w_plus_space = self.box_w + self.box_space

    def create_root(self):
        """Set up the window features for tkinter object"""
        root = tk.Tk()
        root.title('Sudoku')
        root.geometry('600x630+350+50') # widthXheight topx+topy
        root.resizable(False, False)
        root.configure(background='black')
        self.root = root
        return root

    def create_grid(self):
        """Render the grid in the window"""
        self.hv15 = Font(family="Helvetica", size=15)
        self.squares = {}
        for i in range(9):
            for j in range(9):
                e = tk.Entry(self.root,justify='center',font = self.hv15)
                curr_x = board.margin + i * (board.box_w_plus_space) 
                curr_y = board.margin + j * (board.box_w_plus_space) 
                e.place(
                        x = curr_x  ,y = curr_y ,
                        width=board.box_w , height = board.box_w,
                    )
                self.squares[(i,j)] = e

    def create_buttons(self):
        """Render the buttons in the window"""
        self.btnmargin = 10

        clearBtn = tk.Button(self.root , text = 'Clear')      
        clearBtn.place(
                        x = 100  ,
                        y =  board.margin + 9 * (board.box_w_plus_space) + self.btnmargin,
                        width= 130 , height = 50,
                    )


if __name__ == "__main__":

    #Prepare the window
    board = Board_config()
    root = board.create_root()
    board.create_grid()
    board.create_buttons()

    root.mainloop()