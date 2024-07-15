"""
module_5_1

Задача "Developer - не только разработчик":
"""
class House():
    pass
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors


    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print("Такого этажа не существует")
        else:
            for i in range(1, new_floor + 1):
                print(i)


haus1 = House('Мое жилище', 9)
haus1.go_to(8)
haus1.go_to(-2)
haus2 = House('коттедж на Рублевке', 4)
haus2.go_to(666)

#eof-module_5_1.py