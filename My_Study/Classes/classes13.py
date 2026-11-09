class CaseHelper:

    @staticmethod
    def is_snake(string):
        return string.replace('_', '').isalpha() and string.lower() == string and '__' not in string

    @staticmethod
    def is_upper_camel(string):
        return string.isalpha() and string[0].isupper() and string[1].islower()

    @staticmethod
    def to_snake(string):
        return ''.join(i if i.islower() else '_' + i.lower() for i in string)[1:]

    @staticmethod
    def to_upper_camel(string):
        return string.title().replace('_', '')
