import unittest
from autompg2 import autompg, Record

class TestAutoMPG(unittest.TestCase):

    def test_auto_str(self):
        a = autompg("buick","skylark 320",1970,15.0)
        ret = str(a)
        self.assertEqual(ret,"buick, skylark 320, 1970, 15.0")

    def test_auto_repr(self):
        a = autompg("buick","skylark 320",1970,15.0)
        ret = repr(a)
        self.assertEqual(ret,"buick, skylark 320, 1970, 15.0")

    def test_auto_eql_one(self):
        a = autompg("buick","skylark 320",1970,15.0)
        b = autompg("chevrolet","chevelle malibu",1970,18.0)
        self.assertEqual(a == b, False)

    def test_auto_eql_two(self):
        a = autompg("chevrolet","chevelle malibu",1970,18.0)
        b = autompg("chevrolet","chevelle malibu",1970,18.0)
        self.assertEqual(a == b, True)

    def test_auto_lt(self):
        a = autompg("buick","skylark 320",1970,15.0)
        b = autompg("chevrolet","chevelle malibu",1970,18.0)
        self.assertEqual(a < b, False)

    def tuple_test(self):
        a = Record.record
        ret = a("18.0", "8", "307.0", "130.0", "3504.", "12.0", "70", "1", "chevrolet chevelle malibu")
        self.assertEqual(ret, record(mpg='18.0', cylinders='8', displacement='307.0', horsepower='130.0', weight='3504.', acceleration='12.0', modelYear='70', origin='1', carName='chevrolet chevelle malibu'))

if __name__ == "__main__":
    unittest.main()
