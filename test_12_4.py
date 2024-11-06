import module_12_1 as mod1
import unittest
import logging

logging.basicConfig(level=logging.INFO,
                    filemode="w",
                    filename="runner_tests.log",
                    encoding="UTF-8",
                    format="%(asctime)s | %(levelname)s | %(message)s")


class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

class RunnerTest (unittest.TestCase):

    is_frozen = False

    @unittest.skipIf(is_frozen == True, "Кейсы в этом тесте заморожены")
    def test_walk(self):
        try:
            runner1 = mod1.Runner('Alex', -5)
            for walk in range(10):
                runner1.walk()
            self.assertEqual(runner1.distance, 50)
            logging.INFO("test_walk выполнен успешно")
        except:
            logging.warning("Неверная скорость для Runner")

    @unittest.skipIf(is_frozen == True, "Кейсы в этом тесте заморожены")
    def test_run(self):
        try:
            run1 = mod1.Runner(5)
            for run in range(10):
                run1.run()
            self.assertEqual(run1.distance, 100)
            logging.INFO("test_run выполнен успешно")
        except:
            logging.warning("Неверный тип данных для объекта Runner")

    @unittest.skipIf(is_frozen == True, "Кейсы в этом тесте заморожены")
    def test_challenge(self):
        runner1 = mod1.Runner('Alex')
        run1 = mod1.Runner('Alex')
        for walk in range(10):
            runner1.walk()
        for run in range(10):
            run1.run()
        self.assertNotEqual(runner1.distance, run1.distance)

# first = Runner('Вося', 10)
# second = Runner('Илья', 5)
# # third = Runner('Арсен', 10)
#
# t = Tournament(101, first, second)
# print(t.start())