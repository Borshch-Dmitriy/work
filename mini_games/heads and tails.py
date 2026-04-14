import random

def coin_flip():
    choice = random.randint(0,1)
    if choice == 0:
        return "Head"
    else:
        return  "Tail"

print(coin_flip())