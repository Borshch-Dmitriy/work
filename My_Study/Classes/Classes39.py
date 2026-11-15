class RomanNumeral:
    _to_roman_map = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    _values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    def __init__(self, number):
        if isinstance(number, RomanNumeral):
            self.number = number.number
        elif isinstance(number, str):
            self.number = self._from_roman(number)
        else:
            self.number = int(number)

    @classmethod
    def _to_roman(cls, num):
        if not 1 <= num <= 3999:
            return NotImplemented
        result = []
        for value, symbol in cls._to_roman_map:
            count, num = divmod(num, value)
            result.append(symbol * count)
        return ''.join(result)

    @classmethod
    def _from_roman(cls, s):
        s = s.upper()
        total = 0
        for i, ch in enumerate(s):
            if ch not in cls._values:
                return NotImplemented
            value = cls._values[ch]
            if i + 1 < len(s) and cls._values[s[i + 1]] > value:
                total -= value
            else:
                total += value
        if cls._to_roman(total) == s:
            return total
        return NotImplemented

    def __str__(self):
        return self._to_roman(self.number)

    def __int__(self):
        return self.number

    def __add__(self, other):
        return RomanNumeral(self.number + int(other))

    def __sub__(self, other):
        return RomanNumeral(self.number - int(other))

    def _get_val(self, other):
        if isinstance(other, RomanNumeral):
            return other.number
        return None

    def __eq__(self, other):
        val = self._get_val(other)
        if val is None:
            return NotImplemented
        return self.number == val

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        return not result

    def __lt__(self, other):
        val = self._get_val(other)
        if val is None:
            return NotImplemented
        return self.number < val

    def __le__(self, other):
        val = self._get_val(other)
        if val is None:
            return NotImplemented
        return self.number <= val

    def __gt__(self, other):
        val = self._get_val(other)
        if val is None:
            return NotImplemented
        return self.number > val

    def __ge__(self, other):
        val = self._get_val(other)
        if val is None:
            return NotImplemented
        return self.number >= val
# INPUT DATA:

# TEST_1:
number = RomanNumeral('IV') + RomanNumeral('VIII')

print(number)
print(int(number))

# TEST_2:
number = RomanNumeral('X') - RomanNumeral('VI')

print(number)
print(int(number))

# TEST_3:
a = RomanNumeral('X')
b = RomanNumeral('XII')

print(a == b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

# TEST_4:
a = RomanNumeral('X')
b = RomanNumeral('X')

print(a == b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

# TEST_5:
number = RomanNumeral('MXL') + RomanNumeral('MCDVIII') - RomanNumeral('I')

print(number)
print(int(number))

# TEST_6:
number = RomanNumeral('I') + RomanNumeral('II') + RomanNumeral('III') - RomanNumeral('V')

print(number)
print(int(number))

# TEST_7:
romans1 = ['I', 'X', 'L', 'IV', 'IX', 'XLV', 'CXXIV', 'MCMXCIV']
romans2 = ['I', 'V', 'L', 'VI', 'XI', 'XXV', 'CDXLVIII', 'MCMXCI']

for x, y in zip(romans1, romans2):
    number = RomanNumeral(x) + RomanNumeral(y)
    print(number, int(number))

# TEST_8:
romans1 = ['III', 'X', 'L', 'C', 'M', 'XXV', 'XC', 'MMMCMXXXV']
romans2 = ['II', 'V', 'X', 'L', 'D', 'IV', 'VIII', 'MCMXCIV']

for x, y in zip(romans1, romans2):
    number = RomanNumeral(x) - RomanNumeral(y)
    print(number, int(number))

# TEST_9:
romans = ['I', 'IV', 'IX', 'XII', 'XXV', 'XLV', 'LXIX', 'XC', 'CDXLVIII']

for num in romans:
    print(RomanNumeral(num), int(RomanNumeral(num)))

# TEST_10:
roman = RomanNumeral('L')
print(roman.__eq__(1))
print(roman.__ne__(1.1))
print(roman.__gt__(range(5)))
print(roman.__lt__([1, 2, 3]))
print(roman.__ge__({4, 5, 6}))
print(roman.__le__({1: 'one'}))
