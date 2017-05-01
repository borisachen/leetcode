117. Populating Next Right Pointers in Each Node II

Follow up for problem "Populating Next Right Pointers in Each Node.

What if the given tree could be any binary tree? Would your previous solution still work?

Note:

You may only use constant extra space.
"""
For example,
Given the following binary tree,
         1
       /  \
      2    3
     / \    \
    4   5    7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL
"""

at each step,
	set tail.next to be curr.left
	? set tail to be tail.next (if tail.next exists)
	set tail.next to be curr.right
	? set tail to be tail.next (if tail.next exists)
	move curr to the next curr 
	if curr is null, means we have hit the end of the row, so:
		set tail to be dummy
		set root to be dummy.next

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
		tail = dummy = TreeLinkNode(0)
		while root:
			tail.next = root.left
			if tail.next:
				tail = tail.next
			tail.next = root.right
			if tail.next:
				tail = tail.next
			root = root.next
			if not root:
				tail = dummy
				root = dummy.next