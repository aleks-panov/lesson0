import unittest

class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name

class RunnerTest (unittest.TestCase):
    def test_walk(self):
        runner1 = Runner('Alex')
        for walk in range(10):
            runner1.walk()
        self.assertEqual(runner1.distance, 50)

    def test_run(self):
        run1 = Runner('Alex')
        for run in range(10):
            run1.run()
        self.assertEqual(run1.distance, 100)
    def test_challenge(self):
        runner1 = Runner('Alex')
        run1 = Runner('Alex')
        for walk in range(10):
            runner1.walk()
        for run in range(10):
            run1.run()
        self.assertNotEqual(runner1.distance, run1.distance)