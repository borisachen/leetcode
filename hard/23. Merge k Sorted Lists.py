23. Merge k Sorted Lists
Hard

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from Queue import PriorityQueue

# divide and conquer merge
k lists of size n
merge 2 lists: O(n)
k log k lists

O(n*k*logk)

class Solution(object):
	def mergeKLists(self, lists):
		"""
		:type lists: List[ListNode]
		:rtype: ListNode
		"""
		while len(lists) > 1:
			list0 = lists[0]
			list1 = lists[1]
			newlist = self.myMerge(list0, list1)
			lists.append(newlist)
		return lists[0]

	def myMerge(list0, list1):
		return


from Queue import PriorityQueue
class Solution(object):
	def mergeKLists(self, lists):
		"""
		:type lists: List[ListNode]
		:rtype: ListNode
		"""
		pq = PriorityQueue()
		dummy = ListNode(0)
		curr = dummy
		for node in lists:
			if node:
				pq.add((curr, curr.val))
		while pq:
			node = pq.pop()
			curr.next = ListNode(node.val)
			curr = curr.next
			pq.add((node.next, node.next.val))