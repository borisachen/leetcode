222. Count Complete Tree Nodes

Given a complete binary tree, count the number of nodes.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def countNodes(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		import math
		left_depth = leftDepth(root)
		right_depth = rightDepth(root)
		if left_depth == right_depth:
			return (1 << left_depth) - 1
		else:
			return 1 + self.countNodes(root.left) + self.countNodes(root.right)

	def leftDepth(root):
		d = 0
		while root:
			root = root.left
			d += 1
		return d

	def rightDepth(root):
		d = 0
		while root:
			root = root.right
			d += 1
		return d