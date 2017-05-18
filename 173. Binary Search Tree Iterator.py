173. Binary Search Tree Iterator

Implement an iterator over a binary search tree (BST). 
Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.

1. store a stack, only keep 1 node from each level in memory.


# Definition for a  binary tree node
# class TreeNode(object):
#	 def __init__(self, x):
#		 self.val = x
#		 self.left = None
#		 self.right = None

class BSTIterator(object):
	def __init__(self, root):
		"""
		:type root: TreeNode
		"""
		self.stack = []
		if root: self.stack.append(root)
		if root.left: self.pushLeft(root.left)

	def hasNext(self):
		"""
		:rtype: bool
		"""
		if not stack: return False
		return True

	def next(self):
		"""
		:rtype: int
		"""
		top = stack.pop()
		self.pushLeft(top.right)
		return top.val

	def pushLeft(self, node):
		while node:
			self.stack.append(node.left)
			node = node.left

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
	