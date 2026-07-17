# Проверка слова на сходство по гласным.
text = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']

check_word = input()
num = int(input())
new_text = []
result = []

# Собираем слова
for i in range(num):
    new_text.append(input())

res_indexes = []
for i in range(len(check_word)):
    if check_word[i] in text:
        res_indexes.append(i)

# Проверяем слова
for i in range(len(new_text)):
    check_indexes = []
    for j in range(len(new_text[i])):
        if new_text[i][j] in text:
            check_indexes.append(j)

    # Если списки индексов полностью совпали, значит гласные на тех же местах
    if res_indexes == check_indexes:
        result.append(new_text[i])

print(*result, sep='\n')