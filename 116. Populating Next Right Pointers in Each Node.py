116. Populating Next Right Pointers in Each Node

Given a binary tree

    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
For example,
Given the following perfect binary tree,
         1
       /  \
      2    3
     / \  / \
    4  5  6  7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \  / \
    4->5->6->7 -> NULL


the top level is already done
consider two levels at a time
iterate through level 1 and 
set left -> right
set right -> curr.next.left

# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
	# @param root, a tree link node
	# @return nothing
	def connect(self, root):
		curr = root
		while curr and curr.left:
			next = curr.left
			while curr:
				curr.left.next = curr.right
				curr.right.next = curr.next and curr.next.left
				curr = curr.next
			curr = next



















class Solution(object):
	# @param root, a tree link node
	# @return nothing
	def connect(self, root):
		while root and root.left:
			next = root.left
			while root:
				root.left.next = root.right
				root.right.next = root.next and root.next.left
				root = root.next
			root = next


			