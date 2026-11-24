class HistoryDict:
    def __init__(self, data=None):
        self._history = {}
        if data:
            for key, value in data.items():
                self._history[key] = [value]

    def __iter__(self):
        return iter(self._history)

    def __getitem__(self, key):
        return self._history[key][-1]

    def __setitem__(self, key, value):
        if key in self._history:
            self._history[key].append(value)
        else:
            self._history[key] = [value]

    def __delitem__(self, key):
        del self._history[key]

    def __len__(self):
        return len(self._history)

    def keys(self):
        return self._history.keys()

    def values(self):
        return (item[-1] for item in self._history.values())

    def items(self):
        return ((key, item[-1]) for key, item in self._history.items())

    def history(self, key):
        if key not in self._history:
            return []
        return list(self._history[key])

    def all_history(self):
        return {key: list(item) for key, item in self._history.items()}


# INPUT DATA:

# TEST_1:
historydict = HistoryDict({'ducks': 99, 'cats': 1})

print(historydict['ducks'])
print(historydict['cats'])
print(len(historydict))

# TEST_2:
historydict = HistoryDict({'ducks': 99, 'cats': 1})

print(*historydict)
print(*historydict.keys())
print(*historydict.values())
print(*historydict.items())

# TEST_3:
historydict = HistoryDict({'ducks': 99, 'cats': 1})

historydict['ducks'] = 100

print(*historydict.values())
print(historydict.history('ducks'))
print(historydict.history('cats'))
print(historydict.history('dogs'))

# TEST_4:
historydict = HistoryDict({'ducks': 99, 'cats': 1})

print(historydict.all_history())
historydict['ducks'] = 100
historydict['ducks'] = 101
historydict['cats'] = 2
print(historydict.all_history())
