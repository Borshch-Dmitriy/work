class SparseArray:
    def __init__(self, default):
        self.default = default
        self.array = {}
    def __getitem__(self, item):
        if item in self.array:
            return self.array[item]
        else:
            self.array[item] = self.default
            return self.array[item]
    def __setitem__(self, key, value):
        self.array[key] = value
        return self.array[key]



# INPUT DATA:

# TEST_1:
array = SparseArray(0)

array[5] = 1000
array[12] = 1001

print(array[5])
print(array[12])
print(array[13])

# TEST_2:
array = SparseArray(None)

array[0] = 'Timur'
array[1] = 'Arthur'

print(array[0])
print(array[1])
print(array[2])

# TEST_3:
array = SparseArray(None)
print(array[0])
