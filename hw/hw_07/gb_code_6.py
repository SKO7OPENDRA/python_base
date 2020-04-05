class Car:
    def __init__(self):
        self.modelues = []

    def __add__(self, other):
        self.modelues.append(other)

car = Car()
module_1 = 'теплый руль'
module_2 = 'подогрев сидения'

car + module_1  # car.__add__('123')
car + module_2
print(car.modelues)


