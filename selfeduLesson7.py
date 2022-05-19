class Point:
    MAX_COORD = 100
    MIN_COORD = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __delattr__(self, item):
        print('__delattr__: ' + item)
        object.__delattr__(self, item)


pt1 = Point(1, 2)
pt2 = Point(10, 20)
del pt1.x
print(pt1.__dict__)
print(pt2.__dict__)
print(Point.__dict__)
