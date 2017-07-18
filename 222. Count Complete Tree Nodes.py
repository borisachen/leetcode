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

1. we can find the depth easily, dfs to the left
then we need to find the first part of the tree that doesnt go down to depth d

class Solution(object):
	def countNodes(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		h = height(root)
		

	def height(root):
		return -1 if not root else 1 + height(root.left)