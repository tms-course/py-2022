class DimentionsMismatch(Exception): ...

class Matrix:
    def __init__(self, n_rows: int, n_cols: int, data: list = list) -> None:
        self._n_cols = n_cols
        self._n_rows = n_rows
        self._data = data if data else [0] * n_rows * n_cols

    def __add__(self, another: 'Matrix') -> 'Matrix':
        if self._n_cols != another._n_cols or self._n_rows != another._n_rows:
            raise DimentionsMismatch()
        
        data = list(map(sum, zip(self._data, another._data)))
        
        return Matrix(self._n_rows, self._n_cols, data)


m1 = Matrix(2, 3, [1, 2, 3, 4])
m2 = Matrix(2, 2, [5, 6, 7, 8])
print((m1 + m2)._data)