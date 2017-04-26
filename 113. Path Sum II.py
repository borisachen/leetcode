113. Path Sum II

Given a binary tree and a sum, find all root-to-leaf paths where each paths sum equals the given sum.
"""
For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]
"""
DFS, pass sum_so_far.
once sum_so_far exceeds target, break out
if we are at a leaf, check total sum==target. if matches, then add it to solution array.

time: for any binary tree, half of the nodes are on the leafs (n/2)
o(n)
space: suppose every path is valid, then there are n/2 paths, each path is logn deep.
o(nlogn)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def pathSum(self, root, sum):
		"""
		:type root: TreeNode
		:type sum: int
		:rtype: List[List[int]]
		"""
		res = []
		self.helper(node=root, running=0, target=sum, res=res, path=[])
		return res

	def helper(self, node, running, target, res, path):
		if not node: return
		running += node.val
		if not node.left and not node.right:
			if running == target:
				res.append(path+[node.val])
				return
		path.append(node.val)
		self.helper(node.left, running, target, res, path)
		self.helper(node.right, running, target, res, path)
		path.pop()
		return res









