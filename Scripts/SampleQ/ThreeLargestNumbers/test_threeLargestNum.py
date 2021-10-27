import threeLargestNum as tln
import unittest as ut

class TestLargNum(ut.TestCase):
    def test_case_one(self):
        array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
        expected = [18, 141, 541]
        result = tln.findThreeLargestNumbers(array)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    ut.main()
