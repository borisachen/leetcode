147. Insertion Sort List
Sort a linked list using insertion sort.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def insertionSortList(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		helper = ListNode(0) # dummy new head node
		helper.next = head 
		cur = head # current node to be inserted
		p = helper # pre node. cur will be inserted between [p, p.next]
		# while the current node is valid and needs to be sorted
		while cur:
			nex = cur.next # set pointer for next node to be inserted
			# find the correct pre node
			while p.next and p.next.val < cur.val:
				p = p.next # at the end of this while loop, p will be in the right place
			# insert cur between [p, p.next]
			p.next, cur.next = cur, p.next
			p = helper
			cur = nex
		return helper.next