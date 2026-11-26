from functools import wraps
def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(">>> Функция начала работу")
        func(*args, **kwargs)
        print(">>> Функция завершила работу")
    return wrapper

@log_execution
def say_hello(name):
    print(f"Привет, {name}!")

# Пытаемся вызвать декорированную функцию:
say_hello("Алексей")
