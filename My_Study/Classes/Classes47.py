class ProtectedObject:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            object.__setattr__(self, key, value)

    def __getattribute__(self, name):
        if name.startswith('_'):
            raise AttributeError("Доступ к защищенному атрибуту невозможен")
        else:
            return object.__getattribute__(self, name)

    def __getattr__(self, key):
        if key.startswith('_'):
            raise AttributeError('Доступ к защищенному атрибуту невозможен')
        raise AttributeError

    def __setattr__(self, key, value):
        if key.startswith('_'):
            raise AttributeError('Доступ к защищенному атрибуту невозможен')
        else:
            object.__setattr__(self, key, value)

    def __delattr__(self, key):
        if key.startswith('_'):
            raise AttributeError('Доступ к защищенному атрибуту невозможен')
        else:
            object.__delattr__(self, key)
# INPUT DATA:

# TEST_1:
user = ProtectedObject(login='PG_kamiya', _password='alreadybanned')

try:
    print(user.login)
    print(user._password)
except AttributeError as e:
    print(e)

# TEST_2:
user = ProtectedObject(login='PG_kamiya', _password='alreadybanned')

try:
    user._password = 'qwerty12345'
except AttributeError as e:
    print(e)
