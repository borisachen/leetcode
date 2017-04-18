102. Binary Tree Level Order Traversal

Given a binary tree, return the level order traversal of its nodes values. (ie, from left to right, level by level).
"""
For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""
strategy:
queue for BFS
add root to queue
init result = []
while queue is not empty:
	for each node on the queue, 
		pop,  add left, add right
		add popped to a list
	append list to result

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def levelOrder(self, root):
		"""
		:type root: TreeNode
		:rtype: List[List[int]]
		"""
		if not root: return []
		queue = []
		queue.append(root)
		res = []
		while queue:
			minires = []
			for node in queue:
				curr = queue[0]
				queue = queue[1:]
				if curr.left: queue.append(curr.left)
				if curr.right: queue.append(curr.right)
				








