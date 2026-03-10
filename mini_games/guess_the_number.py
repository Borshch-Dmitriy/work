import random

numbers = random.randrange(1, 101)

while numbers:
    s = int(input("Угадайте число от 1 до 100""\n"))
    if s == numbers:
        print('Вы угадали, поздравляем!')
        break
    elif s > numbers:
        print('Слишком много, попробуйте еще раз')
    elif s < numbers:
        print('Слишком мало, попробуйте еще раз')

print(numbers)