104. Maximum Depth of Binary Tree
Easy
1035/43

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.

-----
-----

class Solution:
	def maxDepth(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		if root == None: 
			return 0
		return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
