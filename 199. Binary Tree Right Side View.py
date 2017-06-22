199. Binary Tree Right Side View 

Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
"""
For example:
Given the following binary tree,
   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
You should return [1, 3, 4]."""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

1. BFS iterative, store in queue
at the end of each level, add that to res

2. recursive, keep track of current depth
if depth == size of res, add it to res
this works if we recusively call the right first




class Solution(object):
	def rightSideView(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		if not root: return []
		queue = [root]
		res = []
		while queue:
			next_level = []
			for node in queue:
				if node.left: next_level.append(node.left)
				if node.right: next_level.append(node.right)
			if next_level: res.append(next_level[-1])
			queue = next_level
		return res







class Solution(object):
	def rightSideView(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		res = []
		self.dfs(root, res, 0)
		return res


	def dfs(self, node, res, level):
		if not node:
			return
		if level == len(res):
			res.append(node.val)
		self.dfs(node.right, res, level+1)
		self.dfs(node.left, res, level+1)



















class Solution(object):
	def rightSideView(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		res = []
		self.helper(root, res, 0)
		return res
	def helper(self, node, res, depth)
		if not node: 
			return
		if len(res)==depth: 
			res.append(node.val)
		self.helper(node.right, res, depth + 1)
		self.helper(node.left, res, depth + 1)
