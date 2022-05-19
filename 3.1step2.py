# class Person:
#
#     def __init__(self, name, surname, gender='male'):
#         self.name = name
#         self.surname = surname
#         self.gender = gender
#         if self.gender != 'female' and self.gender != 'male':
#             # выполняется только в том случае если gender не равен ни 'femame', ни 'male'
#             print('Не знаю, что вы имели ввиду? Пусть это будет мальчик!')
#             self.gender = 'male'
#
#     def __str__(self):
#         return f'Гражданка {self.surname} {self.name}' if self.gender == 'female' else f'Гражданин {self.surname} {self.name}'
#
#
# p1 = Person('Chuck', 'Norris')
# print(p1)  # печатает "Гражданин Norris Chuck"
# p2 = Person('Mila', 'Kunis', 'female')
# print(p2)  # печатает "Гражданка Kunis Mila"
# p3 = Person('Оби-Ван', 'Кеноби', True)  # печатает "Не знаю, что вы имели ввиду? Пусть это будет мальчик!"
# print(p3)  # печатает "Гражданин Кеноби Оби-Ван"

class Person:

    def __init__(self, name, surname, gender='male'):
        self.name = name
        self.surname = surname
        if gender != 'female' and gender != 'male':
            # выполняется только в том случае если gender не равен ни 'femame', ни 'male'
            print('Не знаю, что вы имели ввиду? Пусть это будет мальчик!')
            self.gender = 'male'
        else:
            self.gender = gender

    def __str__(self):
        return f'Гражданка {self.surname} {self.name}' if self.gender == 'female' else f'Гражданин {self.surname} {self.name}'


p1 = Person('Chuck', 'Norris')
print(p1)  # печатает "Гражданин Norris Chuck"
p2 = Person('Mila', 'Kunis', 'female')
print(p2)  # печатает "Гражданка Kunis Mila"
p3 = Person('Оби-Ван', 'Кеноби', True)  # печатает "Не знаю, что вы имели ввиду? Пусть это будет мальчик!"
print(p3)  # печатает "Гражданин Кеноби Оби-Ван"
