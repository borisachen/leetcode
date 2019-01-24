206. Reverse Linked List
Easy/1831/48

Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?

-----
Generic case
   h
d->1->2->3->4->5->NULL
            p  c  n

0) empty list

1) one item list
   h
d->1->NULL

2) two item list
   h
d->1->2->NULL
   p  c  n

-----
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Iterative
class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return None
        prev = head
        curr = head.next
        next = curr.next if curr else None
        prev.next = None
        while curr:
            curr.next = prev
            prev = curr
            curr = next
            if next: next = next.next
        return prev

# Recursive

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.rev(None, head)
    def rev(self, prev, node):
        if not node:
            return prev
        next = node.next
        node.next = prev
        return self.rev(node, next)
