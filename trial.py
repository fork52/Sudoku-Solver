# from tkinter import *

# def blink():
#     e.config(bg='green')
#     e.after(1000, lambda: e.config(bg='white')) # after 1000ms

# root = Tk()
# e = Entry(root)
# e.pack()
# b = Button(root, text='blink', command=blink)
# b.pack()
# root.mainloop()

from copy import copy

if __name__ == "__main__":
    # 2d
    l = [ [ set([1,2]) , set([3,4]) ]  ,  [  set([5 ,6 ]) ,set([7,8]) ] ]
    k = l.copy()

    k[0][0] = k[0][0].copy()
    k[0][0] = -1
 
    print( l , k)

    # 1d
    l = [ set([1,2]) , set([3,4])   ,  set([5 ,6 ]) ,set([7,8])  ]
    k = l.copy()

    k[0]= -1
 
    print( l , k)