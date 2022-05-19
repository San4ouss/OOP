# class Date:
#     def __init__(self, day, month, year):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     @property
#     def date(self):
#         return f'{self.__get_formatted(self.day)}/{self.__get_formatted(self.month)}/{self.__get_formatted(self.year)}'
#
#     @property
#     def usa_date(self):
#         return f'{self.__get_formatted(self.month)}-{self.__get_formatted(self.day)}-{self.__get_formatted(self.year)}'
#
#     # def __get_formatted(self, x):
#     #     return str(x).rjust(4, '0') if x == self.year else str(x).rjust(2, '0')
#
#     @classmethod
#     def __get_formatted(cls, x):
#         return str(x).rjust(4, '0') if len(str(x)) > 2 else str(x).rjust(2, '0')
#
#
# d1 = Date(5, 10, 2001)
# d2 = Date(15, 3, 999)
#
# print(d1.date)  # 05/10/2001
# print(d1.usa_date)  # 10-05-2001
# print(d2.date)  # 15/03/0999
# print(d2.usa_date)  # 03-15-0999


class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @property
    def date(self):
        return f"{str(self.day).rjust(2, '0')}/{str(self.month).rjust(2, '0')}/{str(self.year).rjust(4, '0')}"

    @property
    def usa_date(self):
        return f"{str(self.month).rjust(2, '0')}-{str(self.day).rjust(2, '0')}-{str(self.year).rjust(4, '0')}"


d1 = Date(5, 10, 2001)
d2 = Date(15, 3, 999)

print(d1.date)  # 05/10/2001
print(d1.usa_date)  # 10-05-2001
print(d2.date)  # 15/03/0999
print(d2.usa_date)  # 03-15-0999
