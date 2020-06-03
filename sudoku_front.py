# from tkinter import Tk
import tkinter as tk

# class Entry(tk.Entry):
#     def __init__(self, master, x, y):
#         tk.Entry.__init__(self, master)

#         self.data = tk.IntVar()
#         self.textvariable = self.data
#         self.grid( column= x*10, row= y*10)
#         # self.place(width=x,height=y)
#         self.config(width=5)
#         self.data.trace('w', self.edit_entry)

#     def edit_entry(self, *args):
#         self.data.set(self.get())

# def print_grid():
#     box_name = 1
#     for x in range(9):
#         for y in range(9):
#             print(boxes[box_name].get(), end=',')
#             box_name += 1
#         print('')

if __name__ == "__main__":
    root = tk.Tk()
    root.title('Sudoku')
    root.geometry('600x630+350+50') # widthXheight topx+topy
    root.resizable(False, False)

    a1 = tk.Entry(root)
    a2 = tk.Entry(root)
    a3 = tk.Entry(root)

    a1.place(x=0,   y=0, width= 45,height=45)
    a2.place(x=40, y=0, width = 45,height=45)
    a3.place(x=90, y=0, width = 45,height=45)

    root.mainloop()