from datetime import datetime
digit = int(input())
fmt = '%d.%m.%Y'
new_list = [input().split(' ') for _ in range(digit)]
new_dict = {}
for item in new_list:
    if item[2] not in new_dict:
        new_dict[item[2]] = 1
    elif item[2] in new_dict:
        new_dict[item[2]] += 1
result = []
for key, value in new_dict.items():
    if value == max(new_dict.values()):
        result.append(key)
for i in range(len(result)):
    result[i] = datetime.strptime(result[i], fmt)
result.sort()
for item in result:
    print(datetime.strftime(item, fmt))
