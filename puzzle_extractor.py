from time import time
from pprint import pprint
from sudoku_solvers import Basic_Backtracker, Backtracker_with_IDR, Backtracker_with_CP, CP_with_MRV
from csv import reader
from random import randint
import statistics


def load_random_puzzle(filename):
    '''Loads a random puzzle from the .csv file'''
    csv_file = open(filename, encoding='utf8')
    csv_reader = reader(csv_file, delimiter=',')
    data = [row for row in csv_reader]
    puzzle_index = randint(0, 2999)
    puzzle_string = data[puzzle_index + 1][2]
    new_puzzle = string_to_puzzle(puzzle_string)
    return new_puzzle


def string_to_puzzle(puzzle_string):
    '''Convert puzzle string to a 2d list'''
    res = [[j for j in range(9)] for i in range(9)]
    count = 0
    for c in puzzle_string:

        if c == '.': res[count // 9][count % 9] = 0
        else: res[count // 9][count % 9] = int(c)
        count += 1
    return res


def read_file(filename, nrows=10):
    '''Converts Data/problems.csv string to a puzzle which is a list of lists'''
    csv_file = open(filename, encoding='utf8')
    csv_reader = reader(csv_file, delimiter=',')
    data = [row for row in csv_reader]

    puzzle_list = []
    puzzle_solns = []

    for i in range(nrows):

        puzzle_string = data[i + 1][2]
        puzzle_soln_string = data[i + 1][3]

        puzzle_list.append(string_to_puzzle(puzzle_string))
        puzzle_solns.append(string_to_puzzle(puzzle_soln_string))

    return puzzle_list, puzzle_solns


def time_solver(obj):
    print("Perfomance report for", obj.__class__.__name__)
    i = 0
    times = []
    for puzzle, soln in zip(puzzles, solns):
        start = time()
        obj.solve_sudoku(puzzle)
        end = time()
        times.append(end - start)
        i += 1
        print(
            f"Time taken for solving puzzle{i}: { round( abs(start - end) ,4 )}",
            end='\r')
        if soln != obj.sudoku_soln:
            print(f"  WRONG")
            return times

    data = {
        "Max": max(times),
        "Min": min(times),
        "Total": sum(times),
        "Mean": statistics.mean(times),
        "Std": statistics.stdev(times)
    }
    print("=" * 76)
    for k, v in data.items():
        print("{}\t :  {}".format(k, v))
    print("\n{:.2f} ± {:.2f}\n".format(data['Mean'], data['Std']))


if __name__ == "__main__":

    #You can change the type of of solver here.
    # The solvers are essentially classes using different algos to solve Sudoku puzzle
    # 1) Basic_Backtracker 2)Backtracker_with_IDR 3)Backtracker_with_CP 4)CP_with_MRV

    for solver in [CP_with_MRV]:
        puzzles, solns = read_file('data/problems.csv', nrows=100)
        time_solver(solver())