class Wordplay:
    def __init__(self,words = []):
        self.words = words[:]
    def add_word(self,word):
        if word not in self.words:
            self.words.append(word)
    def words_with_length(self,n):
        return [word for word in self.words if len(word) == n]
    def only(self,*args):
        res = []
        for word in self.words:
            flag = False
            for letter in word:
                if letter not in args:
                    flag = False
                    break
                if letter in args and word not in res:
                    flag = True
                    continue
            if flag and word not in res:
                res.append(word)
        return res
    def avoid(self,*args):
        res = []
        for word in self.words:
            flag = True
            for letter in word:
                if letter not in args:
                    flag = True
                    continue
                if letter in args and word not in res:
                    flag = False
                    break
            if flag and word not in res:
                res.append(word)
        return res

# TEST_5:
wordplay = Wordplay(['a', 'arthur', 'timur', 'bee', 'geek', 'python', 'stepik'])

print(wordplay.avoid('a', 'b', 'c'))

# TEST_8:
words = ['Лейбниц', 'Бэббидж', 'Нейман', 'Джобс', 'да_Винчи', 'Касперский']
wordplay = Wordplay(words)

words.extend(['Гуев', 'Харисов', 'Светкин'])
print(words)
print(wordplay.words)
