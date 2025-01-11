import unittest


def skip_if_frozen(test_func):
    def wrapper(self):
        if self.is_frozen:
            print("Тесты в этом кейсе заморожены")
            self.skipTest("Тесты в этом кейсе заморожены")
        return test_func(self)

    return wrapper


class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).name}')
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


class RunnerTest(unittest.TestCase):
    is_frozen = False  # Измените на True, чтобы заморозить тесты

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner("Усэйн", 10)
        self.andrey = Runner("Андрей", 9)
        self.nik = Runner("Ник", 3)

    @skip_if_frozen
    def test_walk(self):
        try:
            runner = Runner("TestRunner", -5)
        except ValueError as e:
            pass

    @skip_if_frozen
    def test_run(self):
        try:
            runner = Runner("TestName", 5)
        except TypeError as e:
            pass

    @skip_if_frozen
    def test_challenge(self):
        runner1 = Runner("Бегун1", 7)
        runner2 = Runner("Бегун2", 5)

        for _ in range(10):
            runner1.run()
            runner2.walk()

        self.assertNotEqual(runner1.distance, runner2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True  # Измените на False, чтобы активировать тесты

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner("Усэйн", 10)
        self.andrey = Runner("Андрей", 9)
        self.nik = Runner("Ник", 3)

    @skip_if_frozen
    def test_usain_nik(self):
        tournament = Tournament(90, self.usain, self.nik)
        results = tournament.start()
        self.all_results['Usain & Nik'] = {place: str(runner) for place, runner in results.items()}
        self.assertTrue(results[max(results.keys())].name == self.nik.name)

    @skip_if_frozen
    def test_andrey_nik(self):
        tournament = Tournament(90, self.andrey, self.nik)
        results = tournament.start()
        self.all_results['Andrey & Nik'] = {place: str(runner) for place, runner in results.items()}
        self.assertTrue(results[max(results.keys())].name == self.nik.name)

    @skip_if_frozen
    def test_usain_andrey_nik(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nik)
        results = tournament.start()
        self.all_results['Usain, Andrey & Nik'] = {place: str(runner) for place, runner in results.items()}
        self.assertTrue(results[max(results.keys())].name == self.nik.name)


if __name__ == '__main__':
    unittest.main()
