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
        number_of_rows (int): Number of rows in matrix
        number_of_columns (int): Number of columns in matrix
    """
    def __init__(self, real_numbers: List[List]=None, number_of_rows: int=None, number_of_columns: int=None) -> None:
        """
        Attrs:
            real_numbers (List[List]): Filled matrix, if not defined, zero matrix will be set up
            number_of_rows (int): Number of rows in matrix
            number_of_columns (int): number of columns in matrix
        """
        if real_numbers:
            self._real_numbers = real_numbers
        else:
            self._real_numbers = [[0 for _row in range(number_of_rows)] for _column in range(number_of_columns)]
        self._number_of_rows = len(self._real_numbers)
        self._number_of_columns = len(self._real_numbers[0])

    def __add__(self, other: Matrix) -> Matrix:
        """
        Adds two matrix. To perform matrix addition, two matrices must have the same dimensions.

        Args:
            other(Matrix): Matrix to add to original matrix
        
        Returns:
            Matrix: New matrix, where new elements are sum of elements of two prev matrix.
        """
        eq_for_columns = self._number_of_columns == other._number_of_columns
        eq_for_rows = self._number_of_rows == other._number_of_rows 
        if (eq_for_columns and eq_for_rows):
            return Matrix([
                [self._real_numbers[i][j] + other._real_numbers[i][j]
                for j in range(len(self._real_numbers[0]))]
                for i in range(len(self._real_numbers))
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
        elif self._number_of_columns == multiplier._number_of_rows:
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