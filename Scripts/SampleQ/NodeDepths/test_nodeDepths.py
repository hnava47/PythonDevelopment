import nodeDepths as ndp
import unittest as ut

class TestNodeDepths(ut.TestCase):
    def test_case_one(self):
        root = ndp.BinaryTree(1)
        root.left = ndp.BinaryTree(2)
        root.left.left = ndp.BinaryTree(4)
        root.left.left.left = ndp.BinaryTree(8)
        root.left.left.right = ndp.BinaryTree(9)
        root.left.right = ndp.BinaryTree(5)
        root.right = ndp.BinaryTree(3)
        root.right.left = ndp.BinaryTree(6)
        root.right.right = ndp.BinaryTree(7)
        actual = ndp.nodeDepths(root)
        self.assertEqual(actual, 16)

if __name__ == '__main__':
    ut.main()
