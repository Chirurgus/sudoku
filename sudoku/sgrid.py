# Created by Oleksandr Sorochynskyi, and Sebastien Meyer
# On 08/01/2020

import numpy as np
from math import floor

class SudokuGrid():
    '''
    Sudoku grid

    A SudokuGrid is always a (potentially valid) sudoku. 
    The validity is checked on creation, and upon any further
    modification.
    
    0 values are taken to be empty cells. All cells should 
    contain number 0-9.
    '''

    @staticmethod
    def _valid_vector(vector):
        '''
        Check if vector consitutes a valid sudoku line/column/square.

        :param vector: A vector 9 of 0-9s (any shape,
                       preferably result of _get_* methods)
        :returns: True if valid sudoku line (no duplicates), False otherwise.
        '''
        # Filter out any zeros
        vector_nz = vector[np.nonzero(vector)]
        # Check for duplicates
        return len(set(vector_nz.flat)) == len(vector_nz.flat)

    def _get_line(self, i):
        '''
        Get sudoku line

        :param i: The line number to get. Must be in [0, 8]
        :returns: A reference to the line 
        '''
        return self._grid[i,:]
    
    def _get_column(self, j):
        '''
        Get sudoku column

        :param i: The column number to get. Must be in [0, 8]
        :returns: A reference to the column 
        '''
        return self._grid[:,j]

    def _get_square(self, i, j):
        '''
        Get sudoku sub-square

        :param i: The line number of the desired square. Must be in [0, 8]
        :param j: The column number of the desired square. Must be in [0, 8]
        :returns: A reference to the square 
        '''
        i_range = range(i*3, (i+1)*3)
        j_range = range(j*3, (j+1)*3)
        square_range = np.ix_(i_range, j_range)
        return self._grid[square_range]

    def __init__(self, data):
        self._grid = np.matrix(data)
        if not self._is_valid():
            raise ValueError("Invalid sudoku matrix passed to constructor")
    
    def __repr__(self):
        return str(self._grid)

    def __getitem__(self, key):
        return self._grid[key]
    
    def __setitem__(self, key, value):
        if value not in self.possible_values(key).union(set([0])):
            raise ValueError("Invalid value for sudoku")
        self._grid[key] = value
        return self

    def _is_valid(self):
        '''
        Check if the sudoku is valid

        :returns: True if sudoku is valid, False otherwise.
        '''
        # Check rows
        for i in range(9):
            if not SudokuGrid._valid_vector(self._grid[i,:]):
                return False
        # Check columns
        for j in range(9):
            if not SudokuGrid._valid_vector(self._grid[:,j]):
                return False
        # Check squares
        for i in range(3):
            for j in range(3):
                i_range = range(i*3, (i+1)*3)
                j_range = range(j*3, (j+1)*3)
                square_range = np.ix_(i_range, j_range)
                if not SudokuGrid._valid_vector(self._grid[square_range]):
                    return False
        return True

    def empty_cells(self):
        '''
        List of empty cell indexes.

        :returns: List of couples (2-tuples) with i,j indexes of empty cells.
        '''
        ret = []
        for i in range(9):
            for j in range(9):
                if self._grid[i,j] == 0:
                    ret.append((i,j))
        return ret

    def possible_values(self, key):
        '''
        List of possible (valid) values for a given cell (key)

        :param key: 2-tuple i,j coordianes of a cell
        :returns: List of possible values for provided cell (1-9).
        '''
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
    
    def opt_possible_values_for_multiple_cells(self, keys):
        '''
        List of possible values for multiple cells (optimized)

        This method is more effiecient than calling 'possible_values'
        multiple times.

        :param keys: List of 2-tuples for indexes
        :returns: List of lists of possible values for provided cells (1-9).
        '''
        result_list=[]
        i_list=[i for (i,j) in keys]
        j_list=[j for (i,j) in keys]
        square_index=[floor(i/3)*3+floor(j/3) for (i,j) in keys]
        rows = [set(self._grid[i,:].flat) for i in range(9)]
        columns = [set(self._grid[:,j].flat) for j in range(9)]
        squares=[set(self._grid[(i*3):((i+1)*3),(j*3):((j+1)*3)].flat) for i in range(3) for j in range(3)]
        candidates = set([ i + 1 for i in range(9) ])
        for i in range(len(keys)):
            result_list.append(candidates.difference(set().union(rows[i_list[i]], columns[j_list[i]], squares[square_index[i]])))
        return result_list
         
