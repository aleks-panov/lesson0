import Runner
import unittest


class RunnerTest (unittest.TestCase):
    def test_walk(self):
        runner1 = Runner.Runner('Alex')
        for walk in range(10):
            runner1.walk()
        self.assertEqual(runner1.distance, 50)

    def test_run(self):
        run1 = Runner.Runner('Alex')
        for run in range(10):
            run1.run()
        self.assertEqual(run1.distance, 100)
    def test_challenge(self):
        runner1 = Runner.Runner('Alex')
        run1 = Runner.Runner('Alex')
        for walk in range(10):
            runner1.walk()
        for run in range(10):
            run1.run()
        self.assertNotEqual(runner1.distance, run1.distance)