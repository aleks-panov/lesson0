class Horse:
    x_distance = 0
    sound = "Frrr"

    def __init__(self, x_distance):
        self.x_distance = x_distance

    def run(self, dx):
        self.x_distance += dx
        return self.x_distance


class Eagle:
    y_distance = 0
    Horse.sound = "I train, eat, sleep, and repeat"

    def __init__(self, y_distance):
        self.y_distance = y_distance

    def fly(self, dy):
        self.y_distance += dy
        return self.y_distance


class Pegasus(Horse, Eagle):
    def __init__(self):
        Horse.x_distance
        Eagle.y_distance

    def move(self, dx, dy):
        Horse.run(self, dx)
        Eagle.fly(self, dy)

    def get_pos(self):
        Horse.x_distance
        Eagle.y_distance
        return (self.x_distance, self.y_distance)

    def voice(self):
        print(Horse.sound)


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()