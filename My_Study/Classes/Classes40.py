import roman

class RomanNumeral:
    def __init__(self, number):
        if isinstance(number, str):
            self.number = roman.fromRoman(number)
        else:
            self.number = int(number)

    def __str__(self):
        return roman.toRoman(self.number)

    def __int__(self):
        return self.number

    def __add__(self, other):
        return RomanNumeral(self.number + int(other))

    def __sub__(self, other):
        return RomanNumeral(self.number - int(other))

    def _get_val(self, other):
        if isinstance(other, RomanNumeral):
            return other.number
        if isinstance(other, int):
            return other
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

