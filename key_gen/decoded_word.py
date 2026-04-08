## decoded_word for stepik ##

pas, num = input(), int(input())
dict_freq = {}
char_count = {}


for i in range(num):
    key, value = input().split(': ')
    dict_freq[int(value)] = key


for i in pas:
    if i not in char_count:
        char_count[i] = 1
    else:
        char_count[i] += 1


decoded_word = ""
for i in pas:

    current_freq = char_count[i]

    decoded_word += dict_freq[current_freq]

print(decoded_word)