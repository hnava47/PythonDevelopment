import unittest
from blackjack3 import Hand, Strategy

class TestBlackjack(unittest.TestCase):

    def test_score_one(self):
        a = Hand([3, 12])
        ret = a.score()
        self.assertEqual(ret,(13, 0))

    def test_score_two(self):
        a = Hand([5, 5, 10])
        ret = a.score()
        self.assertEqual(ret,(20, 0))

    def test_score_three(self):
        a = Hand([11, 10, 1])
        ret = a.score()
        self.assertEqual(ret, (21, 0))

    def test_score_four(self):
        a = Hand([1, 5])
        ret = a.score()
        self.assertEqual(ret, (16, 1))

    def test_score_five(self):
        a = Hand([1,1, 5])
        ret = a.score()
        self.assertEqual(ret, (17, 1))

    def test_score_six(self):
        a = Hand([1, 1, 1, 7])
        ret = a.score()
        self.assertEqual(ret, (20, 1))

    def test_score_seven(self):
        a = Hand([7, 8, 10])
        ret = a.score()
        self.assertEqual(ret, (25, 0))

    def test_stand_one(self):
        a = Hand([1, 1, 5])
        b = Strategy(17, True)
        ret = b.stand(a)
        self.assertEqual(ret, True)

    def test_stand_two(self):
        a = Hand([1, 1, 5])
        b = Strategy(17, False)
        ret = b.stand(a)
        self.assertEqual(ret, False)

    def test_stand_three(self):
        a = Hand([10, 7])
        b = Strategy(17, True)
        ret = b.stand(a)
        self.assertEqual(ret, True)

    def test_stand_four(self):
        a = Hand([10, 7])
        b = Strategy(17, False)
        ret = b.stand(a)
        self.assertEqual(ret, True)

if __name__ == "__main__":
    unittest.main()
