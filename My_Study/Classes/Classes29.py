from random import randint
class Dice:
    '''Dice class'''
    def __init__(self, sides: int):
        self.sides = sides
    def __call__(self) -> int:
        return randint(1, self.sides)


# INPUT DATA:

# TEST_1:
kingdice = Dice(6)

print(kingdice() in [1, 2, 3, 4, 5, 6])
print(kingdice() in [1, 2, 3, 4, 5, 6])
print(kingdice() in [7, 8, 9, 10])

# TEST_2:
kingdice = Dice(2)

print(kingdice() in [1, 2, 3, 4, 5, 6])
print(kingdice() in [3, 4])
print(kingdice() in [7, 8, 9, 10])
