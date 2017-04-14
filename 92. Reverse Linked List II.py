92. Reverse Linked List II

Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,
         m     n
return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list

--------------
pre->cur->nex
pre<-cur<-nex

edge cases:
m-1 -> n   : find and set marker at m-1, n
m   -> n+1 : find and set marker at m, n+1 

loop:
m+1 -> m
m+2 -> m+1
n   -> n-1
...up until m+x = n

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def reverseBetween(self, head, m, n):
		"""
		:type head: ListNode
		:type m: int
		:type n: int
		:rtype: ListNode
		"""
		if head==None or head.next==None: return head
		dummy = ListNode(0)
		dummy.next = head
		pre = ListNode(0)
		for i in range(0, m-1):
			pre = pre.next
		start = pre.next # a pointer to the beginning of a sub-list that will be reversed
		then = start.next # a pointer to a node that will be reversed
		for i in range(0,n-m):
			start.next = then.next
			then.next = pre.next
			pre.next = then
			then = start.next
		return dummy.next



public ListNode reverseBetween(ListNode head, int m, int n) {
    if(head == null) return null;
    ListNode dummy = new ListNode(0); // create a dummy node to mark the head of this list
    dummy.next = head;
    ListNode pre = dummy; // make a pointer pre as a marker for the node before reversing
    for(int i = 0; i<m-1; i++) pre = pre.next;
    
    ListNode start = pre.next; // a pointer to the beginning of a sub-list that will be reversed
    ListNode then = start.next; // a pointer to a node that will be reversed
    
    // 1 - 2 -3 - 4 - 5 ; m=2; n =4 ---> pre = 1, start = 2, then = 3
    // dummy-> 1 -> 2 -> 3 -> 4 -> 5
    
    for(int i=0; i<n-m; i++)
    {
        start.next = then.next;
        then.next = pre.next;
        pre.next = then;
        then = start.next;
    }
    
    // first reversing : dummy->1 - 3 - 2 - 4 - 5; pre = 1, start = 2, then = 4
    // second reversing: dummy->1 - 4 - 3 - 2 - 5; pre = 1, start = 2, then = 5 (finish)
    
    return dummy.next;
    
}