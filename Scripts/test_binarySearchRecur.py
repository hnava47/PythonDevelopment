import unittest as ut
import binarySearchRecur as bsr

class TestBin(ut.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_one(self):
        array = [1, 10, 14, 90]
        val = 10
        result = bsr.binSearch(array, 0, len(array)-1, val)
        self.assertEqual(result, 1)

    def test_two(self):
        array = [-10, -9, -4, -3, -2]
        val = -2
        result = bsr.binSearch(array, 0, len(array)-1, val)
        self.assertEqual(result, 4)

if __name__ == '__main__':
    ut.main()
