class InfinityIterator:
    def __iter__(self):
        self.start = -10
        return self

    def __next__(self):
        self.start += 10
        return self.start


a = iter(InfinityIterator())
print(next(a))
print(next(a))
print(next(a))
print(next(a))
