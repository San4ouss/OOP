class Laptop:
    def __init__(self, brand='', model='', price=''):
        self.brand = brand
        self.model = model
        self.price = price
        self.laptop_name = f"{self.brand} {self.model}"


laptop1 = Laptop()
laptop2 = Laptop()

hp = Laptop('hp', '15-bw0xx', 57000)
print(hp.price)  # выводит 57000
print(hp.laptop_name)  # выводит "hp 15-bw0xx"
