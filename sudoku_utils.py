#Utilities for the front end solver
def only_digits(P):
    ''' Allow only single non-zero digit or empty string for entries '''
    return (P.isdigit() or P == "") and len(P)<=1 and P!='0'

def is_puzzle_valid(puzzle):
    """Check if the entered sudoku puzzle is valid and can be solved"""
    #check rows
    for row in puzzle:
        current_row = set([])
        for no in row:
            if no == 0 : continue
            if ( no  not in current_row ):current_row.add(no)
            else: return False

    for col in range(9):
        current_col = set([])
        for r in range(9):
            no = puzzle[r][col]
            if no == 0: continue
            if ( no not in current_col ):current_col.add(no)
            else: return False

    #Check box
    for i in range(3):
        for j in range(3):
            current_box = set([])
            for r in range(3):
                for c in range(3):
                    no = puzzle[i*3 + r][j*3 + c]
                    if no == 0: continue
                    if ( no not in current_box): current_box.add(no)
                    else: return False

    return True


'''
Some sample sudoku puzzles
'''

puzzle_difficult = [
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,1,0,2],
            [0,0,2,0,3,0,0,4,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,6,0],
            [0,0,0,0,0,0,0,7,0],
            [0,0,0,0,0,0,0,8,0],
            [0,0,0,0,0,0,0,9,0]
]

hardest_sudoku = [
    [8,0,0,0,0,0,0,0,0],
    [0,0,3,6,0,0,0,0,0],
    [0,7,0,0,9,0,2,0,0],
    [0,5,0,0,0,7,0,0,0],
    [0,0,0,0,4,5,7,0,0],
    [0,0,0,1,0,0,0,3,0],
    [0,0,1,0,0,0,0,6,8],
    [0,0,8,5,0,0,0,1,0],
    [0,9,0,0,0,0,4,0,0]]

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

blog_puzzle = [
            [0,6,1,0,0,7,0,0,3],
            [0,9,2,0,0,3,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,8,5,3,0,0,0,0],
            [0,0,0,0,0,0,5,0,4],
            [5,0,0,0,0,8,0,0,0],
            [0,4,0,0,0,0,0,0,1],
            [0,0,0,1,6,0,8,0,0],
            [6,0,0,0,0,0,0,0,0]
]
