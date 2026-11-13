from datetime import date


class BirthInfo:

    def __init__(self, birth_date):
        self.birth_date = self._parse_date(birth_date)

    @staticmethod
    def _parse_date(birth_date):
        if isinstance(birth_date, date) and type(birth_date) is date:
            return birth_date
        if isinstance(birth_date, (list, tuple)):
            if len(birth_date) == 3 and all(
                type(x) is int for x in birth_date
            ):
                try:
                    return date(*birth_date)
                except ValueError:
                    pass
        if isinstance(birth_date, str):
            try:
                return date.fromisoformat(birth_date)
            except ValueError:
                pass
        raise TypeError("Аргумент переданного типа не поддерживается")

    @property
    def age(self):
        today = date.today()
        return (today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day)))
