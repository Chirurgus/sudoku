# Created by Oleksandr Sorochynskyi, and Sebastien Meyer
# On 09/01/2020


import linecache

import numpy as np

import sudoku

def _get_sudoku_line(num):
    '''
    Get a practice sudoku with its solution.

    :param num: The numebr of the sudoku to get. Must be in [1,1000000]
    :returns: A 2-tuple of `SudokuGrid` objects containing
              an uncompleted sudoku, and its solution.
    '''
    line = linecache.getline("sudoku_examples/sudoku.csv", num+1)
    quiz_str, solution_str = line.split(",")
    quiz = np.zeros((9, 9), np.int8)
    solution = np.zeros((9, 9), np.int8)
    for i in range(9):
        for j in range(9):
            quiz[i, j] = int(quiz_str[i*9 + j])
            solution[i, j] = int(solution_str[i*9 + j])
    return sudoku.SudokuGrid(quiz), sudoku.SudokuGrid(solution)

def get_sudoku(num):
    '''
    Get a practice sudoku board

    Get one of 1 000 000 pracice sudoku board. The solutions
    are avalable via 'get_sudoku_solution' method.
    :param num: The numebr of the sudoku to get. Must be in [1,1000000]
    :returns: A `SudokuGrid` object containing an uncompleted sudoku.
    '''
    return _get_sudoku_line(num)[0]

def get_sudoku_solution(num):
    '''
    Get a practice sudoku solution

    Get one of 1 000 000 pracice sudoku solutions. The uncompleted sudoku
    are avalable via 'get_sudoku' method.
    :param num: The numebr of the sudoku to get. Must be in [1,1000000]
    :returns: A `SudokuGrid` object containing an complete sudoku.
    '''
    return _get_sudoku_line(num)[1]

def get_hardest_sudoku():
    '''
    Get the hardest sudoku

    :returns: A `SudokuGrid` object containing a (uncomplete) hard sudoku.
    '''
    return sudoku.SudokuGrid(
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

__all__ = ['get_sudoku', 'get_sudoku_solution', 'get_hardest_sudoku']
