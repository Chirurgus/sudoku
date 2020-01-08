# Created by Oleksandr Sorochynskyi, and Sebastien Meyer
# On 08/01/2020

from copy import deepcopy

def solve_sudoku(sudoku):
    s = deepcopy(sudoku)
    return solve_recursive(s)

def solve_recursive(sudoku):
    try :
        cells=sudoku.empty_cells()
        ## Naive way was to take the first empty cell available with
        ## cell=cells[0]
        ## Better way (from 12 to 2.5 seconds in average for hardest sudoku):
        possible_values=[sudoku.possible_values(c) for c in cells]
        npv=[len(tpl) for tpl in possible_values]
        cell=cells[npv.index(min(npv))]
    except Exception:
        return sudoku
    
    values = sudoku.possible_values(cell)

    for value in values:
        try:
            sudoku[cell] = value
            return solve_sudoku(sudoku)
        except Exception:
            pass
    raise ValueError("Sudoku does not have a solution")
    
