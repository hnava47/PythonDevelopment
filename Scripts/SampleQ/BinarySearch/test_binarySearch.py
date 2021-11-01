import binarySearch as bs
import unittest as ut

class TestBinSearch(ut.TestCase):
    def test_case_one(self):
        array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
        target = 33
        expected = 3
        result = bs.binarySearch(array, target)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    ut.main()
