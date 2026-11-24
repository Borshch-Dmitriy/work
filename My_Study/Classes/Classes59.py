class PermaDict:
    def __init__(self,data = None):
        self.data = dict(data or {})

    def __iter__(self):
        return iter(self.data)

    def __getitem__(self,key):
        return self.data[key]

    def __setitem__(self, key, value):
        if key in self.data:
            raise KeyError('Изменение значения по ключу невозможно')
        self.data[key] = value

    def __delitem__(self, key):
        if key in self.data:
            del self.data[key]

    def __len__(self):
        return len(self.data)

    def keys(self):
        return self.data.keys()

    def values(self):
        return self.data.values()

    def items(self):
        return self.data.items()

# INPUT DATA:

# TEST_1:
permadict = PermaDict({'name': 'Timur', 'city': 'Moscow'})

print(permadict['name'])
print(len(permadict))

# TEST_2:
permadict = PermaDict({'name': 'Timur', 'city': 'Moscow', 'age': 30})

print(*permadict)
print(*permadict.keys())
print(*permadict.values())
print(*permadict.items())

# TEST_3:
permadict = PermaDict()

permadict['name'] = 'Timur'
permadict['age'] = 30
del permadict['name']
print(permadict['age'])
print(len(permadict))
