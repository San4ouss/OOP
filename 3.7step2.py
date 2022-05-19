# class Addition:
#     amount = 0
#
#     def __call__(self, *args, **kwargs):
#         for i in args:
#             if type(i) in (int, float):
#                 self.amount += i
#
#         print(f"Сумма переданных значений = {self.amount}")
#         self.amount = 0
#
#
# add = Addition()
#
# add(10, 20)  # печатает "Сумма переданных значений = 30"
# add(1, 2, 3.4)  # печатает "Сумма переданных значений = 6.4"
# add(1, 2, 'hello', [1, 2], 3)  # печатает "Сумма переданных значений = 6"

class Addition:

    def __call__(self, *args, **kwargs):
        print(f"Сумма переданных значений = {sum(filter(lambda x: type(x) in (int, float), args))}")


add = Addition()

add(10, 20)  # печатает "Сумма переданных значений = 30"
add(1, 2, 3.4)  # печатает "Сумма переданных значений = 6.4"
add(1, 2, 'hello', [1, 2], 3)  # печатает "Сумма переданных значений = 6"
