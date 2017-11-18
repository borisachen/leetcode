19. Remove Nth Node From End of List
DescriptionHintsSubmissionsDiscussSolution
Discuss Pick One
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.
"""
0
1->2->3->4->5
d     c 
two pointers, curr and tail
iterate curr n spots
then iterate both until curr hits the end

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def removeNthFromEnd(self, head, n):
		"""
		:type head: ListNode
		:type n: int
		:rtype: ListNode
		"""
		curr = head
		for _ in xrange(n):
			curr = curr.next
		tail = head
		while head.next:
			head = head.next
			tail = tail.next
		tail.next = tail.next.next
		return head