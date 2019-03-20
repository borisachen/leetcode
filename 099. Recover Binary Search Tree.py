99. Recover Binary Search Tree
Hard/692/41

Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Note:
A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?

'''
Suppose inorder traversal prints out 6,3,4,5,2
A BST inorder traversal should print elements out in order. This means that 6
and 2 need to be swapped. We reduce the problem to finding the 6 and finding the 2.

Maintain prev pointer. When prev > cur, set FIRST at prev.
Then, when prev > cur again, set SECOND at cur.
Swap FIRST and SECOND, then we are done.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def recoverTree(self, root):
		"""
		:type root: TreeNode
		:rtype: void Do not return anything, modify root in-place instead.
		"""
		first = None
		second = None
		prev = TreeNode(-sys.maxint)
		self.dfs(root, first, second, prev)
		first.val, second.val = second.val, first.val

	def dfs(self, root):
		if not root:
			return
		self.dfs(root.left, first, second, prev)
		if first == None and prev.val >= root.val:
			first = prev
		if first != None and prev.val >= root.val:
			second = root
		prev = root
		self.dfs(root.right, first, second, prev)
