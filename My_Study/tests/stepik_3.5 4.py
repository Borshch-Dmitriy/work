from datetime import datetime, timedelta

fmt = '%d.%m.%Y'
dt1 = datetime.strptime(input(), fmt)
dt2 = datetime.strptime(input(), fmt)


while dt1 <= dt2 and (dt1.day + dt1.month) % 2 == 0:
    dt1 += timedelta(days=1)


while dt1 <= dt2:
    if dt1.weekday() not in (0, 3):
        print(dt1.strftime(fmt))
    dt1 += timedelta(days=3)



