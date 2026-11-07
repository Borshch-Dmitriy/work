class User:
    def __init__(self, name, age):
        if isinstance(name, str) and name.isalpha():
            self._name = name
        else:
            raise ValueError('Некорректное имя')
        if isinstance(age, int) and 0 < age < 110:
            self._age = age
        else:
            raise ValueError('Некорректный возраст')
    def get_name(self):
        return self._name
    def set_name(self, name):
        if isinstance(name, str) and name.isalpha():
            self._name = name
        else:
            raise ValueError('Некорректное имя')
    def get_age(self):
        return self._age
    def set_age(self, age):
        if isinstance(age, int) and 0 < age < 110:
            self._age = age
        else:
            raise ValueError('Некорректный возраст')
