# # первый вариант без защищенных атрибутов и проверок
# class Calculator:
#     """Класс для расчета режимов резания"""
#
#     def __init__(self, Dc, fn, n, lm):
#         import math
#         self.Dc = Dc
#         self.fn = fn
#         self.n = n
#         self.lm = lm
#         self.kc = 2535
#         self.efficiency = 0.95
#         self.vc = self.Dc * math.pi * self.n / 1000
#         self.vf = self.fn * self.n
#         self.Q = self.Dc * self.fn * self.vc / 4
#         self.Pc = self.fn * self.vc * self.Dc * self.kc / 240000
#         self.Mc = self.Pc * 30000 / (math.pi * self.n)
#         self.Ft = 0.5 * self.kc * self.Dc * self.fn * math.sin(2.44/2) / 2
#         self.Tc = self.lm / self.vf
#
#     @classmethod
#     def __check_data(cls, data):
#         if type(data) not in (int, float):
#             raise TypeError("Входные значения должны быть целыми или вещественными числами")
#         return data
#
#     @staticmethod
#     def __calculate_walter(self):
#         '''калькулятор от walter'''
#         import math
#         self.vc = self.Dc * math.pi * self.n / 1000
#         self.vf = self.fn * self.n
#         self.Q = (self.vf * math.pi * pow(self.Dc, 2)) / (4 * 1000)
#         self.P = (self.Q * self.kc) / (60000 * self.efficiency)
#         self.Mc = pow(self.Dc, 2) * self.kc * self.fn / 8000
#         self.Ft = 0.63 * (self.fn * self.Dc * self.kc / 2)
#         self.Tc = self.lm / self.vf
#
#     @staticmethod
#     def __calculate_sandvik(self):
#         '''калькулятор от sandvik'''
#         import math
#         self.vc = self.Dc * math.pi * self.n / 1000
#         self.vf = self.fn * self.n
#         self.Q = self.Dc * self.fn * self.vc / 4
#         self.P = self.fn * self.vc * self.Dc * self.kc / 240000
#         self.Mc = self.Pc * 30000 / (math.pi * self.n)
#         self.Ft = 0.5 * self.kc * self.Dc * self.fn * math.sin(2.44/2) / 2
#         self.Tc = self.lm / self.vf
#
#     def __str__(self):
#         return f'Dc = {self.Dc} \nfn = {self.fn} \nn = {self.n} \nlm = {self.lm} \nvc = {self.vc} ' \
#                f'\nvf = {self.vf} \nQ = {self.Q} \nPc = {self.Pc} \nMc = {self.Mc} \nFt = {self.Ft} \nTc = {self.Tc}'
#
#
# tungaloy123 = Calculator(10.9, 0.13, 1150, 77.84)
# print(tungaloy123)


# второй вариант с защищенными атрибутами и проверками
class Calculator:
    """Класс для расчета режимов резания"""

    def __init__(self, Dc, fn, n, lm):
        import math
        self.__Dc = self.__check_data(Dc)
        self.__fn = self.__check_data(fn)
        self.__n = self.__check_data(n)
        self.__lm = self.__check_data(lm)
        self.__kc = 2535
        self.__efficiency = 0.95
        self.__vc = self.__Dc * math.pi * self.__n / 1000
        self.__vf = self.__fn * self.__n
        self.__Q = self.__Dc * self.__fn * self.__vc / 4
        self.__Pc = self.__fn * self.__vc * self.__Dc * self.__kc / 240000
        self.__Mc = self.__Pc * 30000 / (math.pi * self.__n)
        self.__Ft = 0.5 * self.__kc * self.__Dc * self.__fn * math.sin(2.44 / 2) / 2
        self.__Tc = self.__lm / self.__vf

    @classmethod
    def __check_data(cls, data):
        if type(data) not in (int, float):
            raise TypeError("Входные значения должны быть целыми или вещественными числами")
        return data

    @staticmethod
    def __calculate_walter(self):
        '''калькулятор от walter'''
        import math
        self.__vc = self.__Dc * math.pi * self.__n / 1000
        self.__vf = self.fn * self.n
        self.__Q = (self.__vf * math.pi * pow(self.__Dc, 2)) / (4 * 1000)
        self.__Pc = (self.__Q * self.__kc) / (60000 * self.__efficiency)
        self.__Mc = pow(self.__Dc, 2) * self.__kc * self.__fn / 8000
        self.__Ft = 0.63 * (self.__fn * self.__Dc * self.__kc / 2)
        self.__Tc = self.__lm / self.__vf

    @staticmethod
    def __calculate_sandvik(self):
        '''калькулятор от sandvik'''
        import math
        self.__vc = self.__Dc * math.pi * self.__n / 1000
        self.__vf = self.__fn * self.__n
        self.__Q = self.__Dc * self.__fn * self.__vc / 4
        self.__Pc = self.__fn * self.__vc * self.__Dc * self.__kc / 240000
        self.__Mc = self.__Pc * 30000 / (math.pi * self.__n)
        self.__Ft = 0.5 * self.__kc * self.__Dc * self.__fn * math.sin(2.44 / 2) / 2
        self.__Tc = self.__lm / self.__vf

    def __str__(self):
        # добавить округление у значений
        return f'Dc = {self.__Dc} \nfn = {self.__fn} \nn = {self.__n} \nlm = {self.__lm} \nvc = {self.__vc} ' \
               f'\nvf = {self.__vf} \nQ = {self.__Q} \nPc = {self.__Pc} \nMc = {self.__Mc} \nFt = {self.__Ft} ' \
               f'\nTc = {self.__Tc}'


tungaloy123 = Calculator(10.9, 0.13, 1150, 77.84)
print(tungaloy123)
