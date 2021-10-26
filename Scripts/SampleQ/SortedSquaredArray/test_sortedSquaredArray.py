import sortedSquaredArray as ssa
import unittest as ut

class SortedSquared(ut.TestCase):
    def test_case_1(self):
        input = [1, 2, 3, 5, 6, 8, 9]
        expected = [1, 4, 9, 25, 36, 64, 81]
        actual = ssa.sortedSquaredArray(input)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    ut.main()
