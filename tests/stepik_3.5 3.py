from datetime import datetime

fmt = '%d.%m.%Y %H:%M'
dt = datetime.strptime(input(), fmt)

weekday = dt.weekday()
time_now = dt.time()


if weekday < 5:
    open_time = datetime.strptime('09:00', '%H:%M').time()
    close_time = datetime.strptime('21:00', '%H:%M').time()
else:
    open_time = datetime.strptime('10:00', '%H:%M').time()
    close_time = datetime.strptime('18:00', '%H:%M').time()


if open_time <= time_now < close_time:
    close_datetime = dt.replace(hour=close_time.hour, minute=close_time.minute)
    remaining_minutes = int((close_datetime - dt).total_seconds() // 60)
    print(remaining_minutes)
else:
    print('Магазин не работает')
