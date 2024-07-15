"""
module_5_2
"""
class House():
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors


    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print("Такого этажа не существует")
        else:
            for i in range(1, new_floor + 1):
                print(i)

    def __len__(self):
        """
        должен возвращать кол-во этажей здания self.number_of_floors.
        """
        return self.number_of_floors


    def __str__(self):
        """
        должен возвращать строку: "Название: <название>, кол-во этажей: <этажи>".
        """
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"


h1 = House('домик старого Тыквы', 1)
h2 = House('Empire State Building', 120)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))

#eof-module_5_2