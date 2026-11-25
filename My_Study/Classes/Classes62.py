class SequenceZip:
    def __init__(self, *args):
        self.sequences = [seq if isinstance(seq, range) else tuple(seq) for seq in args]
        self.len = min((len(i) for i in self.sequences), default=0)

    def __len__(self):
        return self.len

    def __getitem__(self, index):
        return tuple(seq[index] for seq in self.sequences)

    def __iter__(self):
        for i in range(self.len):
            yield self[i]


# TEST_4:
x, y, z = [1, 2, 3], [4, 5, 6], [7, 8, 9]
sequencezip = SequenceZip(x, y, z)

print(sequencezip[2])
x[-1], z[-1] = z[-1], x[-1]
print(sequencezip[2])



# TEST_6:
sequencezip = SequenceZip()
print(len(sequencezip))
print(list(sequencezip))

# TEST_7:
data1 = [1, 2, 3, 4, 5]
data2 = 'abcde'

sequencezip = SequenceZip(data1, data2)
data1.extend([6, 7, 8, 9, 10])
data2 += 'fghij'

print(data1)
print(data2)
print(len(sequencezip))
print(list(sequencezip))
