import module_12_1 as mod1
import module_12_2 as mod2
import unittest



class RunnerTest (unittest.TestCase):

    is_frozen = False

    @unittest.skipIf(is_frozen == True, "Кейсы в этом тесте заморожены")
    def test_walk(self):
        runner1 = mod1.Runner('Alex')
        for walk in range(10):
            runner1.walk()
        self.assertEqual(runner1.distance, 50)

    @unittest.skipIf(is_frozen == True, "Кейсы в этом тесте заморожены")
    def test_run(self):
        run1 = mod1.Runner('Alex')
        for run in range(10):
            run1.run()
        self.assertEqual(run1.distance, 100)

    @unittest.skipIf(is_frozen == True, "Кейсы в этом тесте заморожены")
    def test_challenge(self):
        runner1 = mod1.Runner('Alex')
        run1 = mod1.Runner('Alex')
        for walk in range(10):
            runner1.walk()
        for run in range(10):
            run1.run()
        self.assertNotEqual(runner1.distance, run1.distance)


class TournamentTest (unittest.TestCase):

    is_frozen = True

    @classmethod
    def setUpClass (cls):
        cls.all_results = {}

    def setUp(self):
        self.man1 = mod2.Runner("Уссейн", 10)
        self.man2 = mod2.Runner("Андрей", 9)
        self.man3 = mod2.Runner("Ник", 3)

    @unittest.skipIf(is_frozen == False, "Кейсы в этом тесте заморожены")
    def testturn1 (self):
        self.turn1 = mod2.Tournament(90, self.man1, self.man3)
        self.all_results = self.turn1.start()
        lust_runner_name = self.all_results[max(self.all_results.keys())].name
        self.assertTrue(lust_runner_name == "Ник")
        TournamentTest.all_results[1] = self.all_results

    @unittest.skipIf(is_frozen == False, "Кейсы в этом тесте заморожены")
    def testturn2 (self):
        self.turn2 = mod2.Tournament(90, self.man2, self.man3)
        self.all_results = self.turn2.start()
        lust_runner_name = self.all_results[max(self.all_results.keys())].name
        self.assertTrue(lust_runner_name == "Ник")
        TournamentTest.all_results[2] = self.all_results

    @unittest.skipIf(is_frozen == False, "Кейсы в этом тесте заморожены")
    def testturn3 (self):
        self.turn3 = mod2.Tournament(90, self.man1, self.man2, self.man3)
        self.all_results = self.turn3.start()
        lust_runner_name = self.all_results[max(self.all_results.keys())].name
        self.assertTrue(lust_runner_name == "Ник")
        TournamentTest.all_results[3] = self.all_results

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            results = {}
            for place, runner in result.items():
                results[place] = runner.name
            print(results)


if __name__ == '__main__':
     unittest.main()
