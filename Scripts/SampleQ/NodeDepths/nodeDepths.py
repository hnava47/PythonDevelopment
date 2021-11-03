# O(n) time | O(h) space - where n is the number of nodes in the Binary Tree and h is the height of the Binary Tree
def nodeDepths(root):
	sumOfDepth = 0
	stack = [{'node': root, 'depth': 0}]
	while len(stack) > 0:
		nodeInfo = stack.pop()
		node, depth = nodeInfo['node'], nodeInfo['depth']
		# moves onto next loop, does not continue to add depth/append
		if node is None:
			continue
		sumOfDepth += depth
		stack.append({'node': node.left, 'depth': depth + 1})
		stack.append({'node': node.right, 'depth': depth +1})
	return sumOfDepth

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
