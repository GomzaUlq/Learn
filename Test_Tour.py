import unittest
from unittest import TestCase
import Tour


class TournamentTest(TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = []
        return cls.all_results

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.run_1 = Tour.Runner('Уэсейн', 10)
        self.run_2 = Tour.Runner('Андрей', 10)
        self.run_3 = Tour.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for x in cls.all_results:
            print(x)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_race_1(self):
        race_1 = Tour.Tournament(90, self.run_1, self.run_3)
        a = race_1.start()
        TournamentTest.all_results.append(a)
        self.assertTrue(a[2] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_race_2(self):
        race_2 = Tour.Tournament(90, self.run_2, self.run_3)
        b = race_2.start()
        TournamentTest.all_results.append(b)
        self.assertTrue(b[2] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_race_3(self):
        race_3 = Tour.Tournament(90, self.run_1, self.run_2, self.run_3)
        c = race_3.start()
        TournamentTest.all_results.append(c)
        self.assertTrue(c[3] == 'Ник')
