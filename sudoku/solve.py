# Created by Oleksandr Sorochynskyi, and Sebastien Meyer
# On 08/01/2020

from copy import deepcopy

def solve_sudoku(sudoku):
    '''
    Solve a sudoku

    :param sudoku: A :class:`SudokuGrid` to be solved
    :returns: A :class:`SudokuGrid` object with solved sudoku.
    '''
    s = deepcopy(sudoku)
    return _solve_recursive(s)

def _solve_recursive(sudoku):
    '''
    Solve a sudoku in-place using a recursive algorithm

    :param sudoku: A :class:`SudokuGrid` to be solved, will be modified.
    :returns: A :class:`SudokuGrid` object with solved sudoku.
    '''
    try :
        cells=sudoku.empty_cells()
        ## Naive way is to take the first empty cell available
        ## cell=cells[0]
        ## Better way (from 12 to 2.5 seconds in average for hardest sudoku):
        ## possible_values=[sudoku.possible_values(c) for c in cells]
        ## With this further optimisation by grouping reusable computation we get almost 10 times faster
        possible_values=sudoku.opt_possible_values_for_multiple_cells(cells)
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
    
