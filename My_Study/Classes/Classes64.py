class Suppress:
    def __init__(self,*args):
        self.ex = [ard for ard in args]
        self.exception = None
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None and exc_type in self.ex:
            self.exception = exc_val
        return True


with Suppress(TypeError, ValueError) as context:
    number = int('я число')

print(context.exception)
print(type(context.exception))
