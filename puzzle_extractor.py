import pandas as pd
import numpy as np
from time import time
from pprint import pprint
from sudoku_solver import basic_Backtracker , basic_CSP ,basic_CSP_Initial_Domain,CSP_with_MRV
from random import randint


def load_random_puzzle(filename):
    '''Loads a random puzzle from the .csv file'''
    df = pd.read_csv(filename)  
    puzzle_index = randint(0,2999)
    puzzle_string = str( df.iat[puzzle_index,1] )
    new_puzzle = string_to_puzzle(puzzle_string) 
    return new_puzzle

def read_file(filename ,nrows=10):
    '''Converts Data/problems.csv string to a puzzle which is a list of lists'''
    puzzle_list = []
    puzzle_solns = []

    df = pd.read_csv(filename)
    for i in range(nrows):
        # index = int( df.iat[i,0] )
        puzzle_string = str( df.iat[i,1] )
        puzzle_soln_string = str( df.iat[i,2] )

        puzzle_list.append (  string_to_puzzle(puzzle_string) )
        puzzle_solns.append (  string_to_puzzle(puzzle_soln_string) )

    return puzzle_list , puzzle_solns

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
    #Load 'nrows' number of sudoku sudoku puzzles
    puzzles , solns = read_file('data/problems.csv', nrows=10)

    #Grand total of the time required to solve all puzzles
    total_time = 0

    #You can change the type of of solver here.
    # The solvers are essentially classes using different algos to solve Sudoku puzzle
    # 1) basic_Backtracker 2)basic_CSP 3)basic_CSP_Initial_Domain 4)CSP_with_MRV
    obj = CSP_with_MRV() 

    #Code for testing the time taken by the chosen solver
    i = 0
    for puzzle,soln in zip( puzzles,solns):
        start = time()
        obj.solve_sudoku(puzzle)
        end = time()
        i += 1 
        print(f"Time taken for solving puzzle{i}: { round( abs(start - end) ,4 )}" , end='')

        if soln == obj.sudoku_soln:
            print(f"  CORRECT")
        else:
            print(f"  WRONG")

        total_time += round( abs(start - end) ,4 )
    print(f"\nTotal time taken for solving all puzzles: {total_time}")
    

    

    
        
