class Counter:
    """Класс Counter. Считает значения. Методы класса:
           start_from([value=0]) - устанавливает начальное значение счетчика
           increment() - увеличивает счетчик на 1
           display() - выводит текущее значение счетчика
           reset() - обнуляет значение счетчика
        """

    def start_from(self, x=0):
        self.x = x

    def increment(self):
        self.x += 1

    def display(self):
        print(f'Текущее значение счетчика = {self.x}')

    def reset(self):
        self.x = 0


c1 = Counter()
c1.start_from()
c1.increment()
c1.display()  # печатает "Текущее значение счетчика = 1"
c1.increment()
c1.display()  # печатает "Текущее значение счетчика = 2"
c1.reset()
c1.display()  # печатает "Текущее значение счетчика = 0"

c2 = Counter()
c2.start_from(3)
c2.display()  # печатает "Текущее значение счетчика = 3"
c2.increment()
c2.display()  # печатает "Текущее значение счетчика = 4"

print(Counter.__doc__)