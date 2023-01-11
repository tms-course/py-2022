"""Создать класс Матрица который должен иметь следующие переменные:
двумерный массив вещественных чисел; количесство строк и столбцов
в матрице. Класс должен иметь следующие методы: сложение с другой
матрицей; умножение на число; вывод на печать; умножение матриц."""
#import numpy as np



class Matrix(object):
    def __init__(self, matrix: list = [], numb_rows: int=None, numb_columns: int=None) -> None:
        self.matrix = matrix
        self.numb_rows = len(matrix)
        self.numb_columns = len(matrix[0])

    def __add__(self, other):
        other = Matrix(other)
        result = []
        numbers = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                summa = other[i][j] + self.matrix[i][j]
                numbers.append(summa)
                if len(numbers) == len(self.matrix):
                    result.append(numbers)
                    numbers = []
        return Matrix(result)

    def __mul__(self, other):
        length = len(self.matrix) 
        result_matrix = [[0 for i in range(length)] for i in range(length)]
        for i in range(length):
            for j in range(length):
                for k in range(length):
                    result_matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]

    def mul_number_(matrix, n=1):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix [i][j] *= n
        return matrix

""" for row in self.matrix:
        for elem in row:
            print(elem, end=' ')
    print()

или

    print('\n'.join('\t'.join(map(str, row)) for row in matrix))"""




