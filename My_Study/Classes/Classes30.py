class RaiseTo:
    '''Raise to degree'''
    def __init__(self, degree: int):
        self.degree = degree

    def __call__(self,x: int) -> int:
        return  x ** self.degree

one = RaiseTo(10)

print(one.__doc__)
