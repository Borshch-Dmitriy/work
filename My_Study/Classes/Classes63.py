
class MutableString:
    def __init__(self, string = ''):
        self.string = string

    def lower(self):
        self.string = self.string.lower()
        return self.string

    def upper(self):
        self.string = self.string.upper()
        return self.string

    def __getitem__(self, index):
        if isinstance(index, slice):
            return MutableString(self.string[index])
        return MutableString(self.string[index])
    def __setitem__(self, index, value):
        self.string = list(self.string)
        self.string[index] = value
        self.string = ''.join(self.string)
        return MutableString(self.string)

    def __str__(self):
        return self.string

    def __repr__(self):
        return f"MutableString('{self.string}')"

    def __len__(self):
        return len(self.string)

    def __iter__(self):
        return iter(self.string)

    def  __add__(self, other):
        return MutableString(self.string + other.string)

    def __delitem__(self, index):
        if isinstance(index, slice):
            self.string = list(self.string)
            del self.string[index]
            self.string = ''.join(self.string)
            return MutableString(self.string)


# TEST_12:
mutablestring = MutableString('beegeek')

del mutablestring[2:5]
del mutablestring[1:5:2]
print(mutablestring)

# TEST_13:
mutablestring = MutableString('beegeek')

mutablestring[-1] = 'ee'
print(mutablestring)

mutablestring[-2:] = 'geek'
print(mutablestring)

# TEST_14:
mutablestring = MutableString('beegeek')

del mutablestring[1:3]
print(mutablestring)
