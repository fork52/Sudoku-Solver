# Sudoku Solver
**Solving sudoku as a constraint satisfaction problem(CSP).** 

## Description
This repository is an exploration of various algorithms and heuristics which can be used for solving the classic [Sudoku](https://en.wikipedia.org/wiki/Sudoku) puzzle in python. The [sudoku_solver.py](https://github.com/fork52/Sudoku-Solver/blob/master/sudoku_solver.py) has several classes each employing a different strategy for solving the sudkou problem. You can also enjoy the visualization by running the [MAINMENU.py](https://github.com/fork52/Sudoku-Solver/blob/master/MAINMENU.py) file. The GUI has been built using python's inbuilt tkinter library. You can enter your own Sudoku puzzle or load a random puzzle for solving.

## Visualization Demo

<p align="center">
<img src="https://github.com/fork52/Sudoku-Solver/blob/master/readme_resources/Sudoku_demo.gif" width="70%" height="70%">
</p>


## Usage

Use the classes in sudoku_solver.py file to solve sudoku puzzles in the form of 2D lists in python. Currently, the CSP_with_MRV is the most efficient solver of all the classes I have implemented.

1. Create a Sudoku puzzle with blanks marked by 0's:
```python
>>> puzzle = [
...             [5,3,0,0,7,0,0,0,0],
...             [6,0,0,1,9,5,0,0,0],
...             [0,9,8,0,0,0,0,6,0],
...             [8,0,0,0,6,0,0,0,3],
...             [4,0,0,8,0,3,0,0,1],
...             [7,0,0,0,2,0,0,0,6],
...             [0,6,0,0,0,0,2,8,0],
...             [0,0,0,4,1,9,0,0,5],
...             [0,0,0,0,8,0,0,7,9]
... ]
```

2. Import one of the sudoku-solver class and create its object. Call the solve_sudoku() method to solve the puzzle. The solution is stored in the object's `sudoku_soln` attribute. (Note that the pprint has only been used for formatting the list.)
 
```python
>>> from sudoku_solver import CSP_with_MRV 
>>> from pprint import pprint
>>> obj = CSP_with_MRV()
>>> obj.solve_sudoku(puzzle)
>>> pprint(obj.sudoku_soln)
[[5, 3, 4, 6, 7, 8, 9, 1, 2],
 [6, 7, 2, 1, 9, 5, 3, 4, 8],
 [1, 9, 8, 3, 4, 2, 5, 6, 7],
 [8, 5, 9, 7, 6, 1, 4, 2, 3],
 [4, 2, 6, 8, 5, 3, 7, 9, 1],
 [7, 1, 3, 9, 2, 4, 8, 5, 6],
 [9, 6, 1, 5, 3, 7, 2, 8, 4],
 [2, 8, 7, 4, 1, 9, 6, 3, 5],
 [3, 4, 5, 2, 8, 6, 1, 7, 9]]

```


## Credits
* The primary motivation for building this project came from the video [Python Sudoku Solver - Computerphile](https://youtu.be/G_UYXzGuqvM).
* For improving the performance of the algorithms, I have been extemsively referring to this awesome book [Artificial Intelligence: A Modern Approach](http://aima.cs.berkeley.edu/3rd-ed/). 
* The pr

## Future Work

Will be experimenting with some other heuristics as I learn more and I'll be updating the code.


## License
The repository is licensed under MIT License.


<!-- Markdown link & img dfn's -->

