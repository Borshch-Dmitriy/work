import random

print('Вас приветствует гениратор паролей')

def length_password():
    while True:
        print('Введите жилаемую длину пароля')
        length_password = input()
        if length_password.isdigit():
            return int(length_password)
        else:
            print('Допустимо ввод целого числа! от 1 до 100')
            continue
l_n = length_password()

def parametrs_password():
    chars = ''
    while True:
        include_digits = input('Включать ли цифры 0123456789? ответ(ДА,НЕТ) ').lower()
        if include_digits == 'да':
            chars = chars + '0123456789'
        include_uppercase_letters = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? ответ(ДА,НЕТ) ').lower()
        if include_uppercase_letters == 'да':
            chars = chars + 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        include_lowercase_letters = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? ответ(ДА,НЕТ) ').lower()
        if include_lowercase_letters == 'да':
            chars = chars + 'abcdefghijklmnopqrstuvwxyz'
        include_punctuation = input('!#$%&*+-=?@^_?"" ответ(ДА,НЕТ) ').lower()
        if include_punctuation == 'да':
            chars = chars + '!#$%&*+-='
        if chars == '':
            print('Пароль не может быть пустой, Выбирите настройки еще раз')
            continue
        return chars

chars = parametrs_password()

def safe_password():
    amount = input('Количество паролей для генерации:')
    if  amount.isdigit():
        amount = int(amount)
        for j in range(0,amount):
            for i in range(l_n):
                print(random.choice(chars), end = "")
            print('\n')
    elif not amount.isdigit():
        print('ВВедите число')
        safe_password()

safe_password()
