#The last in block
from datetime import datetime, timedelta

def choose_p(amount, declensions):
    if amount % 10 == 1 and amount % 100 != 11:
        return f"{amount} {declensions[0]}"
    elif amount % 10 in [2, 3, 4] and amount % 100 not in [12, 13, 14]:
        return f"{amount} {declensions[1]}"
    else:
        return f"{amount} {declensions[2]}"

pattern = "%d.%m.%Y %H:%M"
start_date = datetime(2022, 11, 8, 12, 0)
now_date = datetime.strptime(input(), pattern)

if now_date >= start_date:
    print("Курс уже вышел!")
else:
    diff = start_date - now_date
    days = diff.days
    hours = diff.seconds // 3600
    minutes = (diff.seconds // 60) % 60
    d_str = choose_p(days, ('день', 'дня', 'дней'))
    h_str = choose_p(hours, ('час', 'часа', 'часов'))
    m_str = choose_p(minutes, ('минута', 'минуты', 'минут'))
    if days > 0:
        if hours > 0:
            print(f"До выхода курса осталось: {d_str} и {h_str}")
        else:
            print(f"До выхода курса осталось: {d_str}")
    else:
        if hours > 0 and minutes > 0:
            print(f"До выхода курса осталось: {h_str} и {m_str}")
        elif hours > 0 and minutes == 0:
            print(f"До выхода курса осталось: {h_str}")
        elif hours == 0 and minutes > 0:
            print(f"До выхода курса осталось: {m_str}")




