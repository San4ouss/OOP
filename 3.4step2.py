# class ChessPlayer:
#     def __init__(self, name, surname, rating):
#         self.name = name
#         self.surname = surname
#         self.rating = rating
#
#     @classmethod
#     def __check_data(cls, other):
#         if type(other) not in (int, ChessPlayer):
#             return 'Невозможно выполнить сравнение'
#         return other if type(other) is int else other.rating
#
#     def __eq__(self, other):
#         sc = self.__check_data(other)
#         if type(sc) is not str:
#             return self.rating == sc
#         return sc
#
#     def __lt__(self, other):
#         sc = self.__check_data(other)
#         if type(sc) is not str:
#             return self.rating < sc
#         return sc
#
#     # инициализатор языка Python при проверке на больше использует магический метод __lt__
#     # предварительно поменяв операнды местами
#     # поэтому метод __gt__ прописывать необязательно
#     def __gt__(self, other):
#         sc = self.__check_data(other)
#         if type(sc) is not str:
#             return self.rating > sc
#         return sc
#
#
# magnus = ChessPlayer('Carlsen', 'Magnus', 2847)
# ian = ChessPlayer('Ian', 'Nepomniachtchi', 2789)
# print(magnus == 4000)  # False
# print(ian == 2789)  # True
# print(magnus == ian)  # False
# print(magnus > ian)  # True
# print(magnus < ian)  # False
# print(magnus < [1, 2])  # печатает "Невозможно выполнить сравнениe"
# print(magnus < 'p')  # печатает "Невозможно выполнить сравнениe"

# второй способ с дублированием

class ChessPlayer:
    def __init__(self, name, surname, rating):
        self.name = name
        self.surname = surname
        self.rating = rating

    def __eq__(self, other):
        if type(other) is int:
            return self.rating == other
        elif type(other) is ChessPlayer:
            return self.rating == other.rating
        else:
            return 'Невозможно выполнить сравнение'

    def __lt__(self, other):
        if type(other) is int:
            return self.rating < other
        elif type(other) is ChessPlayer:
            return self.rating < other.rating
        else:
            return 'Невозможно выполнить сравнение'

    # инициализатор языка Python при проверке на больше использует магический метод __lt__
    # предварительно поменяв операнды местами
    # поэтому метод __gt__ прописывать необязательно
    def __gt__(self, other):
        if type(other) is int:
            return self.rating > other
        elif type(other) is ChessPlayer:
            return self.rating > other.rating
        else:
            return 'Невозможно выполнить сравнение'


magnus = ChessPlayer('Carlsen', 'Magnus', 2847)
ian = ChessPlayer('Ian', 'Nepomniachtchi', 2789)
print(magnus == 4000)  # False
print(ian == 2789)  # True
print(magnus == ian)  # False
print(magnus > ian)  # True
print(magnus < ian)  # False
print(magnus < [1, 2])  # печатает "Невозможно выполнить сравнениe"
