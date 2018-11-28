138. Copy List with Random Pointer

A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

1. first pass, copy the normal list
second pass, use a dictionary / hashmap to store {random:sourcenode}

2. first pass, store a copy of all nodes in a dictionary {node : RandomListNode(node.label)}
second pass, assign next and random pointers

class Solution(object):
	def copyRandomList(self, head):
		"""
		:type head: RandomListNode
		:rtype: RandomListNode
		"""
		if not head: return head
		temp = head
		d = {}
		while temp:
			d[temp] = RandomListNode(temp.label)
			temp = temp.next
		temp = head
		while temp:
			d[temp].next = d[temp.next]
			d[temp].random = d[temp.random]
			node = node.next
		return d[head]


def copy_random_list(head):
	iter = head
	# 1 make copy, interleaved
	while iter:
		next = iter.next
		copy = RandomListNode(iter.val)
		iter.next = copy
		copy.next = next
		iter = next
	# 2 assign random pointer in copy nodes
	iter = head
	while iter:
		if iter.random:
			iter.next.random = iter.random.next
		iter = iter.next.next
	# 3 restore original list, and extract copy list
	iter = head
	pseudohead = RandomListNode(0)
	copyiter = pseudohead
	while iter:
		next = iter.next.next
		copy = iter.next
		copyiter.next = copy
		copyiter = copy
		iter.next = next
		iter = next
	return pseudohead.next