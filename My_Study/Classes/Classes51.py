class SkipIterator:
    def __init__(self, iterable, n):
        self.n = n
        self.iterable = iter([x for x in iterable][::self.n+1])
    def __iter__(self):
        yield from self.iterable
    def __next__(self):
        return next(self.iterable)

# INPUT DATA:

# TEST_1:
skipiterator = SkipIterator([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1)   # пропускаем по одному элементу

print(*skipiterator)

# TEST_2:
skipiterator = SkipIterator([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2)   # пропускаем по два элемента

print(*skipiterator)

# TEST_3:
skipiterator = SkipIterator([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0)   # не пропускаем элементы

print(*skipiterator)

# TEST_4:
skipiterator = SkipIterator('abcd', 0)

print(*skipiterator)
