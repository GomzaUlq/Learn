import unittest
import Test_Tour
import Tests_Runner

test_tour = unittest.TestSuite()
test_runner = unittest.TestSuite()

test_tour.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_Tour.TournamentTest))
test_runner.addTest(unittest.TestLoader().loadTestsFromTestCase(Tests_Runner.RunnerTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(test_tour)
runner.run(test_runner)
