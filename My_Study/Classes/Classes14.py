from functools import singledispatchmethod

class Formatter:
    @singledispatchmethod
    @staticmethod
    def format(value):
        raise TypeError("Аргумент переданного типа не поддерживается")

    @format.register
    @staticmethod
    def _(value: int):
        print(f'Целое число: {value}')

    @format.register
    @staticmethod
    def _(value: float):
        print(f'Вещественное число: {value}')

    @format.register
    @staticmethod
    def _(value: list):
        res = ', '.join(repr(x) for x in value)
        print(f'Элементы списка: {res}')

    @format.register
    @staticmethod
    def _(value: tuple):
        res = ', '.join(repr(x) for x in value)
        print(f'Элементы кортежа: {res}')

    @format.register
    @staticmethod
    def _(value: dict):
        print('Пары словаря: ', end='')
        print(*tuple((k, v) for k, v in value.items()), sep=', ')
