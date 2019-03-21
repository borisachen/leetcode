106. Construct Binary Tree from Inorder and Postorder Traversal

Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

postorder implies the last element is the root node
find that element in inorder, say its position j
the elements right of j in inorder will belong to the right node
the elements left of j in inorder will belong to the left node
if we process the right node first,

left node:
right node:


class Solution(object):
	def buildTree(self, inorder, postorder):
		"""
		:type inorder: List[int]
		:type postorder: List[int]
		:rtype: TreeNode
		"""
		if not inorder or not postorder:
			return None
		root = TreeNode(postorder.pop())
		j = inorder.index(root.val)
		root.right = self.buildTree(inorder[j+1:], postorder)
		root.left = self.buildTree(inorder[:j], postorder)
		return root
