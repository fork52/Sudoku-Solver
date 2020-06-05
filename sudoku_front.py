# from tkinter import Tk
import tkinter as tk
from tkinter.font import Font

class Board_config:
    def __init__(self):
        self.margin = 40    #top and left margin
        self.box_w = 50     #width of each box
        self.box_space = 2  #box_space
        self.box_w_plus_space = self.box_w + self.box_space
        self.extra_space = 4

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
        callback = root.register(self.only_digits)  # registers a Tcl to Python callback
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


    def create_buttons(self):
        """Render the buttons in the window"""
        self.btn_top_margin = 25    # btn_top_margin
        self.btn_height = 50        
        self.btn_width = 100
        self.btn_space = 40

        #Create the clear button
        clear_btn_left_margin = 100
        clearBtn = tk.Button(self.root , text = 'Clear',command = self.clear_boxes)      
        clearBtn.place(
                        x = clear_btn_left_margin  ,
                        y = self.margin + 9 * (self.box_w_plus_space) + self.btn_top_margin,
                        width=  self.btn_width  , height = self.btn_height,
                    )
                
        #Create the solve button
        solve_btn_left_margin = clear_btn_left_margin + self.btn_width + self.btn_space
        clearBtn = tk.Button(self.root , text = 'Solve')      
        clearBtn.place(
                        x = solve_btn_left_margin  ,
                        y = self.margin + 9 * (self.box_w_plus_space) + self.btn_top_margin,
                        width=  self.btn_width  , height = self.btn_height,
                    )

        #Create the solve button
        Quit_btn_left_margin = clear_btn_left_margin + 2*(self.btn_width + self.btn_space)
        QuitBtn = tk.Button(self.root , text = 'Quit',command = self.root.quit)      
        QuitBtn.place(
                        x = Quit_btn_left_margin  ,
                        y = self.margin + 9 * (self.box_w_plus_space) + self.btn_top_margin,
                        width=  self.btn_width  , height = self.btn_height,
                    )

    def clear_boxes(self):
        "Action for the clear button. Clears the entire grid"
        for i in range(9):
            for j in range(9):
                e = self.squares[(i,j)] #Get the entry object e
                e.delete(first=0,last=2)

    def only_digits(self,P):
        ''' Allow only single non-zero digit or empty string for entries '''
        return (P.isdigit() or P == "") and len(P)<=1 and P!='0'
          
if __name__ == "__main__":

    #Instantiate the window
    window = Board_config()

    root = window.create_root()
    window.create_grid()
    window.create_buttons()

    root.mainloop()