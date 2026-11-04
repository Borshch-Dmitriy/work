class TextHandler:
    def __init__(self):
        self.text = []
    def add_words(self, words):
        for word in words.split():
            self.text.append(word)
    def show_words(self):
        return self.text
    def get_shortest_words(self):
        res = []
        for word in self.text:
            if len(word) == len(min(self.text, key=len)):
                res.append(word)
        return res
    def get_longest_words(self):
        res = []
        for word in self.text:
            if len(word) == len(max(self.text, key=len)):
                res.append(word)
        return res




texthandler = TextHandler()

texthandler.add_words('The world will hold my trial for your sins')
texthandler.add_words('Never meant to see the sky never meant to live')

print(texthandler.get_shortest_words())
print(texthandler.get_longest_words())