# Различие атрибутов класса и экземпляра
# Создайте новый класс Building с атрибутом total
# Создайте инициализатор для класса Building,
# который будет увеличивать атрибут количества созданных объектов класса Building total
# В цикле создайте 40 объектов класса Building и выведите их на экран командой print
# Полученный код напишите в ответ к домашнему заданию


class Building:
    total = 0

    def __init__(self, quantity, floors, types):
        self.numberOfFloors = floors
        self.buildingType = types
        Building.total = quantity

        for i in range(1, Building.total + 1):
            if i <= Building.total:
                print(f'Здание № {i}\n{self.buildingType}\n{self.numberOfFloors} этажей \n')


house = Building(40, 7, 'кирпичный дом')
