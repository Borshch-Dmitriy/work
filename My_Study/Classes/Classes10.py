class QuadraticPolynomial:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @property
    def x1(self):
        discriminant = self.b**2 - 4 * self.a * self.c
        if discriminant < 0:
            return None
        return (-self.b - discriminant**0.5) / (2 * self.a)

    @property
    def x2(self):
        discriminant = self.b**2 - 4 * self.a * self.c
        if discriminant < 0:
            return None
        return (-self.b + discriminant**0.5) / (2 * self.a)

    @property
    def view(self):
        b_sign = "+" if self.b >= 0 else "-"
        c_sign = "+" if self.c >= 0 else "-"
        return f"{self.a}x^2 {b_sign} {abs(self.b)}x {c_sign} {abs(self.c)}"

    @property
    def coefficients(self):
        return (self.a, self.b, self.c)

    @coefficients.setter
    def coefficients(self, values):
        self.a, self.b, self.c = values

polynom = QuadraticPolynomial(1, 2, -3)

print(polynom.view)
print(polynom.coefficients)
