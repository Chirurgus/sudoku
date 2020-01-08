# Created by Oleksandr Sorochynskyi, and Sebastien Meyer
# On 08/01/2020

import numpy as np
import time
from sudoku.sgrid import SudokuGrid
from sudoku.solve import solve_sudoku

n=100
quizzes = np.zeros((n, 81), np.int32)
solutions = np.zeros((n, 81), np.int32)
for i, line in enumerate(open('sudoku.csv', 'r').read().splitlines()[1:n+1]):
    quiz, solution = line.split(",")
    for j, q_s in enumerate(zip(quiz, solution)):
        q, s = q_s
        quizzes[i, j] = q
        solutions[i, j] = s
quizzes = quizzes.reshape((-1, 9, 9))
solutions = solutions.reshape((-1, 9, 9))

hardest_sudoku = SudokuGrid(
    [[8, 0, 0,  0, 0, 0,  0, 0, 0],
     [0, 0, 3,  6, 0, 0,  0, 0, 0],
     [0, 7, 0,  0, 9, 0,  2, 0, 0],

     [0, 5, 0,  0, 0, 7,  0, 0, 0],
     [0, 0, 0,  0, 4, 5,  7, 0, 0],
     [0, 0, 0,  1, 0, 0,  0, 3, 0],

     [0, 0, 1,  0, 0, 0,  0, 6, 8],
     [0, 0, 8,  5, 0, 0,  0, 1, 0],
     [0, 9, 0,  0, 0, 0,  4, 0, 0]]
)

solution = solve_sudoku(hardest_sudoku)
