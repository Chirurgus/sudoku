# Created by Oleksandr Sorochynskyi, and Sebastien Meyer
# On 08/01/2020

import time

from sudoku_examples import get_hardest_sudoku, get_sudoku, get_sudoku_solution

from sudoku.sgrid import SudokuGrid
from sudoku.solve import solve_sudoku

hardest_sudoku = get_hardest_sudoku()
solution = solve_sudoku(hardest_sudoku)

keys = hardest_sudoku.empty_cells()

# Using the optimized method
before = time.time()
hardest_sudoku.possible_values_vectorized(keys)
after = time.time()

opt_time = after-before

# Using list compact
before = time.time()
[ hardest_sudoku.possible_values(key) for key in keys ]
after = time.time()
list_time = after-before

opt_time
list_time
# bravo
