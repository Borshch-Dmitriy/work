class AttrsNumberObject:
    def __init__(self,**kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
    @property
    def attrs_num(self):
        return len(self.__dict__) + 1



music_group = AttrsNumberObject(name='Silent Poets', genre='acid jazz')

print(music_group.attrs_num)
