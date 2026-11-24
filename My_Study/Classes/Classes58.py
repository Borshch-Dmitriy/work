class OrderedSet:
    def __init__(self,iterable=None):
        if iterable is None:
            self.iterable = []
        else :
            self.iterable = list(dict.fromkeys(iterable))

    def __iter__(self):
        return iter(self.iterable)

    def __len__(self):
        return len(self.iterable)

    def __eq__(self, other):
        if isinstance(other, OrderedSet):
            if len(self) != len(other):
                return False
            return list(self) == list(other)
        if isinstance(other, set):
            if len(self) != len(other):
                return False
            return set(self) == other
        return NotImplemented

    def add(self, item):
        if item not in self.iterable:
            self.iterable.append(item)

    def discard(self, item):
        if item in self.iterable:
            self.iterable.remove(item)

orderedset = OrderedSet()

orderedset.add('green')
orderedset.add('green')
orderedset.add('blue')
orderedset.add('red')
print(*orderedset)
orderedset.discard('blue')
orderedset.discard('white')
print(*orderedset)
