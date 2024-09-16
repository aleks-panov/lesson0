import time
from datetime import datetime
from threading import Thread

class Knight (Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f"{self.name} на нас напали")
        enemy  = 100
        day = 0
        for i in range(enemy):
            if enemy > 0:
                enemy -= self.power
                day += 1
                time.sleep(1.0)
                print(f"{self.name} сражается {day} день(дня)..., осталось {enemy} воинов.")
                if enemy <= 0:
                    print(f"{self.name} одержал победу спустя {day} дней(дня)!")


#Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
# Запуск потоков и остановка текущего
# Вывод строки об окончании сражения

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
print("Все битвы закончились")