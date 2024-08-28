
import unittest
import hw_12_1_test
import hw_12_2

testing_suite = unittest.TestSuite()
testing_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(hw_12_1_test.RunnerTest))
testing_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(hw_12_2.TournamentTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(testing_suite)

