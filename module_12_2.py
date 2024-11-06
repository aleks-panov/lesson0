import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
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


class TournamentTest (unittest.TestCase):

    @classmethod
    def setUpClass (cls):
        cls.all_results = {}

    def setUp(self):
        self.man1 = Runner("Уссейн", 10)
        self.man2 = Runner("Андрей", 9)
        self.man3 = Runner("Ник", 3)


    def testturn1 (self):
        self.turn1 = Tournament(90, self.man1, self.man3)
        self.all_results = self.turn1.start()
        lust_runner_name = self.all_results[max(self.all_results.keys())].name
        self.assertTrue(lust_runner_name == "Ник")
        TournamentTest.all_results[1] = self.all_results

    def testturn2 (self):
        self.turn2 = Tournament(90, self.man2, self.man3)
        self.all_results = self.turn2.start()
        lust_runner_name = self.all_results[max(self.all_results.keys())].name
        self.assertTrue(lust_runner_name == "Ник")
        TournamentTest.all_results[2] = self.all_results

    def testturn3 (self):
        self.turn3 = Tournament(90, self.man1, self.man2, self.man3)
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
