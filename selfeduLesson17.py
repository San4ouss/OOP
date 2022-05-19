class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        print('__len__')
        return self.x * self.x + self.y * self.y


p = Point(3, 4)
print(len(p))
print(bool(p))

