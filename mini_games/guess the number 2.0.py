# Есть выбор крайней правой границы, возможность начать игру заново.
import random
print('Добро пожаловать в числовую угадайку')
def is_valid():
    print('Укажите ваше крайнюю границу до какого числа нужно угадать пример "от 1 до (Ваше число)"')
    dif = input()
    if dif.isdigit():
        dif = int(dif)
        numbers = random.randint(1, dif)
        print(f'Введите число от 1 до {dif}')
        counter = 0
        while True:
            counter += 1
            num = input()
            if numbers == num:
                return 'Вы угадали, поздравляем!'
            if num.isdigit() and 1<=int(num)<=dif:
                num = int(num)
                if num > numbers:
                    print('Ваше число больше загаданного, попробуйте еще разок')
                elif num < numbers:
                    print('Ваше число меньше загаданного, попробуйте еще разок')
                elif num == numbers:
                    print('Вы угадали, поздравляем!')
                    while True:
                        answer = input("Хотите повторить?").upper()
                        if answer == "ДА":
                            print(is_valid())
                        elif answer == "НЕТ":
                            print(f'Вы угадали с {counter} попытки')
                            return 'Спасибо, что играли в числовую угадайку. Еще увидимся...'
                        else:
                            print("Введите 'да' или 'нет'")
                            continue
            else:
                print(f'А может быть все-таки введем целое число от 1 до {dif}?')
    else:
        print(f'А может быть все-таки введем целое число?')
        print(is_valid())
print(is_valid())