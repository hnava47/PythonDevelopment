import branchSums as bsm
import unittest as ut

class TestBranchSums(ut.TestCase):
    def test_case_one(self):
        root = bsm.BST(1)
        root.left = bsm.BST(2)
        root.left.left = bsm.BST(4)
        root.left.left.left = bsm.BST(8)
        root.left.left.right = bsm.BST(9)
        root.left.right = bsm.BST(5)
        root.left.right.left = bsm.BST(10)
        root.right = bsm.BST(3)
        root.right.left = bsm.BST(6)
        root.right.right = bsm.BST(7)
        result = bsm.branchSums(root)
        expected = [15, 16, 18, 10, 11]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    ut.main()
