==========================================
ШПАРГАЛКА ПО КЛАССАМ И ООП В PYTHON
==========================================
1. ОБЪЯВЛЕНИЕ КЛАССА И СОЗДАНИЕ ОБЪЕКТА (ЭКЗЕМПЛЯРА)
class Dog:
# Конструктор класса — вызывается при создании объекта
def init(self, name, age):
self.name = name     # Атрибут экземпляра (у каждого свой)
self.age = age
# Метод экземпляра класса
def bark(self):
return f"{self.name} гавкает!"
my_dog = Dog("Шарик", 3)     # Создание объекта (экземпляра) класса
print(my_dog.name)           # Доступ к атрибуту -> "Шарик"
print(my_dog.bark())         # Вызов метода -> "Шарик гавкает!"
2. АТРИБУТЫ КЛАССА И ЭКЗЕМПЛЯРА
class Car:
wheels = 4               # Атрибут класса (общий для всех объектов)
def init(self, brand):
self.brand = brand   # Атрибут экземпляра (уникальный)
# car1 = Car("BMW")
# car2 = Car("Audi")
# print(car1.wheels, car2.wheels) -> 4, 4 (общие)
# print(Car.wheels)            -> обращение через сам класс
3. НАСЛЕДОВАНИЕ
class Animal:                # Родительский (базовый) класс
def init(self, name):
self.name = name
def make_sound(self):
return "Шум..."
class Cat(Animal):           # Дочерний класс (наследует от Animal)
def make_sound(self):    # Переопределение (override) метода родителя
return "Мяу!"
my_cat = Cat("Барсик")
print(my_cat.name)           # Взято из Animal -> "Барсик"
print(my_cat.make_sound())   # Переопределенный метод -> "Мяу!"
4. СПЕЦИАЛЬНЫЕ МЕТОДЫ (МАГИЧЕСКИЕ / DUNDER-МЕТОДЫ)
class Book:
def init(self, title, pages):
self.title = title
self.pages = pages
def str(self):       # Для пользователя (вызывается print() и str())
return f"Книга: '{self.title}', страниц: {self.pages}"
def repr(self):      # Для разработчика (в консоли, отладка)
return f"Book('{self.title}', {self.pages})"
def len(self):       # Поведение для функции len()
return self.pages
b = Book("Python 101", 300)
print(b)                     # Вызовет str -> Книга: 'Python 101', страниц: 300
print(len(b))                # Вызовет len -> 300
5. ИНКАПСУЛЯЦИЯ (ОБРАМЛЕНИЕ И СКРЫТИЕ ДАННЫХ)
class BankAccount:
def init(self, owner, balance):
self.owner = owner          # Публичный атрибут
self._pin = 1234            # Защищенный (protected) — соглашение о не трогать вне класса
self.__balance = balance    # Приватный (private) — питон делает name mangling
def get_balance(self):          # Геттер (чтение приватного поля)
return self.__balance
def deposit(self, amount):      # Сеттер/метод изменения с логикой
if amount > 0:
self.__balance += amount
6. СВОЙСТВА (PROPERTY — ГЕТТЕРЫ И СЕТТЕРЫ ЧЕРЕЗ ДЕКОРАТОРЫ)
class Temperature:
def init(self, celsius=0):
self._celsius = celsius
@property
def celsius(self):       # Позволяет вызывать как атрибут: obj.celsius
return self._celsius
@celsius.setter
def celsius(self, value):# Позволяет присваивать: obj.celsius = 25
if value < -273.15:
raise ValueError("Температура ниже абсолютного нуля!")
self._celsius = value
t = Temperature(20)
t.celsius = 25               # Вызывает сеттер
print(t.celsius)             # Вызывает геттер -> 25
7. СТАТИЧЕСКИЕ МЕТОДЫ И МЕТОДЫ КЛАССА (@classmethod, @staticmethod)
class MathUtils:
PI = 3.14159
@classmethod
def get_pi(cls):         # Принимает класс (cls) как аргумент, имеет доступ к атрибутам класса
return cls.PI
@staticmethod
def add(a, b):           # Обычная функция внутри класса, не видит ни self, ни cls
return a + b
print(MathUtils.get_pi())    # Вызов метода класса -> 3.14159
print(MathUtils.add(2, 3))   # Вызов статического метода -> 5
