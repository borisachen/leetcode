142. Linked List Cycle II

Given a linked list, return the node where the cycle begins. 
If there is no cycle, return null.

Note: Do not modify the linked list.

Follow up:
Can you solve it without using extra space?


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

a -> b -> c -> d 
1. naive: store seen nodes in a hashmap. if we see an element already in the hashmap, return that node

2. 
A = distance from head to start of cycle 
A+B = distance slow pointer travels
fast pointer must travel 2A+2B
let full cycle = N = how much more fast one has traveled
A+B+N = 2A+2B
N = A+B

class Solution(object):
	def detectCycle(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		if not head: return head
		slow = fast = head
		while fast and fast.next:
			slow = slow.next
			fast = fast.fast.next
			if fast == slow:
				slow2 = head
				while slow2 != slow:
					slow = slow.next
					slow2=slow2.next
				return slow
		return None