class AttrsIterator:
    def __init__(self,obj):
        self.obj = iter(obj.__dict__.items())
    def __iter__(self):
        yield from self.obj
    def __next__(self):
        for item in self.obj:
            if item:
                return item
        raise StopIteration('Атрибуты закончилис111ь')



# INPUT DATA:

# TEST_1:
class User:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age


user = User('Debbie', 'Harry', 77)
attrsiterator = AttrsIterator(user)

print(*attrsiterator)


# TEST_2:
class User:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
