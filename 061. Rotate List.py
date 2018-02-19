61. Rotate List

Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
	  p  c
Given 1->2->3->4->5->NULL and k = 2,
			p  c
return 4->5->1->2->3->NULL.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None: return None
        if head.next == None or k == 0: return head
        top = curr = head
        n = 1
        while curr.next != None:
        	curr = curr.next
        	n += 1
        k = k%n
        if n==k or k==0: return head
        prev = head
        curr = head
        for i in range(0, n-k):
        	prev = curr
        	curr = curr.next
        prev.next = None
        res = curr 
        while curr.next!=None:
        	curr = curr.next
        curr.next = top
        return res