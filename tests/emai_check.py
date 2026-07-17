n = int(input())
busy_emails = {input() for _ in range(n)}

m = int(input())
new_emails = [input() for _ in range(m)]

em = "@beegeek.bzz"

for name in new_emails:
    number = 0
    while True:
        # Если 0, номер к имени не приписывается
        suffix = "" if number == 0 else str(number)
        current_email = f"{name}{suffix}{em}"

        # Если сгенерированный адрес свободен
        if current_email not in busy_emails:
            busy_emails.add(current_email)
            print(current_email)
            break

        # Если занят, проверяем следующий по порядку номер
        number += 1