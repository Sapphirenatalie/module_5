class House:

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):

        for new_floor in range(1, new_floor + 1):
            if new_floor > self.number_of_floors or new_floor < 1:
                print('Такого этажа не существует')

            else:

                print(f'Вы на этаже {new_floor}')


house_ = House('ЖК Эльбрус', 30)
print(house_.name, '- этажей:', house_.number_of_floors)

house_.go_to(12)
print('----------------')

house_1 = House('ЖК Горский', 18)
print(house_1.name, '- этажей:', house_1.number_of_floors)
house_1.go_to(18)
print('----------------')

house_2 = House('Домик в деревне', 2)
print(house_2.name, '- этажей:', house_2.number_of_floors)
house_2.go_to(10)
print('----------------')
