141. Linked List Cycle
Easy 1235/94

Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.


Example 2:

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

-----
Approach 1:
Iterate and store seen nodes in a set.
Check if new node is in set
if yes, return True
if we hit the end, return False
Time: O(n) since we go through each node once
Space: O(n) since we store all nodes

Approach 2:
Tortoise and hare. If we have a fast and slow pointer (fast moves twice),
then if there is a cycle at some point fast = slow.
if there is not a cycle, fast will hit none.
-----

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# O(n) storage
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head: return False
        cur = head
        seen = set()
        while cur:
            if cur in seen:
                return True
            seen.add(cur)
            cur = cur.next
        return False

# O(1) storage, tortoise and hare

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head: return False
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
