from unittest import TestCase
import DZ


class TournamentTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = []
        return cls.all_results

    def setUp(self):
        self.run_1 = DZ.Runner('Уэсейн', 10)
        self.run_2 = DZ.Runner('Андрей', 10)
        self.run_3 = DZ.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for x in cls.all_results:
            print(x)

    def test_race_1(self):
        race_1 = DZ.Tournament(90, self.run_1, self.run_3)
        a = race_1.start()
        TournamentTest.all_results.append(a)
        self.assertTrue(a[2] == 'Ник')

    def test_race_2(self):
        race_2 = DZ.Tournament(90, self.run_2, self.run_3)
        b = race_2.start()
        TournamentTest.all_results.append(b)
        self.assertTrue(b[2] == 'Ник')

    def test_race_3(self):
        race_3 = DZ.Tournament(90, self.run_1, self.run_2, self.run_3)
        c = race_3.start()
        TournamentTest.all_results.append(c)
        self.assertTrue(c[3] == 'Ник')
