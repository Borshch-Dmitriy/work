from datetime import date
def is_correct(day,month,year):
    try:
        date(int(year),int(month),int(day))
        print("Корректная")
        return True
    except:
        print('Некорректная')
        return False
counter = 0
while True:
    line = input()
    if line == "end":
        break
    day, month, year = line.split('.')
    if is_correct(day,month,year):
        counter += 1
print(counter)