class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        else:
            return NotImplemented
    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        else:
            return NotImplemented
    def __mul__(self, other):
        if isinstance(other, int):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return Vector(self.x * other, self.y * other)
        else:
            return NotImplemented
    def __rmul__(self, other):
        if isinstance(other, int):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return Vector(self.x * other, self.y * other)
        else:
            return NotImplemented
    def __truediv__(self, other):
        if isinstance(other, int):
            return Vector(self.x / other, self.y / other)
        else:
            return NotImplemented
