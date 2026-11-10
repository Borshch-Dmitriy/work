class PhoneNumber:
    def __init__(self, number):
        self.number = ''.join(number.split())

    def __str__(self):
        return f'({self.number[0:3]}) {self.number[3:6]}-{self.number[6:]}'

    def __repr__(self):
        return f"PhoneNumber('{self.number}')"
