# Created by Oleksandr Sorochynskyi, and Sebastien Meyer
# On 09/01/2020

import unittest

from sudoku_examples import get_sudoku, get_sudoku_solution

from . import SudokuGrid, solve_sudoku

class TestSudokuGrid(unittest.TestCase):
    def test_empty_grid_is_valid(self):
        sudoku = SudokuGrid([
            [0, 0, 0,  0, 0, 0,  0, 0, 0],
            [0, 0, 0,  0, 0, 0,  0, 0, 0],
            [0, 0, 0,  0, 0, 0,  0, 0, 0],

            [0, 0, 0,  0, 0, 0,  0, 0, 0],
            [0, 0, 0,  0, 0, 0,  0, 0, 0],
            [0, 0, 0,  0, 0, 0,  0, 0, 0],

            [0, 0, 0,  0, 0, 0,  0, 0, 0],
            [0, 0, 0,  0, 0, 0,  0, 0, 0],
            [0, 0, 0,  0, 0, 0,  0, 0, 0]
        ])

    def test_full_sudoku_is_valid(self):
        sudoku = SudokuGrid([
            [8, 6, 4,  3, 7, 1,  2, 5, 9],
            [3, 2, 5,  8, 4, 9,  7, 6, 1],
            [9, 7, 1,  2, 6, 5,  8, 4, 3],
            
            [4, 3, 6,  1, 9, 2,  5, 8, 7],
            [1, 9, 8,  6, 5, 7,  4, 3, 2],
            [2, 5, 7,  4, 8, 3,  9, 1, 6],

            [6, 8, 9,  7, 3, 4,  1, 2, 5],
            [7, 1, 3,  5, 2, 8,  6, 9, 4],
            [5, 4, 2,  9, 1, 6,  3, 7, 8]
        ])

    def test_bad_sudoku_not_valid(self):
        with self.assertRaises(ValueError):
            sudoku = SudokuGrid([
                [1, 1, 1,  1, 1, 1,  1, 1, 1],
                [1, 1, 1,  1, 1, 1,  1, 1, 1],
                [1, 1, 1,  1, 1, 1,  1, 1, 1],

                [1, 1, 1,  1, 1, 1,  1, 1, 1],
                [1, 1, 1,  1, 1, 1,  1, 1, 1],
                [1, 1, 1,  1, 1, 1,  1, 1, 1],

                [1, 1, 1,  1, 1, 1,  1, 1, 1],
                [1, 1, 1,  1, 1, 1,  1, 1, 1],
                [1, 1, 1,  1, 1, 1,  1, 1, 1]
            ])

class TestSudokuSolver(unittest.TestCase):
    def test_solves_sudoku(self):
        test = get_sudoku(1)
        solution = solve_sudoku(test)
        self.assertEqual(solution, get_sudoku_solution(1))