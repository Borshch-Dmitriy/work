from datetime import datetime
digit = int(input())
fmt = '%d.%m.%Y'
new_list = [input().split(' ') for _ in range(digit)]
for i in range(digit):
    new_list[i][2] = datetime.strptime(new_list[i][2], fmt)
new_list.sort(key=lambda x: x[2])
counter = 0
for item in new_list:
    if new_list[0][2] == item[2]:
        counter += 1
if counter == 1:
    print(f"{datetime.strftime(new_list[0][2], '%d.%m.%Y')} {new_list[0][0]} {new_list[0][1]}")
if counter > 1:
    print(f"{datetime.strftime(new_list[0][2], '%d.%m.%Y')} {counter}")





