from datetime import datetime, date
class DateFormatter:
    '''Format datetime string'''
    formats = {'ru': '%d.%m.%Y','us': '%m-%d-%Y','ca': '%Y-%m-%d','br': '%d/%m/%Y','fr': '%d.%m.%Y','pt': '%d-%m-%Y'}
    def __init__(self, country_code: str):
        if country_code not in self.formats:
            raise ValueError('Неверный код страны. Доступные (ru,us,ca,br,fr,pt)')
        else:
            self.country_code = country_code
    def __call__(self,d):
        return d.strftime(self.formats[self.country_code])


ru_format = DateFormatter('rп')

print(ru_format(date(2022, 11, 7)))
