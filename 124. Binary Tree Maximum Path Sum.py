124. Binary Tree Maximum Path Sum
DescriptionHintsSubmissionsDiscussSolution
Given a binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. 
The path must contain at least one node and does not need to go through the root.

For example:
Given the below binary tree,

       1
      / \
     2   3
Return 6.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def maxPathSum(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		maxvalue = -sys.maxint
		dfs(root)

	def dfs(self, node):
		if not node:
			return 0
		left = max(0, dfs(node.left))
		right = max(0, dfs(node.right))
		maxvalue = max(maxvalue, left + right + node.val)
		return max(left, right) + node.val