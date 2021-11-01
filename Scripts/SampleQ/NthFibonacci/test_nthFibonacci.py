import nthFibonacci as nf
import unittest as ut

class TestNthFib(ut.TestCase):
    def test_case_one(self):
        n = 6
        expected = 5
        result = nf.getNthFib(n)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    ut.main()
