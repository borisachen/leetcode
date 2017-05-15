143. Reorder List

Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You must do this in-place without altering the nodes values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

1. find the midpoint
2. reverse the second half
3. interleave the two halfs

class Solution(object):
	def reorderList(self, head):
		"""
		:type head: ListNode
		:rtype: void Do not return anything, modify head in-place instead.
		"""
		if not head: return
		# 1. find midpoint
		slow = fast = head
		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next
		# 2. reverse second half
		pre = None
		node = slow
		while node:
			pre, node.next, node = node, pre, node.next
		# 3. merge in place
		first = head
		second = pre
		while second.next:
			first.next, first = second, first.next
			second.next, second = first, second.next
		return