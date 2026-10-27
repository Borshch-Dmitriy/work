import random
def get_anagram(word):
    word = list(word)
    random.shuffle(word)
    word = "".join(word)
    return word

print(get_anagram(input()))