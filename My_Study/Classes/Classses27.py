class Path:
    def __init__(self, *args):
        res = []
        for arg in args:
            if isinstance(arg, Path):
                res.extend(arg.path)
            else:
                res.append(arg)
        self.path = tuple(res)

    def __repr__(self):
        return f"Path('{'/'.join(map(str, self.path))}')"

    def __str__(self):
        return '/'.join(map(str, self.path))

    def __truediv__(self, other):
        if isinstance(other, Path):
            return Path(*(self.path + other.path))
        elif isinstance(other, str):
            return Path(*(self.path + (other,)))
        return NotImplemented

    def __itruediv__(self, other):
        if isinstance(other, Path):
            self.path = self.path + other.path
            return self
        elif isinstance(other, str):
            self.path = self.path + (other,)
            return self
        return NotImplemented
path = Path('home', 'user', 'docs')
