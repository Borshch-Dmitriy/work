from copy import deepcopy


class Atomic:
    def __init__(self, data: list | set | dict, deep: bool = False):
        self._orig = data
        self.deep = deep
        self.data = deepcopy(data) if deep else data.copy()

    def __enter__(self):
        return self.data

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            if isinstance(self._orig, list):
                self._orig[:] = self.data
            else:
                self._orig.clear()
                self._orig.update(self.data)
            return False
        return True

matrix = [[1, 2], [3, 4]]

with Atomic(matrix, True) as atomic:
    atomic[1].append(0)       # изменение вложенной структуры
    atomic.append([5, 6])
    del atomic[100]           # обращение по несуществующему индексу

print(matrix)
