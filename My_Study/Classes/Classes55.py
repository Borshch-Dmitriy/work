class ReversedSequence:
    def __init__(self, sequence):
        self.sequence = sequence

    def __iter__(self):
        return reversed(self.sequence)

    def __len__(self):
        return len(self.sequence)

    def __getitem__(self, index):
        if isinstance(index, int):
            return self.sequence[~index]
        raise IndexError("Index out of range")


# INPUT DATA:

# TEST_1:
reversed_list = ReversedSequence([1, 2, 3, 4, 5])

print(reversed_list[0])
print(reversed_list[1])
print(reversed_list[2])

# TEST_2:
numbers = [1, 2, 3, 4, 5]
reversed_numbers = ReversedSequence(numbers)

print(reversed_numbers[0])
numbers.append(6)
print(reversed_numbers[0])

# TEST_3:
numbers = [1, 2, 3, 4, 5]
reversed_numbers = ReversedSequence(numbers)
print(len(reversed_numbers))

numbers.append(6)
numbers.append(7)
print(len(reversed_numbers))

# TEST_4:
reversed_numbers = ReversedSequence((1, 2, 3, 4, 5))

for num in reversed_numbers:
    print(num)

# TEST_5:
reversed_chars = ReversedSequence('abcde')

for char in reversed_chars:
    print(char)
