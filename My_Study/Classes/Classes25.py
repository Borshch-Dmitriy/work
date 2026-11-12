class SuperString:

    def __init__(self,string):
        self.string = string

    def __repr__(self):
        return self.string

    def __add__(self, other):
        if isinstance(other, SuperString):
            return SuperString(self.string + other.string)
        return NotImplemented

    def __radd__(self, other):
        return SuperString(self.string + str(other))

    def __mul__(self, other):
        if isinstance(other, int):
            return SuperString(self.string * other)
        return NotImplemented

    def __rmul__(self, other):
        if isinstance(other, int):
            return SuperString(self.string * other)
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, int):
            return SuperString(self.string[:len(self.string) // other])
        return NotImplemented

    def __lshift__(self, other):
        if isinstance(other, int):
            num = len(self.string) - other
            if num >= 0:
                return SuperString(self.string[:num])
            elif num < 0:
                return SuperString(self.string[:0])
        else:
            return NotImplemented

    def __rshift__(self, other):
        if isinstance(other, int):
            return SuperString(self.string[other:])
        return NotImplemented
