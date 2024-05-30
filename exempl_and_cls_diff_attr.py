class Building:
    total = 0

    def __init__(self, name):
        self.name = name


while Building.total < 40:
    Building.total += 1
    house = Building(f'house {Building.total}')
    print(house.name)
