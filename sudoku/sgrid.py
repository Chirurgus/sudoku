# Created by Oleksandr Sorochynskyi, and Sebastien Meyer
# On 08/01/2020

import numpy as np
from math import floor

class SudokuGrid():
    '''
    Sudoku grid
    '''

    @staticmethod
    def _valid_vector(vector):
        # Filter out any zeros
        vector_nz = vector[np.nonzero(vector)]
        # Check for duplicates
        return len(set(vector_nz.flat)) == len(vector_nz.flat)

    def __init__(self, data):
        self._grid = np.matrix(data)
        if not self._is_valid():
            raise ValueError("Invalid sudoku matrix passed to constructor")
    
    def __str__(self):
        return str(self._grid)

    def __getitem__(self, key):
        return self._grid[key]
    
    def __setitem__(self, key, value):
        if value not in self.possible_values(key).union(set([0])):
            raise ValueError("Invalid value for sudoku")
        self._grid[key] = value
        return self

    def is_complete(self):
        return len(self.empty_cells()) == 0

    def _is_valid(self):
        # Rows
        for i in range(9):
            if not SudokuGrid._valid_vector(self._grid[i,:]):
                return False
        # Columns
        for j in range(9):
            if not SudokuGrid._valid_vector(self._grid[:,j]):
                return False
        # Squares
        for i in range(3):
            for j in range(3):
                i_range = range(i*3, (i+1)*3)
                j_range = range(j*3, (j+1)*3)
                square_range = np.ix_(i_range, j_range)
                if not SudokuGrid._valid_vector(self._grid[square_range]):
                    return False
        return True

    def empty_cells(self):
        ret = []
        for i in range(9):
            for j in range(9):
                if self._grid[i,j] == 0:
                    ret.append((i,j))
        return ret

    def possible_values(self, key):
        i, j = key
        # Ranges for containing square
        i_range = range(floor(i/3)*3, (floor(i/3)+1)*3)
        j_range = range(floor(j/3)*3, (floor(j/3)+1)*3)
        square_range = np.ix_(i_range, j_range)

        row = set(self._grid[i,:].flat)
        column = set(self._grid[:,j].flat)
        square = set(self._grid[square_range].flat)

        candidates = set([ i + 1 for i in range(9) ])
        return candidates.difference(set().union(row, column, square))
         