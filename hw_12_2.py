import unittest
import runner_and_tournament

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.run1 = runner_and_tournament.Runner('Усэйн', 10)
        self.run2 = runner_and_tournament.Runner('Андрей', 9)
        self.run3 = runner_and_tournament.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for key, result in cls.all_results.items():
            print(f'{key}:{result}')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament(self):
        t1 = runner_and_tournament.Tournament(90, self.run1, self.run3)
        results = t1.start()
        self.all_results['test_tournament1'] = results
        last_place = max(results.keys())
        last_run = results[last_place]
        self.assertTrue(last_run == self.run3)

        t2 = runner_and_tournament.Tournament(90, self.run2, self.run3)
        results = t2.start()
        self.all_results['test_tournament2'] = results
        first_place = min(results.keys())
        last_place = max(results.keys())
        first_run = results[first_place]
        last_run = results[last_place]
        print("Результаты турнира:", results)
        for place, runner in results.items():
            print(f'Place {place}: {runner.name}')
        self.assertTrue(first_run == self.run2)
        self.assertTrue(last_run == self.run3)


        t3 = runner_and_tournament.Tournament(90, self.run1, self.run2, self.run3)
        results = t3.start()
        self.all_results['test_tournament3'] = results
        last_place = max(results.keys())
        last_run = results[last_place]
        self.assertTrue(last_run == self.run3)

if __name__ == '__main__':
    unittest.main()


