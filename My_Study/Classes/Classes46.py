class Const:
    def __init__(self,**kwargs):
        self.__dict__.update(kwargs)
    def __setattr__(self, key, value):
        if key not in self.__dict__:
            self.__dict__[key] = value
        else:
            raise AttributeError('Изменение значения атрибута невозможно')
    def __delattr__(self, key):
        raise AttributeError('Удаление атрибута невозможно')

# TEST_4:
person = Const()

person.name = 'Erlich'
person.surname = 'Bachmann'
print(person.name)
print(person.surname)

