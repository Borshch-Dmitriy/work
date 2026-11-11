class ReversibleString:
    def __init__(self, string):
        self.string = string
    def __repr__(self):
        return self.string
    def __neg__(self):
        return  ReversibleString(self.string[::-1])
