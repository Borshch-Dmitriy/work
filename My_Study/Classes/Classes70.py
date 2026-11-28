class TreeBuilder:
    def __init__(self):
        self._root = []
        self._stack = [self._root]

    def __enter__(self):
        new_node = []
        self._stack.append(new_node)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        finished_node = self._stack.pop()
        if finished_node:
            self._stack[-1].append(finished_node)
        return False

    def add(self, value):
        self._stack[-1].append(value)

    def structure(self):
        return self._root


tree = TreeBuilder()
print(tree.structure())

tree.add('1st')
print(tree.structure())

with tree:
    tree.add('2nd')
    with tree:
        tree.add('3rd')
    tree.add('4th')
    with tree:
        pass 

print(tree.structure())
