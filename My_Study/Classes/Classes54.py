    def __iter__(self):
        return self

    def __next__(self):
        if self._n >= self._l:
            self.end += 1
            raise StopIteration

        self._last_element = next(self._iterable)
        self._n += 1

        if self._n == self._l:
            self._is_empty = True

        self._has_last = True
        return self._last_element

    def is_empty(self):
        return self._is_empty

    @property
    def empty_accesses(self):
        return self.end

    @property
    def accesses(self):
        return self._n

    @property
    def first(self):
        if not self._has_first:
            raise AttributeError('Исходный итерируемый объект пуст')
        return self._collection[0]

    @property
    def last(self):
        if not self._has_last:
            raise AttributeError('Последнего элемента нет')
        return self._last_element
