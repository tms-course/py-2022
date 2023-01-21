"""Создать класс Матрица который должен иметь следующие переменные:
двумерный массив вещественных чисел; количесство строк и столбцов
в матрице. Класс должен иметь следующие методы: сложение с другой
матрицей; умножение на число; вывод на печать; умножение матриц."""


from typing import List


class Matrix(object):
    """class represent Matrix
    Attributes:
        matrix (List): matrix
        numb_rows (int): number of rows in matrix
        numb_columns (int): number of columns on matrix
    """
    def __init__(self, matrix: List[List]):
        self.matrix = matrix
        self.numb_rows = len(matrix)
        self.numb_columns = len(matrix[0])

    def __add__(self, other):
        """
        Method add one matrix by another
        Args:
            other: other matrix
        Returns: matrix
        """
        if (self.numb_rows != other.numb_rows or
            self.numb_columns != other.numb_columns):
            print("Матрицы не могут быть сложены")
        for i in range(self.numb_rows):
            for j in range(self.numb_columns):
                self.matrix[i][j] += other.matrix[i][j]
        return Matrix(self.matrix)

    def __mul__(self, other):
        """
        Method that multiplies on matrix by another or one matrix by number
        Args:
            other: matrix or number
        Returns:matrix
        """
        if type(other) == int or type(other) == float:
            for i in range(self.numb_rows):
                for j in range(self.numb_columns):
                    self.matrix[i][j] *= other
            return self.matrix
        else:
            result_matrix = [[0 for _ in range(other.numb_columns)] for _ in range(self.numb_rows)]
            for i in range(self.numb_rows):
                for j in range(other.numb_columns):
                    for k in range(self.numb_columns):
                        result_matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]
            return result_matrix

    def __repr__(self):
        """
        Returns: matrix as a string
        """
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.matrix]))


a = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = Matrix([[11, 12, 13], [14, 15, 16], [17, 18, 19]])

print(a+b)
print(a*5)
print(a*b)







