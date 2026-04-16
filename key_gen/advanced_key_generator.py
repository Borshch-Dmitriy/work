import random
import string

not_use = "lI1oO0"

digits = [c for c in string.digits if c not in not_use]
up_letters = [c for c in string.ascii_uppercase if c not in not_use]
low_letters = [c for c in string.ascii_lowercase if c not in not_use]
all_chars = digits + up_letters + low_letters


def generate_password(length):
    if length < 3:
        return "Password length: >= 3"

    pwd = [random.choice(digits), random.choice(up_letters), random.choice(low_letters)]
    pwd += random.choices(all_chars, k=length - 3)

    random.shuffle(pwd)
    return ''.join(pwd)

count = int(input())
length = int(input())
if length < 3:
    print("Error: Password length must be at least 3 chars.")
else:
    for _ in range(count):
        print(generate_password(length))