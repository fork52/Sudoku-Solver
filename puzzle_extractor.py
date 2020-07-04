import pandas as pd
import numpy as np
from time import time
from pprint import pprint
from sudoku_solver import basic_Backtracker , basic_CSP

def read_file(filename ,nrows=10):
    '''Converts problems.csv string to a puzzle which is a list of lists'''
    puzzle_list = []

    df = pd.read_csv(filename)
    for i in range(nrows):
        index = int( df.iat[i,0] )
        puzzle_string = str( df.iat[i,1] )
        puzzle_list.append (  string_to_puzzle(puzzle_string) )
    return puzzle_list


def string_to_puzzle(puzzle_string):
    '''Convert puzzle string to a 2d list'''
    res = [[j for j in range(9)] for i in range(9)]
    count = 0
    for c in puzzle_string:
    
        if c == '.':  res[count // 9][count % 9] =  0
        else:          res[count // 9][count % 9] =  int(c)
        count += 1
    return res


if __name__ == "__main__":

    #Load nrows sudoku puzzles
    puzzles = read_file('problems.csv', nrows=10)

    #Grand total of the time required
    total_time = 0
    obj = basic_Backtracker() #You can change the type of of solver here

    i = 0
    for puzzle in puzzles:
        start = time()
        obj.solve_sudoku(puzzle)
        end = time()
        i += 1 
        print(f"Time taken for solving puzzle{i}: { round( abs(start - end) ,4 )}")
        pprint(obj.sudoku_soln)
        total_time += round( abs(start - end) ,4 )
    print(f"\nTotal time taken for solving all puzzles: {total_time}")

    
# if __name__ == "__main__":
#     from sample_puzzles import *

    

    
        
