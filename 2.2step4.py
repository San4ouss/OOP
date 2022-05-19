class Zebra:
    def __init__(self, count=0):
        self.count = count

    def which_stripe(self):
        self.count += 1
        print('Полоска белая' if self.count % 2 != 0 else 'Полоска черная')


z1 = Zebra()
z1.which_stripe()  # печатает "Полоска белая"
z1.which_stripe()  # печатает "Полоска черная"
z1.which_stripe()  # печатает "Полоска белая"

z2 = Zebra()
z2.which_stripe()  # печатает "Полоска белая"
