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
        possible_values=sudoku.possible_values_vectorized(cells)
        # Choose the cell that has the least possible values
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
    
