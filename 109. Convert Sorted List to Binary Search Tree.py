109. Convert Sorted List to Binary Search Tree

Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

-------------
if it was an array,
then we can go to the middle element, set it to the be the root
left half goes to the left node
right half goes to the right node


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

time: at the end, we have a BST, log n depth. however, at each level we need to traverse the entire list o(n)
o(nlogn)
space: at each call, we use o(1) space. however recurssive methods call ==> logn calls
o(logn)

class Solution(object):
	def sortedListToBST(self, head):
		"""
		:type head: ListNode
		:rtype: TreeNode
		"""
		if not head: 
		    return
		if not head.next: 
		    return TreeNode(head.val)
		slow = head
		fast = head.next.next
		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next
		temp = slow.next
		root = TreeNode(temp.val)
		slow.next = None
		root.left = self.sortedListToBST(head)
		root.right = self.sortedListToBST(temp.next)
		return root