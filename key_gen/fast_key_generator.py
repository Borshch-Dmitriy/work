import random

def generate_password (length):
    result = ""
    for _ in range(length):
        chance = random.randint(0,1)
        if chance == 0:
            result += chr(random.randint(65, 90))
        elif chance == 1:
            result += chr(random.randint(97, 122))
    return result


print(generate_password(int(input("Enter the length of the password: "))))