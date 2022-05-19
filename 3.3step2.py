# class Vector:
#     def __init__(self, *args):
#         self.values = sorted(filter(lambda x: type(x) is int, args))
#
#     def __str__(self):
#         return f'Вектор{tuple(self.values)}' if self.values else 'Пустой вектор'
#
#     @classmethod
#     def __check_values(cls, other):
#         if type(other) not in (int, Vector):
#             return print(f'Вектор нельзя сложить с {other}')
#         return other
#
#     def __add__(self, other):
#         sc = self.__check_values(other)
#         if type(sc) is Vector and len(sc.values) == len(self.values):
#             if len(sc.values) == len(self.values):
#                 # присваиваем объекту v1 новые значения класса Vector, список мы присвоить не можем,
#                 # поэтому его сначала нужно распаковать с помощью оператора *
#                 # проще говоря нельзя передавать объекту класса не распакованный список
#                 return Vector(*[self.values[i] + sc.values[i] for i in range(len(self.values))])
#             else:
#                 print("Сложение векторов разной длины недопустимо")
#         if type(sc) is int:
#             return Vector(*[i + sc for i in self.values])
#
#     def __radd__(self, other):
#         return self + other
#
#     def __mul__(self, other):
#         sc = self.__check_values(other)
#         if type(sc) is Vector:
#             if len(sc.values) == len(self.values):
#                 return Vector(*[self.values[i] * sc.values[i] for i in range(len(self.values))])
#             else:
#                 print("Сложение векторов разной длины недопустимо")
#         if type(sc) is int:
#             return Vector(*[i * sc for i in self.values])
#
#     def __rmul__(self, other):
#         return self + other


# v1 = Vector(1, 2, 3)
# print(v1)  # печатает "Вектор(1, 2, 3)"
#
# v2 = Vector(3, 4, 5)
# print(v2)  # печатает "Вектор(3, 4, 5)"
# v3 = v1 + v2
# print(v3)  # печатает "Вектор(4, 6, 8)"
# v4 = v3 + 5
# print(v4)  # печатает "Вектор(9, 11, 13)"
# v5 = v1 * 2
# print(v5)  # печатает "Вектор(2, 4, 6)"
# v5 + 'hi'  # печатает "Вектор нельзя сложить с hi"


# lst = [1, 2, 3]
# a = 100
# print([i + a for i in lst])

class Vector:
    def __init__(self, *args):
        self.values = sorted(filter(lambda x: type(x) is int, args))

    def __str__(self):
        return f'Вектор{tuple(self.values)}' if self.values else 'Пустой вектор'

    def __add__(self, other):
        if type(other) is Vector:
            if len(other.values) == len(self.values):
                # присваиваем объекту v1 новые значения класса Vector, список мы присвоить не можем,
                # поэтому его сначала нужно распаковать с помощью оператора *
                # проще говоря нельзя передавать объекту класса не распакованный список
                return Vector(*[self.values[i] + other.values[i] for i in range(len(self.values))])
            else:
                print("Сложение векторов разной длины недопустимо")
        if type(other) is int:
            return Vector(*[i + other for i in self.values])
        else:
            print(f'Вектор нельзя сложить с {other}')

    def __radd__(self, other):
        return self + other

    def __mul__(self, other):
        if type(other) is Vector:
            if len(other.values) == len(self.values):
                return Vector(*[self.values[i] * other.values[i] for i in range(len(self.values))])
            else:
                print("Сложение векторов разной длины недопустимо")
        if type(other) is int:
            return Vector(*[i * other for i in self.values])
        else:
            print(f'Вектор нельзя сложить с {other}')

    def __rmul__(self, other):
        return self + other


v1 = Vector(1, 2, 3)
print(v1)  # печатает "Вектор(1, 2, 3)"

v2 = Vector(3, 4, 5)
print(v2)  # печатает "Вектор(3, 4, 5)"
v3 = v1 + v2
print(v3)  # печатает "Вектор(4, 6, 8)"
v4 = v3 + 5
print(v4)  # печатает "Вектор(9, 11, 13)"
v5 = v1 * 2
print(v5)  # печатает "Вектор(2, 4, 6)"
v5 + 'hi'  # печатает "Вектор нельзя сложить с hi"
