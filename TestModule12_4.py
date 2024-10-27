import unittest
from unittest import TestCase
import Module12_4
import logging


class RunnerTest(TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            logging.info(f'test_walk" выполнен успешно')
            run_1 = Module12_4.Runner('Бегун_1', -5)
            for i in range(10):
                run_1.walk()
            self.assertEqual(run_1.distance, 50)
        except ValueError as e:
            logging.warning(f'Неверная скорость для Runner\n{e}')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            logging.info(f'"test_run" выполнен успешно')
            run_2 = Module12_4.Runner('Бегун_2', -5)
            for i in range(10):
                run_2.run()
            self.assertEqual(run_2.distance, 100)
        except ValueError as e:
            logging.warning(f'Неверная скорость для Runner\n{e}')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        run_3 = Module12_4.Runner('Бегун_3')
        run_4 = Module12_4.Runner('Бегун_4')
        for i in range(10):
            run_3.walk()
            run_4.run()
        self.assertNotEqual(run_3.distance, run_4.distance)


logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='utf-8',
                    format='%(asctime)s| %(levelname)s | %(message)s')
