from random import shuffle
class RandomLooper:
    def __init__(self,*args):
        self.args = [y for x in args for y in x]
        shuffle(self.args)
        self.args = iter(self.args)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.args)


# TEST_3:
from string import ascii_letters

domains = ['riley.net', 'herman.org', 'tran-guerrero.com', 'martinez.com', 'riley-moore.info', 'allen.com',
           'lopez.com', 'santiago.com', 'moran-craig.com', 'smith-graves.com', 'smith.com', 'johnson.biz',
           'gregory-smith.com', 'smith.com', 'douglas.com', 'marshall.com', 'henry-garcia.com', 'allen.com']

work = {'Horticulturist, commercial', 'Archaeologist', 'Neurosurgeon', 'Investment analyst',
        'Energy manager', 'Conservation officer, historic buildings', 'Town planner',
        'Research scientist (physical sciences)', 'Dancer', 'Financial adviser', 'Human resources officer',
        'Meteorologist', 'Water quality scientist', 'Call centre manager', 'Surveyor, rural practice',
        'Sports administrator', 'Electronics engineer', 'Pharmacist, hospital'}

phone_numbers = ('178-222-6477x229', '+1-656-770-5470x078', '+1-297-950-6100',
                 '(931)443-0778x87575', '329-788-0662', '+1-955-232-3577x6474', '001-562-654-3195x083', '854.344.9086',
                 '546-622-8169', '(161)097-6037', '(539)319-3442', '001-874-988-4679x3997', '079-860-8803x913',
                 '2410563363', '(852)061-7986x980', '393.485.5132', '+1-089-015-3223x3791', '(010)648-5657x225',)

names = {'Brittany Mccoy': 'BM', 'Ariana Jackson': 'AJ', 'Jeffrey Smith': 'JS',
         'Eric Hanson': 'EH', 'Anthony Robinson': 'AR', 'Ricky Garcia': 'RG', 'Derrick Cruz': 'DC',
         'Brittany Simpson': 'BS', 'Richard Tran': 'RT', 'Denise Hernandez': 'DH', 'Michael Lin': 'ML',
         'James James': 'JJ', 'Jacob Saunders': 'JS', 'Stephanie Sherman': 'SS', 'John Austin': 'JA',
         'Benjamin Mason': 'BM', 'Corey Brown': 'CB', 'Gregory Adams': 'GA'}

randomlooper = RandomLooper(domains, work, phone_numbers, names, ascii_letters)
print(list(randomlooper))

