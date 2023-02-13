"""
4.
Создать класс "Матрица который должен иметь следующие переменные: двумерный массив вещественных чисел;
количество строк и столбцов в матрице. Класс должен иметь следующие методы: сложение с другой матрицей;
умножение на число; вывод на печать; умножение матриц.
"""
from typing import List


class Matrix:
    """
    Class represents matrix
    Attributes:
        List[List] matrix: matrix
        int number_of_rows: number of row in matrix
        int number_of_columns: length of matrix's rows
    """
    matrix: List[List]
    number_of_rows: int
    number_of_columns: int

    def __init__(self, real_number_matrix: List[List]):
        self.matrix = real_number_matrix
        self.number_of_rows = len(real_number_matrix)
        self.number_of_columns = len(real_number_matrix[0])

    def __add__(self, other):
        """
        Method that add to matrix other matrix
        :param other: other matrix
        :return: matrix
        """
        if (self.number_of_columns != other.number_of_columns or
                self.number_of_rows != other.number_of_rows):
            raise ValueError
        for i in range(self.number_of_rows):
            for j in range(self.number_of_columns):
                self.matrix[i][j] += other.matrix[i][j]

        return Matrix(self.matrix)

    def __mul__(self, other):
        """
        Multiplies matrix either with other one or with a constant
        :param other: a constant or another matrix
        :return: new Matrix instance or original matrix if param is a constant
        """
        if type(other) == int or type(other) == float:
            for i in range(self.number_of_rows):
                for j in range(self.number_of_columns):
                    self.matrix[i][j] *= other
            return Matrix(self.matrix)

        new_matrix = [[None for _ in range(other.number_of_columns)] for _ in range(self.number_of_rows)]
        for i in range(self.number_of_rows):
            for j in range(other.number_of_columns):
                new_matrix[i][j] = sum(self.matrix[i][kk] * other.matrix[kk][j] for kk in range(other.number_of_rows))

        return Matrix(new_matrix)

    def __repr__(self):
        """
        represents Matrix output
        :return: Matrix as a string
        """
        string_matrix = ""
        for row in self.matrix:
            string_matrix += "".join(str(row)) + '\n'
        return string_matrix


A = Matrix([[4, 1, 2], [4, 5, 6], [7, 8, 9]])
B = Matrix([[2, 6, 5], [1, 3, 6], [3, 2, 1]])
C = Matrix([[1, 5, 2, 4], [6, 3, 7, 1]])

print(f'Matrix A = {A}')
print(A + B)
print(A * B)
print(A * 2)
print(B + C)
