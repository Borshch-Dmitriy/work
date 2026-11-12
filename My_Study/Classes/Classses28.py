from collections import deque

class Queue:
    def __init__(self,*args):
        self.queue = deque(x for x in args)
    def __str__(self):
        return f'{' -> '.join([str(x) for x in self.queue])}'
    def add(self,*args):
        return self.queue.extend(args)
    def pop(self):
        if len(self.queue) > 0:
            return self.queue.popleft()
        return None
    def __eq__(self, other):
        if isinstance(other, Queue):
            return self.queue == other.queue and len(self.queue) == len(other.queue)
        return NotImplemented
    def __add__(self, other):
        if isinstance(other, Queue):
            res = self.queue + other.queue
            return Queue(*res)
        return NotImplemented
    def __iadd__(self, other):
        if isinstance(other, Queue):
            self.queue += other.queue
            return self
        return NotImplemented
    def __rshift__(self, other):
        if isinstance(other, int):
            return Queue(*[str(x) for x in self.queue][other:])
        return NotImplemented
