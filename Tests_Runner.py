import unittest
from unittest import TestCase
import Runar


class RunnerTest(TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        run_1 = Runar.Runner('Бегун_1')
        for i in range(10):
            run_1.walk()
        self.assertEqual(run_1.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        run_2 = Runar.Runner('Бегун_2')
        for i in range(10):
            run_2.run()
        self.assertEqual(run_2.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        run_3 = Runar.Runner('Бегун_3')
        run_4 = Runar.Runner('Бегун_4')
        for i in range(10):
            run_3.walk()
            run_4.run()
        self.assertNotEqual(run_3.distance, run_4.distance)
