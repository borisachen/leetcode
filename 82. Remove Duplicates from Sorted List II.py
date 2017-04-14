82. Remove Duplicates from Sorted List II

Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def deleteDuplicates(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		if not head or not head.next:
			return head
		fakehead = ListNode(0)
		fakehead.next = head
		pre = fakehead
		curr = head
		while curr:
			while curr.next and curr.val == curr.next.val:
				curr = curr.next
			if pre.next = curr:
				prev = prev.next
			else:
				pre.next = curr
			curr = curr.next
		return fakehead.next