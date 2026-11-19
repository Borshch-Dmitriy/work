from copy import copy


class Peekable:
    def __init__(self, iterable):
        self.iterator = iter(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.iterator)

    def peek(self, default=StopIteration):
        iterator_peek = copy(self.iterator)

        if default != StopIteration:
            return next(iterator_peek, default)

        return next(iterator_peek)
# INPUT DATA:

# TEST_1:
iterator = Peekable('beegeek')

print(next(iterator))
print(next(iterator))
print(*iterator)

# TEST_2:
iterator = Peekable('Python')

print(next(iterator))
print(iterator.peek())
print(iterator.peek())
print(next(iterator))
print(iterator.peek())
print(iterator.peek())
