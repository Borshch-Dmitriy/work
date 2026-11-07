class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    def name(self):
        return self.name
    def surname(self):
        return self._surname
    def fullname(self):
        return f"{self.name} {self.surname}"
    def fullname_setter(self,value):
        self.name,self.surname = value.split(" ")

    fullname = property(fullname, fullname_setter)

person = Person('Меган', 'Фокс')

print(person.name)
print(person.surname)
print(person.fullname)


person = Person('Джон', 'Маккарти')

person.fullname = 'Алан Тьюринг'
print(person.name)
print(person.surname)
