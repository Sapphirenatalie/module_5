# Атрибуты и методы объекта
# Пункты задачи:
# Создайте класс House.
# Внутри класса House определите метод __init__, в который передадите название и кол-во этажей.
# Внутри метода __init__ создайте атрибуты объекта self.name и self.number_of_floors,
# присвойте им переданные значения.
# Создайте метод go_to с параметром new_floor
# и напишите логику внутри него на основе описания задачи.
# Создайте объект класса House с произвольным названием и количеством этажей.
# Вызовите метод go_to у этого объекта с произвольным числом.
# Пример результата выполнения программы:
# Исходные данные:

# h1 = House('ЖК Горский', 18)
# h2 = House('Домик в деревне', 2)
# h1.go_to(5)
# h2.go_to(10)
# Вывод на консоль:
# 1
# 2
# 3
# 4
# 5
# "Такого этажа не существует"

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
