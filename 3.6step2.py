class City:
    def __init__(self, name):
        self.name = ' '.join([i[0].upper() + i[1:].lower() for i in name.split()])
        # # Переводит первый символ каждого слова в верхний регистр, а остальные символы этого слова - в нижний
        # self.name = name.title()
        # # Первый символ теперь помещается в заглавный, а не в верхний регистр
        # self.name = " ".join([i.capitalize() for i in name.split()])

    def __str__(self):
        return self.name

    def __bool__(self):
        return self.name[-1] not in ('a', 'e', 'i', 'o', 'u')


p1 = City('new york')
print(p1)  # печатает "New York"
print(bool(p1))  # печатает "True"
p2 = City('SaN frANCISco')
print(p2)  # печатает "San Francisco"
print(p2 == True)  # печатает "False"

