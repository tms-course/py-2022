"""
Задание 4.

Создать класс "Матрица который должен иметь следующие переменные: двумерный
массив вещественных чисел; количество строк и столбцов в матрице. Класс должен
иметь следующие методы: сложение с другой матрицей; умножение на число; вывод на
печать; умножение матриц.
"""
from __future__ import annotations
from numbers import Number
from typing import List


class Matrix:
    """
    A classed used to represent a Matrix

    Attributes:
        real_numbers (List[List]): An email of a user
        nrows (int): Number of rows in matrix
        ncol (int): Number of columns in matrix
    """
    def __init__(self, real_numbers: List[List]=None, nrows: int=None, ncols: int=None) -> None:
        """
        Attrs:
            real_numbers (List[List]): Filled matrix, if not defined, zero matrix will be set up
            nrows (int): Number of rows in matrix
            ncol (int): number of columns in matrix
        """
        if real_numbers:
            self._real_numbers = real_numbers
        else:
            self._real_numbers = [[0 for _row in range(nrows)] for _column in range(ncols)]
        self._nrows = len(self._real_numbers)
        self._ncols = len(self._real_numbers[0])

    def __add__(self, other: Matrix) -> Matrix:
        """
        Adds two matrix. To perform matrix addition, two matrices must have the same dimensions.

        Args:
            other(Matrix): Matrix to add to original matrix
        
        Returns:
            Matrix: New matrix, where new elements are sum of elements of two prev matrix.
        """
        eq_for_columns = self._ncols == other._ncols
        eq_for_rows = self._nrows == other._nrows 
        if eq_for_columns and eq_for_rows:
            return Matrix([
                [self._real_numbers[i][j] + other._real_numbers[i][j]
                for j in range(self._ncols)]
                for i in range(self._nrows)
            ])

        print("To perform matrix addition, two matrices must have the same dimensions."
        f"{other._real_numbers} can't be added to {self._real_numbers}.")

    def __mul__(self, multiplier: Matrix | Number) -> Matrix:
        """
        Multiplies origin matrix either on constant or other matrix.
        To perform matrix multiplication matrix A must have number of rows equivalent to number of columns in matrix B.

        Args:
            multiplier(Matrix | Number): Matrix or constant.
        
        Returns:
            Matrix: New matrix, where new elements are result of multiplication.
        """
        if isinstance(multiplier, (int, float)):
            return Matrix([[val * multiplier for val in row] for row in self._real_numbers])
        elif self._ncols == multiplier._nrows:
            return Matrix([
                [sum(i * j for i, j in zip(col, row))
                for col in zip(*multiplier._real_numbers)] 
                for row in self._real_numbers
                ])

        print(f"To perform matrix multiplication, {multiplier._real_numbers} must have number of rows equivalent"
        f" to number of columns in {self._real_numbers}.")
    
    def __str__(self) -> str:
        """Produces matrix output that is intended to be human-readable."""
        return str(self._real_numbers)

    def __repr__(self) -> str:
        """Produces matrix output that is intended to be machine-readeble"""
        return f"{self.__class__}({self._real_numbers})"


A = Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [1, 2, 3, 4]])
B = Matrix([[10, 15, 2, 3], [7, 9, 30, 33], [11, 12, 13, 14], [5, 6, 7, 9]])

print(A + B) # sum of two matrix
print(A * 3) # mul
print(A * B) # multiplication of two matrix
print(f"A={A}; B={B}") # str