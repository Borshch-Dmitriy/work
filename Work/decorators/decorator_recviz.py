import functools


def recviz(func):
    spaces = [0]
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        indent = "    " * spaces[0]
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={repr(v)}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)

        print(f"{indent}-> {func.__name__}({signature})")
        spaces[0] += 1
        result = func(*args, **kwargs)
        spaces[0] -= 1
        print(f"{indent}<- {repr(result) if isinstance(result, str) else result}")
        return result

    return wrapper


@recviz
def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

fib(4)

@recviz
def add(a, b, c, d, e):
    return (a + b + c) * (d + e)

add('a', b='b', c='c', d=3, e=True)