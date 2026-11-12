class Time:
    def __init__(self,hours,minutes):
        self.hours = (hours + minutes // 60) % 24
        self.minutes = minutes % 60
    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}"
    def __add__(self,other):
        if isinstance(other, Time):
            return Time(self.hours + other.hours, self.minutes + other.minutes)
        return NotImplemented
    def __iadd__(self,other):
        if isinstance(other, Time):
            res = self + other
            self.hours = res.hours
            self.minutes = res.minutes
            return self
        return NotImplemented
