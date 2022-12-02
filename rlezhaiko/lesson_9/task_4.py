""" 
4. Создать класс "Матрица", который должен иметь следующие переменные: двумерный
массив вещественных чисел; количество строк и столбцов в матрице. Класс должен
иметь следующие методы: сложение с другой матрицей; умножение на число; вывод на печать; 
умножение матриц.
"""
from __future__ import annotations


class Matrix(object):
    """ 
    Class Matrix
    
    Creates an instance of a Matrix class
    """
    def __init__(self, matrix: list = [], rows: int = 0, columns: int = 0) -> None:
        """
        :param matrix: list of lists of numbers. Defaults to [].
        :param rows: row count in matrix. Defaults to 0.
        :param columns: column count in matrix. Defaults to 0.
        """
        self.__matrix = matrix
        self.__row = rows
        self.__column = columns
        
    
    def mul_by_number(self, number: float) -> Matrix:
        """
        Multiplication by number function
        Multiplication all elements of matrix by number
        
        :param number: float number for multiplication matrix
        :returns: return an instance of a Matrix class
        """
        list_tmp, matrix_tmp = [], []
        for row in self.__matrix:
            for column in row:
                list_tmp.append(column * number)
            matrix_tmp.append(list_tmp)
            list_tmp = []
        return Matrix(matrix_tmp)
        
    
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
            obj_tmp = Matrix()
            obj_tmp.set_matrix(matrix_tmp)
            return obj_tmp
    
    
    def __mul__(self, other: Matrix) -> Matrix:
        """
        Multiplication matrix by matrix
        
        :param other: an instance of a Matrix class
        :returns: return an instance of a Matrix class
        """
        summ, list_tmp, matrix_tmp = 0, [], []     
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
            obj_tmp = Matrix()
            obj_tmp.set_matrix(matrix_tmp)
            return obj_tmp
    
    
    def print_matrix(self) -> None:
        """
        Print matrix in human representation
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
        print(data)
    
    
    def get_matrix(self) -> list:
        """
        Getter matrix
        
        :returns: return list of list of numbers
        """ 
        return self.__matrix
    
    
    def set_matrix(self, matrix: list) -> None:
        """
        Setter matrix
        
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
            self.set_count_row()
            self.set_count_column()
    
    
    def get_count_row(self) -> int:
        """
        Getter count row
        
        :returns: return count row in matrix
        """  
        return self.__row
    
    
    def set_count_row(self) -> None: 
        """
        Setter count row
        """
        self.__row = len(self.__matrix)
    
    
    def get_count_column(self) -> int: 
        """
        Getter count column
        
        :returns: return count column in matrix
        """
        return self.__column
    
    
    def set_count_column(self) -> None:
        """
        Setter count column
        """
        flag_valid = True
        column_count = len(self.__matrix[0])
        for row in self.__matrix:
            if len(row) != column_count:
                print('Вы ввели не матрицу!')
                flag_valid = False
                break
        
        if flag_valid:
            self.__column = column_count
        
    
    matrix = property(get_matrix, set_matrix)
    count_row = property(get_count_row, set_count_row)
    count_column = property(get_count_column, set_count_column)    


matrix_1 = [[1, 2, 3], 
            [4, 5, 6], 
            [7, 8, 9]]

matrix_2 = [[9, 8, 7], 
            [6, 5, 4], 
            [3, 2, 1]]

matrix_obj_1 = Matrix()
matrix_obj_2 = Matrix()
matrix_obj_1.set_matrix(matrix_1)
matrix_obj_2.set_matrix(matrix_2)

matr_mul_numb = matrix_obj_1.mul_by_number(3.56)
matr_mul_numb.print_matrix()

matrix_add = matrix_obj_1 + matrix_obj_2
matrix_add.print_matrix()

matrix_mul = matrix_obj_1 * matrix_obj_2
matrix_mul.print_matrix()