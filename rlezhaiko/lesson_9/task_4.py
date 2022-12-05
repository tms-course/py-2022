""" 
4. Создать класс "Матрица", который должен иметь следующие переменные: двумерный
массив вещественных чисел; количество строк и столбцов в матрице. Класс должен
иметь следующие методы: сложение с другой матрицей; умножение на число; вывод на печать; 
умножение матриц.
"""
from __future__ import annotations


class Matrix(object):
    """ 
    Creates an instance of a Matrix class
    """
    def __init__(self, matrix: list = []) -> None:
        """
        :param matrix: list of lists of numbers. Defaults to [].
        """
        self.matrix = matrix
        
    
    def __add__(self, other: Matrix) -> Matrix:
        """
        Addition matrix with matrix
        
        :param other: an instance of a Matrix class
        :returns: return an instance of a Matrix class
        """
        list_tmp, matrix_tmp = [], []
        if self.__row != other.__row and self.__column != other.__column:
            print('Матрицы не могут быть сложены')
        else:
            for i in range(self.__row):
                for j in range(self.__column):
                    list_tmp.append(self.__matrix[i][j] + other.__matrix[i][j])
                matrix_tmp.append(list_tmp)
                list_tmp = []
            return Matrix(matrix_tmp)
    
    
    def __mul__(self, other: Matrix | int | float) -> Matrix | None:
        """
        Multiplication matrix by matrix or matrix by number
        
        :param other: an instance of a Matrix class or integer number or float number
        :returns: return an instance of a Matrix class or None
        """
        summ, list_tmp, matrix_tmp = 0, [], [] 
        if type(other) == Matrix:
            if self.__row != other.__column:
                print('Матрицы не могут быть перемножены.')        
            else:
                for i in range(self.__row):
                    for j in range(other.__column):
                        for k in range(self.__column):
                            summ += self.__matrix[i][k] * other.__matrix[k][j]
                        list_tmp.append(summ)
                        summ = 0
                    matrix_tmp.append(list_tmp)
                    list_tmp = []
                return Matrix(matrix_tmp)
        elif type(other) == int or type(other) == float:
            for row in self.__matrix:
                for column in row:
                    list_tmp.append(column * other)
                matrix_tmp.append(list_tmp)
                list_tmp = []
            return Matrix(matrix_tmp)
        else:
            print('Вы пытаетесь перемножить матрицу не с числом или с другой матрицей!')
    
    
    def __str__(self) -> str:
        """
        :returns: return matrix in string format
        """
        max_length = 0
        for row in self.__matrix:
            for column in row:
                if len(str(column)) > max_length:
                    max_length = len(str(column))
        
        data = ''
        for row in self.__matrix:
            for column in row:
                standart_indent = ' ' * 3
                indent_by_length_element = ' ' * (max_length-len(str(column)))
                data += str(column) + indent_by_length_element + standart_indent
            data += '\n\n'
        data = data.strip()
        return data
    
    
    def get_matrix(self) -> list:
        """
        :returns: return list of list of numbers
        """ 
        return self.__matrix
    
    
    def set_matrix(self, matrix: list) -> None:
        """
        :param matrix: list of lists of numbers
        """
        flag_valid = True
        for row in matrix:
            for column in row:
                if not (type(column) == float or type(column) == int):
                    flag_valid = False
                    break
            
            if not flag_valid:
                print('Вы ввели матрицу не из чисел!')
                break
        
        if flag_valid:      
            self.__matrix = matrix
            self.set_row_count()
            self.set_column_count()
    
    
    def get_row_count(self) -> int:
        """
        :returns: return row count in matrix
        """  
        return self.__row
    
    
    def set_row_count(self) -> None: 
        self.__row = len(self.__matrix)
    
    
    def get_column_count(self) -> int: 
        """
        :returns: return column count in matrix
        """
        return self.__column
    
    
    def set_column_count(self) -> None:
        flag_valid = True
        if self.__matrix == []:
            flag_valid = False
        else:
            column_count = len(self.__matrix[0])
            for row in self.__matrix:
                if len(row) != column_count:
                    print('Вы ввели не матрицу!')
                    flag_valid = False
                    break
        
        if flag_valid:
            self.__column = column_count
        
    
    matrix = property(get_matrix, set_matrix)
    row_count = property(get_row_count, set_row_count)
    column_count = property(get_column_count, set_column_count)    


matrix_1 = [[1, 2, 3], 
            [4, 5, 6], 
            [7, 8, 9]]

matrix_2 = [[9, 8, 7], 
            [6, 5, 4], 
            [3, 2, 1]]

matrix_obj_1 = Matrix(matrix_1)
matrix_obj_2 = Matrix(matrix_2)

matrix_mul_numb = matrix_obj_1 * 3.56
print(str(matrix_mul_numb))

matrix_add = matrix_obj_1 + matrix_obj_2
print(str(matrix_add))

matrix_mul = matrix_obj_1 * matrix_obj_2
print(str(matrix_mul))