203. Remove Linked List Elements
Easy/673/41

Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
-----
Edge cases:
The linked list is empty, i.e. the head node is None.
Multiple nodes with the target value in a row.
The head node has the target value.
The head node, and any number of nodes immediately after it have the target value.
All of the nodes have the target value.
The last node has the target value.

-----
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head: return None
        cur = head
        while cur:
            if cur.next and cur.next.val == val:
                cur.next = cur.next.next
            cur = cur.next
        return head
