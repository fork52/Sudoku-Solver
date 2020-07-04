from pprint import pprint 
from sample_puzzles import *
from typing import Iterable
from copy import deepcopy

def is_consistent(puzzle,row,col,num):
    '''Checks alldifferent constraint for box,row and column.'''
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

class basic_Backtracker:
    def __init__(self):
        pass

    def solve_sudoku(self,puzzle):
        '''Wrapper for the Backtracking function.'''
        self.isSolnFound = False
        self.sudoku_soln = None
        self.Backtracking(puzzle)
    
    def Backtracking(self,puzzle):
        for i in range(9):
            for j in range(9):
                if puzzle[i][j] == 0:
                    for no in range(1,10):
                        if is_consistent(puzzle,i,j,no):
                            puzzle[i][j] = no
                            if self.isSolnFound : return
                            self.Backtracking(puzzle)
                            if self.isSolnFound : return
                            puzzle[i][j] = 0
                    return
        self.isSolnFound = True
        self.sudoku_soln = puzzle

class basic_CSP_Initial_Domain:
    '''Basic CSP solver with domain reduction'''
    def __init__(self):
        pass

    def solve_sudoku(self,puzzle):
        '''Wrapper for the basic_CSP_solver function.'''
        self.isSolnFound = False
        self.sudoku_soln = None
        self.var_domains = self.get_puzzle_domains(puzzle)
        self.basic_CSP_solver_with_Initial_RV(puzzle)

    def find_domain(self ,puzzle, row:int , col:int)->set:
        '''Returns the domain of the single empty cell'''
        domain = set( [ i for i in range(1,10)] )

        #check row
        for no in puzzle[row]:
            if no != 0 and no in domain:
                domain.remove(no)
            
        #check col
        for r in range(9):
            if puzzle[r][col] !=0 and  puzzle[r][col] in domain:
                domain.remove(puzzle[r][col])
                
        #check box/square
        box_r = ( row// 3 ) * 3
        box_c = (col // 3 ) * 3
        for i in range(box_r,box_r+3):
            for j in range(box_c ,box_c+3):
                if puzzle[i][j] != 0 and puzzle[i][j] in domain:
                    domain.remove( puzzle[i][j] )
        return domain

    def get_puzzle_domains(self,puzzle:list):
        # -1 indicates that the cell was a part of the original problem
        var_domains = [ [-1 for i in range(9)] for j in range(9)]

        for row in range(9):
            for col in range(9):
                if puzzle[row][col] == 0:
                    var_domains[row][col] = self.find_domain(puzzle, row,col)
        return var_domains 

        
    def basic_CSP_solver_with_Initial_RV(self,puzzle:list ):
        for i in range(9):
            for j in range(9):
                if puzzle[i][j] == 0:
                    for no in self.var_domains[i][j]:
                        if is_consistent(puzzle,i,j,no):
                            puzzle[i][j] = no #Assign the no to the cell
                            self.basic_CSP_solver_with_Initial_RV(puzzle)
                            if self.isSolnFound : return
                            puzzle[i][j] = 0
                    return
        self.isSolnFound = True
        self.sudoku_soln = puzzle
        
class basic_CSP:
    '''Basic CSP solver with domain reduction'''
    def __init__(self):
        pass

    def solve_sudoku(self,puzzle):
        '''Wrapper for the basic_CSP_solver function.'''
        self.isSolnFound = False
        self.sudoku_soln = None
        var_domains = self.get_puzzle_domains(puzzle)
        self.CSP_solver(puzzle ,var_domains)

    def find_domain(self ,puzzle, row:int , col:int)->set:
        '''Returns the domain of the single empty cell'''
        domain = set( [ i for i in range(1,10)] )

        #check row
        for no in puzzle[row]:
            if no != 0 and no in domain:
                domain.remove(no)
            
        #check col
        for r in range(9):
            if puzzle[r][col] !=0 and  puzzle[r][col] in domain:
                domain.remove(puzzle[r][col])
                
        #check box/square
        box_r = ( row// 3 ) * 3
        box_c = (col // 3 ) * 3
        for i in range(box_r,box_r+3):
            for j in range(box_c ,box_c+3):
                if puzzle[i][j] != 0 and puzzle[i][j] in domain:
                    domain.remove( puzzle[i][j] )
        return domain

    def get_puzzle_domains(self,puzzle:list):
        # -1 indicates that the cell was a part of the original problem
        var_domains = [ -1 for i in range(81)]

        for row in range(9):
            for col in range(9):
                if puzzle[row][col] == 0:
                    var_domains[row*9+col] = self.find_domain(puzzle, row,col)
                    if len( var_domains[row*9+col] ) == 0: return False
        return var_domains 

    def reduce_var_domains(self,puzzle:list,row:int , col:int ,var_domains:list):
        no = puzzle[row][col]

        for r in range(9):
            if var_domains[r*9+col] != -1:
                if row != r and no in var_domains[r*9+col]:
                    var_domains[r*9+col] = var_domains[r*9+col].copy()
                    var_domains[r*9+col].remove(no)
                    if len(var_domains[r*9+col]) == 0:
                        return False
        
        for c in range(9):
            if var_domains[row*9+c] != -1:
                if col != c and no in var_domains[row*9+c]:
                    var_domains[row*9+c] = var_domains[row*9+c].copy()
                    var_domains[row*9+c].remove(no)
                    if len(var_domains[row*9+c]) == 0:
                        return False
        
        box_r = ( row// 3 ) * 3
        box_c = (col // 3 ) * 3
        for r in range(box_r,box_r+3):
            for c in range(box_c ,box_c+3):
                if var_domains[r*9+c] != -1:
                    if no in var_domains[r*9+c]:
                        var_domains[r*9+c] = var_domains[r*9+c].copy()
                        var_domains[r*9+c].remove( no )
                        if len(var_domains[r*9+c]) == 0:
                            return False

        return var_domains
       
    def CSP_solver(self,puzzle:list ,var_domains:list):
        for i in range(9):
            for j in range(9):
                if puzzle[i][j] == 0:
                    for no in var_domains[i*9 + j]:
                        if is_consistent(puzzle,i,j,no):

                            puzzle[i][j] = no #Assign the no to the cell

                            new_var_domains = var_domains.copy()
                            new_var_domains[i*9+j] = -1 # it is assigned so domain required 
                            new_var_domains = self.reduce_var_domains(puzzle,i,j,new_var_domains)
                            
                            # Recurse only if all of the domains of un-assigned variables are non-empty 
                            if new_var_domains == False: pass
                            else: self.CSP_solver(puzzle , new_var_domains)
                                
                            if self.isSolnFound : return
                            puzzle[i][j] = 0
                            
                    return
        self.isSolnFound = True
        self.sudoku_soln = puzzle
        
class CSP_with_MRV:
    '''Basic CSP solver with domain reduction and MRV'''
    def __init__(self):
        pass

    def solve_sudoku(self,puzzle):
        '''Wrapper for the basic_CSP_solver function.'''
        self.isSolnFound = False
        self.sudoku_soln = None
        self.get_puzzle_domains(puzzle)
        self.basic_CSP_solver(puzzle)

    def find_domain(self ,puzzle, row:int , col:int)->set:
        '''Returns the domain of the single empty cell'''
        domain = set( [ i for i in range(1,10)] )

        #check row
        for no in puzzle[row]:
            if no != 0 and no in domain:
                domain.remove(no)
            
        #check col
        for r in range(9):
            if puzzle[r][col] !=0 and  puzzle[r][col] in domain:
                domain.remove(puzzle[r][col])
                
        #check box/square
        box_r = ( row// 3 ) * 3
        box_c = (col // 3 ) * 3
        for i in range(box_r,box_r+3):
            for j in range(box_c ,box_c+3):
                if puzzle[i][j] != 0 and puzzle[i][j] in domain:
                    domain.remove( puzzle[i][j] )
        return domain

    def get_puzzle_domains(self,puzzle:list):
        # -1 indicates that the cell was a part of the original problem
        var_domains = [ [-1 for i in range(9)] for j in range(9)]

        for row in range(9):
            for col in range(9):
                if puzzle[row][col] == 0:
                    var_domains[row][col] = self.find_domain(puzzle, row,col)
        self.var_domains = var_domains

    def basic_CSP_solver(self,puzzle:list):
        for i in range(9):
            for j in range(9):
                if puzzle[i][j] == 0:
                    for no in self.var_domains[i][j]:
                        if is_consistent(puzzle,i,j,no):
                            puzzle[i][j] = no
                            if self.isSolnFound : return
                            self.basic_CSP_solver(puzzle)
                            if self.isSolnFound : return
                            puzzle[i][j] = 0
                    return
        self.isSolnFound = True
        self.sudoku_soln = puzzle


if __name__ == "__main__":
    obj = basic_CSP()
    obj.solve_sudoku(puzzle1)
    pprint(obj.sudoku_soln)

    # print( is_solvable( puzzle , 0 ,2 , 1 ) )
    # obj = basic_Backtracker()
    # obj.solve_sudoku(puzzle1)