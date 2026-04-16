import random
import string
not_use = "lI1oO0"
letters_digits = string.digits + string.ascii_letters
new_letters_digits = [letter for letter in letters_digits if letter not in not_use]
count, length = int(input()), int(input())


def generate_password(length):
    password = random.sample(new_letters_digits, length)
    return password

def generate_passwords(count, length):
    result = []
    for i in range(count):
        result.append(generate_password(length))
    return result
result = generate_passwords(count, length)

for j in range(count):
    print(*result[j], sep='')