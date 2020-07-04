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
    l = [[1,2],[3,4] ]
    k = l.copy()

    l.append([0,0])

    l[0] = 100
    print(k , l)

    # s1 =set ( [1,2] )
    # s2 = s1.copy()
    # s2.add(100)
    # print(s1,s2)
