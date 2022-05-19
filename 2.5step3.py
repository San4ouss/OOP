# class PizzaMaker:
#     def __make_pepperoni(self):
#         pass
#
#     def _make_barbecue(self):
#         pass
#
#
# maker = PizzaMaker()
# maker._make_barbecue()
# maker._PizzaMaker__make_pepperoni()
#
# print(PizzaMaker.__dict__.keys())
# # print(PizzaMaker.__dict__)
# print(maker._make_barbecue())
# print(maker._PizzaMaker__make_pepperoni())


class PizzaMaker:
    __x = 5
    __y = 3
    def __make_pepperoni(self):
        return self.__x

    def _make_barbecue(self):
        return self.__y


maker = PizzaMaker()
# maker._make_barbecue()
# maker._PizzaMaker__make_pepperoni()

print(PizzaMaker.__dict__.keys())
print(PizzaMaker.__dict__)
print(maker._make_barbecue())
print(maker._PizzaMaker__make_pepperoni())

print(maker._PizzaMaker__x)
print(maker._PizzaMaker__y)