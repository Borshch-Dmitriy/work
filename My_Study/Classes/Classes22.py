class Matrix:
    def __init__(self, rows, cols, value=0):
        self.rows = rows
        self.cols = cols
        self._data = [[value for _ in range(cols)] for _ in range(rows)]

    def get_value(self, row, col):
        return self._data[row][col]

    def set_value(self, row, col, value):
        self._data[row][col] = value

    def __repr__(self):
        return f"Matrix({self.rows}, {self.cols})"

    def __str__(self):
        return '\n'.join(' '.join(str(val) for val in row) for row in self._data)

    def __pos__(self):
        new_m = Matrix(self.rows, self.cols)
        new_m._data = [row[:] for row in self._data]
        return new_m

    def __neg__(self):
        new_m = Matrix(self.rows, self.cols)
        new_m._data = [[-val for val in row] for row in self._data]
        return new_m

    def __invert__(self):
        new_m = Matrix(self.cols, self.rows)
        transposed_data = [[self._data[r][c] for r in range(self.rows)] for c in range(self.cols)]
        new_m._data = transposed_data
        return new_m

    def __round__(self, n=None):
        new_m = Matrix(self.rows, self.cols)
        if n is None:
            new_m._data = [[round(val) for val in row] for row in self._data]
        else:
            new_m._data = [[round(val, n) for val in row] for row in self._data]
        return new_m
