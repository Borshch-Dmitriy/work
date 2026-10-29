import random

def estimate_pi(n=1000000):
    m = 0
    for _ in range(n):
        x = random.random()
        y = random.random()
        if x ** 2 + y ** 2 <= 1:
            m += 1

    pi_val = (m / n) * 4
    return pi_val


result = estimate_pi()
print(result)