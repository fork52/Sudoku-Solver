# from tkinter import Tk
import tkinter as tk
from tkinter.font import Font


class Sudoku_grid:
    def __init__(self):
        self.margin = 40
        self.box_w = 50
        self.box_space = 5
        self.box_w_plus_space = self.box_w + self.box_space

if __name__ == "__main__":

    #Prepare the window
    root = tk.Tk()
    root.title('Sudoku')
    root.geometry('600x630+350+50') # widthXheight topx+topy
    root.resizable(False, False)
    root.configure(background='black')

    hv15 = Font(family="Helvetica", size=15)

    grid = Sudoku_grid()

    squares = {}
    for i in range(9):
        for j in range(9):
            e = tk.Entry(root,justify='center',font = hv15)
            curr_x = grid.margin + i * (grid.box_w_plus_space) 
            curr_y = grid.margin + j * (grid.box_w_plus_space) 
            e.place(
                    x = curr_x  ,y = curr_y ,
                    width=grid.box_w , height = grid.box_w,
                )
            squares[(i,j)] = e
    root.mainloop()