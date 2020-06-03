

puzzle1 = [
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

puzzle2 = [
            [5,3,0,0,0,0,0,0,0],
            [6,0,0,1,0,5,0,0,0],
            [0,9,8,0,0,0,0,6,0],
            [0,0,0,0,6,0,0,0,3],
            [4,0,0,8,0,3,0,0,1],
            [7,0,0,0,2,0,0,0,0],
            [0,6,0,0,0,0,2,8,0],
            [0,0,0,4,1,9,0,0,0],
            [0,0,0,0,8,0,0,7,0]
]
from pprint import pprint 

def is_solvable(puzzle,row,col,num):
    #check row
    for no in puzzle[row]:
        if no == num:
            return False
    
    #check col
    for r in range(9):
        if puzzle[r][col] == num:
            return False

    #check box/square
    box_r = ( row// 3 ) * 3
    box_c = (col // 3 ) * 3

    for i in range(box_r,box_r+3):
        for j in range(box_c ,box_c+3):
            if puzzle[i][j] == num:
                return False
    return True

def find_Soln(puzzle):
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                for no in range(1,10):
                    if is_solvable(puzzle,i,j,no):
                        puzzle[i][j] = no
                        find_Soln(puzzle)
                        puzzle[i][j] = 0
                return
    pprint(puzzle)
    input('More?')

if __name__ == "__main__":
    # print( is_solvable( puzzle , 0 ,2 , 1 ) )
    find_Soln(puzzle2)