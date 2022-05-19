class PowerTwo:
    def __init__(self, power):
        if type(power) is int and power >= 0:
            self.power = power
        else:
            raise TypeError('Число должно быть целым положительным')

    def __iter__(self):
        self.start = -1
        return self

    def __next__(self):
        if self.start < self.power:
            self.start += 1
            return 2 ** self.start
        else:
            raise StopIteration


for i in PowerTwo(4):  # итерируемся до 4й степени двойки
    print(i)

numbers = PowerTwo(2)

iterator = iter(numbers)

print(next(iterator))  # печатает 1
print(next(iterator))  # печатает 2
print(next(iterator))  # печатает 4
print(next(iterator))  # исключение StopIteration
