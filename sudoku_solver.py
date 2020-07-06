from pprint import pprint 
from typing import Iterable

class Basic_Backtracker:
    '''Class for solving Sudoku puzzles with backtracking'''

    def solve_sudoku(self,puzzle):
        '''Wrapper for the Backtracking function.'''
        self.isSolnFound = False
        self.sudoku_soln = None
        self.recursive_solver(puzzle)
    
    def recursive_solver(self,puzzle):
        for i in range(9):
            for j in range(9):
                if puzzle[i][j] == 0:
                    for no in range(1,10):
                        if self.is_consistent(puzzle,i,j,no):
                            puzzle[i][j] = no
                            if self.isSolnFound : return
                            self.recursive_solver(puzzle)
                            if self.isSolnFound : return
                            puzzle[i][j] = 0
                    return
        self.isSolnFound = True
        self.sudoku_soln = puzzle

    def is_consistent(self,puzzle:list,row:int,col:int,num:int):
        '''Checks Alldifferent constraint for box,row and column of the sudoku puzzle.'''
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

class Backtracker_with_IDR(Basic_Backtracker):
    '''Class for Solving Sudoku with Initial Domain Reduction (IDR) only'''

    def solve_sudoku(self,puzzle):
        '''Wrapper for the basic_CSP_solver function.'''
        self.isSolnFound = False
        self.sudoku_soln = None
        self.var_domains = self.get_puzzle_domains(puzzle)
        self.recursive_solver(puzzle)

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
                
    def recursive_solver(self,puzzle:list ):
        for i in range(9):
            for j in range(9):
                if puzzle[i][j] == 0:
                    for no in self.var_domains[i*9+j]:
                        if self.is_consistent(puzzle,i,j,no):
                            puzzle[i][j] = no #Assign the no to the cell
                            self.recursive_solver(puzzle)
                            if self.isSolnFound : return
                            puzzle[i][j] = 0
                    return
        self.isSolnFound = True
        self.sudoku_soln = puzzle

class Backtracker_with_CP(Backtracker_with_IDR):
    ''''Class for Solving Sudoku with complete Constraint Propagation(CP)'''

    def solve_sudoku(self,puzzle):
        '''Wrapper for the basic_CSP_solver function.'''
        self.isSolnFound = False
        self.sudoku_soln = None
        var_domains = self.get_puzzle_domains(puzzle)
        self.recursive_solver(puzzle ,var_domains)

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
       
    def recursive_solver(self,puzzle:list ,var_domains:list):
        for i in range(9):
            for j in range(9):
                if puzzle[i][j] == 0:
                    for no in var_domains[i*9 + j]:
                        if self.is_consistent(puzzle,i,j,no):

                            puzzle[i][j] = no #Assign the no to the cell

                            new_var_domains = var_domains.copy()
                            new_var_domains[i*9+j] = -1 # it is assigned so domain required 
                            new_var_domains = self.reduce_var_domains(puzzle,i,j,new_var_domains)
                            
                            # Recurse only if all of the domains of un-assigned variables are non-empty 
                            if new_var_domains == False: pass
                            else: self. recursive_solver(puzzle , new_var_domains)
                                
                            if self.isSolnFound : return
                            puzzle[i][j] = 0
                    return
        self.isSolnFound = True
        self.sudoku_soln = puzzle

class CP_with_MRV(Backtracker_with_CP):
    '''Class solver with Minimum Remaining Value (MRV) Heuristic for selecting next varaible to process.'''

    def select_unassigned_var(self,var_domains:list ):
        '''Returns the (row,col) of the element with least no of values in var_domains'''
        min_rv = 100
        min_r , min_c = -1 , -1

        for r in range(9):
            for c in range(9):
                if var_domains[r*9+c] == -1: continue
                current_rv = len(var_domains[r*9+c])

                if current_rv < min_rv and current_rv > 0:
                    min_rv = current_rv
                    min_r , min_c = r , c

        return min_r , min_c

    def recursive_solver(self,puzzle:list ,var_domains:list):
        i ,j = self.select_unassigned_var(var_domains)
        if i != -1: 
            for no in var_domains[i*9 + j]:
                if self.is_consistent(puzzle,i,j,no):

                    puzzle[i][j] = no #Assign the no to the cell

                    new_var_domains = var_domains.copy()
                    new_var_domains[i*9+j] = -1 # it is assigned so domain required 
                    new_var_domains = self.reduce_var_domains(puzzle,i,j,new_var_domains)
                    
                    # Recurse only if all of the domains of un-assigned variables are non-empty 
                    if new_var_domains == False: pass
                    else: self.recursive_solver(puzzle , new_var_domains)
                        
                    if self.isSolnFound : return
                    puzzle[i][j] = 0  # Un-assign the cell
                    
            return
        self.isSolnFound = True
        self.sudoku_soln = puzzle
 


if __name__ == "__main__":
    pass
    
    '''Using the objects of the above classes'''
    # obj = CSP_with_MRV()
    # obj.solve_sudoku(puzzle_d)
    # pprint(obj.sudoku_soln)
