import quickSort as qst
import unittest as ut

class TestQuickSort(ut.TestCase):
    def test_case_one(self):
        array = [8, 5, 2, 9, 5, 6, 3]
        result = qst.quickSort(array)
        expected = [2, 3, 5, 5, 6, 8, 9]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    ut.main()
