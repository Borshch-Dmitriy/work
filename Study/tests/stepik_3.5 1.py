from datetime import datetime, timedelta

fmt = '%H:%M'

data = [('07:14', '08:46'),
        ('09:01', '09:37'),
        ('10:00', '11:43'),
        ('12:13', '13:49'),
        ('15:00', '15:19'),
        ('15:58', '17:24'),
        ('17:57', '19:21'),
        ('19:30', '19:59')]

res = 0
for i in data:
    start = datetime.strptime(i[0], fmt)
    end = datetime.strptime(i[1], fmt)
    result = end - start
    res += result.total_seconds()
res = res//60
print(int(res))