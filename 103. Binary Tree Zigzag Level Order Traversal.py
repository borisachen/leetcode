103. Binary Tree Zigzag Level Order Traversal
Medium/842/55

Given a binary tree, return the zigzag level order traversal of its nodes values. (ie, from left to right, then right to left for the next level and alternate between).
"""
For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
"""
Regular BFS traversal with queue
keep a direction flag
if flag is -1, reverse each row before appending to solution array

time- o(n) visit each node once
space- O(n), solution array

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def zigzagLevelOrder(self, root):
		"""
		:type root: TreeNode
		:rtype: List[List[int]]
		"""
		if not root: return []
		queue = [root]
		res = []
		d = 1
		while queue:
			minires = []
			n = len(queue)
			for i in range(n):
				cur = queue[i]
				if cur.left: queue.append(cur.left)
				if cur.right: queue.append(cur.right)
				minires.append(cur.val)
			queue = queue[n:]
			minires = minires[::d]
			d = d*-1
			res.append(minires)
		return res
