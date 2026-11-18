class DevelopmentTeam:
    def __init__(self):
        self.juniors = []
        self.seniors = []
    def add_junior(self,*args):
        for i in ((x,'junior') for x in args):
            self.juniors.append(i)
        print(self.juniors)
    def add_senior(self,*args):
        for i in ((x,'senior') for x in args):
            self.seniors.append(i)
        print(self.seniors)
    def __iter__(self):
        yield from self.juniors
        yield from self.seniors





beegeek = DevelopmentTeam()

beegeek.add_senior('Gvidos')
beegeek.add_senior('Papandos')
beegeek.add_junior('Timur')
beegeek.add_junior('Arthur', 'Valery')
beegeek.add_senior('Gvido')
print(*beegeek, sep='\n')
