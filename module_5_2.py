# Специальные методы класса
# Создайте новый класс House
# Создайте инициализатор для класса House,
# который будет задавать атрибут этажности self.numberOfFloors = 0
# Создайте метод setNewNumberOfFloors(floors),
# который будет изменять атрибут numberOfFloors
# на параметр floors и выводить в консоль numberOfFloors


class House:

    def __init__(self, name, floors):
        self.numberOfFloors = floors
        print('исходное кол-во этажей -', self.numberOfFloors)

    def __setNewNumberOfFloors__(self, floors):
        self.numberOfFloors = floors
        print('измененное кол-во этажей -', self.numberOfFloors)


house_1 = House('Многоквартирный дом', 10)
house_1.__setNewNumberOfFloors__(floors=8)
print()
house_1.__setNewNumberOfFloors__(int(input('Введите необходимое кол-во этажей: ')))
