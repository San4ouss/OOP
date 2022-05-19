class Building:
    def __init__(self, floor):
        self.floor = [None] * floor

    def __setitem__(self, key, value):
        self.floor[key] = value

    def __getitem__(self, item):
        return self.floor[item]

    def __delitem__(self, key):
        del self.floor[key]


iron_building = Building(22)  # Создаем здание с 22 этажами
print(iron_building.floor)
iron_building[0] = 'Reception'
iron_building[1] = 'Oscorp Industries'
iron_building[2] = 'Stark Industries'
print(iron_building.floor)
print(iron_building[2])
del iron_building[2]
print(iron_building[2])
