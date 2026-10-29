from datetime import datetime, timedelta
start = datetime(1,1,1)
end = datetime(9999, 12,31)

def find_fridays(start, end):
    monday = 0
    tuesday = 0
    wednesday = 0
    thursday = 0
    friday = 0
    saturday = 0
    sunday = 0

    while start < end:
        if start.day == 1:
            start += timedelta(days=+11)
        if start.day == 14:
            start += timedelta(days=+13)
        if start.weekday() == 0 and start.day == 13:
            monday += 1
        if start.weekday() == 1 and start.day == 13:
            tuesday += 1
        if start.weekday() == 2 and start.day == 13:
            wednesday += 1
        if start.weekday() == 3 and start.day == 13:
            thursday += 1
        if start.weekday() == 4 and start.day == 13:
            friday += 1
        if start.weekday() == 5 and start.day == 13:
            saturday += 1
        if start.weekday() == 6 and start.day == 13:
            sunday += 1
        start += timedelta(days=+1)

    return monday, tuesday, wednesday, thursday, friday, saturday, sunday


print(*find_fridays(start, end), sep='\n')