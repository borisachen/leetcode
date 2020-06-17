1019. Next Greater Node In Linked List
Medium/694/43

We are given a linked list with head as the first node.
Let's number the nodes in the list: node_1, node_2, node_3, ... etc.

Each node may have a next larger value:
for node_i, next_larger(node_i) is the node_j.val
such that j > i, node_j.val > node_i.val, and j is the smallest possible choice.
If such a j does not exist, the next larger value is 0.

Return an array of integers answer, where answer[i] = next_larger(node_{i+1}).

Note that in the example inputs (not outputs) below, arrays such as [2,1,5]
represent the serialization of a linked list with a head node value of 2, second
node value of 1, and third node value of 5.

Example 1:
Input: [2,1,5]
Output: [5,5,0]

Example 2:
Input: [2,7,4,3,5]
Output: [7,0,5,5,0]

Example 3:
Input:  [1,7,5,1,9,2,5,1]
Output: [7,9,9,9,0,5,0,0]

Note:
1 <= node.val <= 10^9 for each node in the linked list.
The given list has length in the range [0, 10000].

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
1. Naive:
for each node i, for loop from i to the end. Time: O(n^2), Space O(1)

2. Stack? Maintain a monotonic decreasing stack (value, index)
Push the current element onto the stack if:
- the stack is emtpy, or
- curr is less than or equal to the top element
If curr is greater than the top element, then pop until curr is less than
or equal to the top element (or the stack is empty). Then add curr to the stack.
"""

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        # Replicate the linked list to a list
        a = []
        curr = head
        while curr:
            a.append(curr.val)
            curr = curr.next
        # Maintain a decreasing stack of (value, index)
        s = []
        res = [0] * len(a)
        for i in range(len(a)):
            if not s or a[i] <= s[-1][0]:
                s.append((a[i], i))
            if a[i] > s[-1][0]:
                while s and a[i] > s[-1][0]:
                    top = s.pop()
                    res[top[1]] = a[i]
                s.append((a[i], i))
        return res

# We can also do this without converting to a list

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        i = 0
        n = 0
        curr = head
        while curr:
            curr = curr.next
            n += 1
        s = []
        res = [0] * n
        curr = head
        while curr:
            if not s or curr.val <= s[-1]['val']:
                s.append({'val': curr.val, 'idx': i})
            if curr.val > s[-1]['val']:
                while s and curr.val > s[-1]['val']:
                    top = s.pop()
                    res[top['idx']] = curr.val
                s.append({'val': curr.val, 'idx': i})
            curr = curr.next
            i += 1
        return res
