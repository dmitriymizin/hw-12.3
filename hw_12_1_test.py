
import runner
import unittest

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, '')
    def test_walk(self):
        r1 = runner.Runner('Mini-Me')
        for i in range(10):
            r1.walk()
        self.assertEqual(r1.distance, 50)

    @unittest.skipIf(is_frozen, '')
    def test_run(self):
        r2 = runner.Runner('Tirion')
        for i in range(10):
            r2.run()
        self.assertEqual(r2.distance, 100)

    @unittest.skipIf(is_frozen, '')
    def test_challenge(self):
        r1 = runner.Runner('Mini-Me')
        r2 = runner.Runner('Tirion')
        for i in range(10):
            r1.walk()

        for i in range(10):
            r2.run()

        self.assertNotEqual(r1.distance, r2.distance)


if __name__ == '__main__':
    unittest.main()

