class Numbers:
    def __init__(self):
        self.numbers = []

    def add_number(self,number):
        self.numbers.append(number)

    def get_even(self):
        result = [i for i in self.numbers if i % 2 == 0]
        return result

    def get_odd(self):
        result = [i for i in self.numbers if i % 2 == 1]
        return result

numbers = Numbers()

numbers.add_number(3)
numbers.add_number(2)
numbers.add_number(1)
numbers.add_number(4)

print(numbers.get_even())
print(numbers.get_odd())