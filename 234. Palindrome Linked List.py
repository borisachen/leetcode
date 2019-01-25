234. Palindrome Linked List
Easy/1353/206

Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
-----
None
1
1 2
s f
  n
p s
1 2 1
s f
  s   f
p   n

1 2 2 1
  s   f
p s n f
  p s     f
-----
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next: return True
        prev = None
        slow = head
        fast = head.next
        while fast and fast.next:
            n = slow.next
            slow.next = prev
            prev = slow
            slow = n
            fast = fast.next.next
        if fast:
            slow = slow.next
        # prev and slow should be the same
        while prev and slow:
            if prev.val != slow.val:
                return False
            prev = prev.next
            slow = slow.next
        return True
