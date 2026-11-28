
class Grandfather:
    def __init__(self):
        print("Инициализация дедушки (Grandfather)")


class Father(Grandfather):
    def __init__(self):
        print("Инициализация отца (Father) — начало")
        super().__init__()  # Вызывает Grandfather
        print("Инициализация отца (Father) — конец")


class Son(Father):
    def __init__(self):
        print("Инициализация сына (Son) — начало")
        object.__init__(self)  # Вызывает Father (НЕ Grandfather напрямую!)
        print("Инициализация сына (Son) — конец")


# Создаем объект
s = Son()