class Todo:
    def __init__(self):
        self.things = []
    def add(self, thing,priority=0):
        self.things.append((thing,priority))
    def get_by_priority(self,priority):
        return [i[0] for i in self.things if i[1] == priority]
    def get_low_priority(self):
        try:
            priority = min(i[1] for i in self.things)
            return [i[0] for i in self.things if i[1] == priority]
        except:
            return []
    def get_high_priority(self):
        try:
            priority = max(i[1] for i in self.things)
            return [i[0] for i in self.things if i[1] == priority]
        except:
            return []

# TEST_4:
todo = Todo()

todos = [
    'Выбрать хостинг для своего сайта',
    'Записаться к стоматологу',
    'Записаться на курсы английского',
    'Навести порядок на кухне',
    'Подготовить одежду к лету',
    'Подготовиться к выступлению в понедельник',
    'Помыть машину',
    'Пропылесосить ковры',
    'Свозить Кемаля к ветеринару',
    'Сходить в парикмахерскую',
    'Посетить выставку камней'
]

priorities = [4, 1, 2, 5, 2, 5, 5, 3, 3, 3, 4]
for t, p in zip(todos, priorities):
    todo.add(t, p)

print(todo.things)
print(todo.get_by_priority(3))
print(todo.get_low_priority())
print(todo.get_high_priority())
