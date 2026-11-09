import re
class CaseHelper:
    @staticmethod
    def is_snake(string):
        pattern = r'^[a-z]+(_[a-z]+)*$'
        return bool(re.match(pattern, string))
    @staticmethod
    def is_upper_camel(string):
        pattern = r'^[A-Z][a-zA-Z]+([A-Z][a-zA-Z]+)*$'
        return bool(re.match(pattern, string))
    @staticmethod
    def to_snake(string):
        res = re.findall(r'[A-Z][a-z]+', string)
        return '_'.join(res).lower()
    @staticmethod
    def to_upper_camel(string):
        return ''.join(x.title() for x in re.findall(r'[a-z]+', string))



print(CaseHelper.to_upper_camel('beegeek'))
print(CaseHelper.to_upper_camel('bee_geek'))


