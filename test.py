# Created by Oleksandr Sorochynskyi, and Sebastien Meyer
# On 08/01/2020

import time

from sudoku_examples import get_hardest_sudoku, get_sudoku, get_sudoku_solution

from sudoku.sgrid import SudokuGrid
from sudoku.solve import solve_sudoku


hardest_sudoku = get_hardest_sudoku()
solution = solve_sudoku(hardest_sudoku)

