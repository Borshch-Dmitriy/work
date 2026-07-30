from datetime import datetime, timedelta

fmt = "%d.%m.%Y"

current_date = datetime.strptime(input(), fmt)

next_7_days = [
    ((current_date + timedelta(days=i)).month, (current_date + timedelta(days=i)).day)
    for i in range(1, 8)
]

suitable_employees = []

for _ in range(int(input())):
    *name, bd_str = input().split()
    name = " ".join(name)
    bd = datetime.strptime(bd_str, fmt)


    if (bd.month, bd.day) in next_7_days:
        suitable_employees.append((name, bd))


if suitable_employees:
    youngest = max(suitable_employees, key=lambda x: x[1])
    print(youngest[0])
else:
    print("Дни рождения не планируются")



