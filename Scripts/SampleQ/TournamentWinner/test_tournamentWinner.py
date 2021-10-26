import tournamentWinner as tw
import unittest as ut

class TestWinner(ut.TestCase):
    def test_case_1(self):
        competitions = [["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]]
        results = [0, 0, 1]
        testResults = tw.tournamentWinner(competitions, results)
        self.assertEqual(testResults, 'Python')

# Allows to view results in console
if __name__ == '__main__':
    ut.main()
