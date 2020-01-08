# Created by Oleksandr Sorochynskyi, and Sebastien Meyer
# On 08/01/2020

from copy import deepcopy

def solve_sudoku(sudoku):
    s = deepcopy(sudoku)
    return solve_recursive(s)

def solve_recursive(sudoku):
    if sudoku.is_complete():
        return sudoku
    
    cell = sudoku.empty_cells()[0]
    values = sudoku.possible_values(cell)

    for value in values:
        try:
            sudoku[cell] = value
            return solve_sudoku(sudoku)
        except Exception:
            pass
    raise ValueError("Sudoku does not have a solution")
    
