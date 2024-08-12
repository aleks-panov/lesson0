class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        self.new_floor = new_floor
        num = self.number_of_floors
        new = list(range(1, new_floor + 1))
        for i in range(len(new)):
            if new_floor >= num:
                print("Такого этажа не существует")
                break
            if new[i] >= 1 and new[i] <= num:
                print(new[i])
            else:
                print("Такого этажа не существует")
                break


h1 = House("ЖК Горький", 18)
h2 = House("Домик в деревне", 2)
h1.go_to(5)
h2.go_to(10)
