class Vector:
    def __init__(self, *args):
        self.values = list(filter(lambda x: type(x) is int, args))

    def __str__(self):
        return f'Вектор{tuple(sorted(self.values))}' if self.values else 'Пустой вектор'
        # if self.values:
        #     values = ', '.join(map(str, sorted(self.values)))
        #     return f'Вектор({values})'
        # else:
        #     return 'Пустой вектор'


v1 = Vector(5, 1, 2, 3, 2.1, '3')
print(v1)  # печатает "Вектор(1, 2, 3)"
v2 = Vector()
print(v2)  # печатает "Пустой вектор"
