2. Add Two Numbers
Medium
6396/1670
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def addTwoNumbers(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		if not l1 and l2: return l2
		if not l2 and l1: return l1
		head = ListNode(0)
		curr = head
		carry = 0
		while l1 or l2:
			if l1:
				carry += l1.val
				l1 = l1.next
			if l2:
				carry += l2.val
				l2 = l2.next
			curr.next = ListNode(carry%10)
			curr = curr.next
			carry = carry/10
		if carry > 0:
			curr.next = ListNode(carry)
		return head.next









class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        # create iterators through the list
        i1, i2 = l1, l2
        sum = 0
        head = ListNode(0)
        curr = head
        while (i1 != None) | (i2 != None):
            if (i1 != None):
                sum += i1.val
                i1 = i1.next
            if (i2 != None):
                sum += i2.val
                i2 = i2.next
            curr.next = ListNode(sum % 10)
            curr = curr.next
            sum = sum/10

        # at the end, if sum is 1, then add a 1 to the master list
        if sum > 0:
            curr.next = ListNode(sum)

        return head.next
        """
        i1 = l1
        i2 = l2
        head = ListNode(0)
        curr = head
        carry = 0
        while (i1!=None) | (i2!=None):
            if i1!=None:
                carry += i1.val
                i1 = i1.next
            if i2!=None:
                carry += i2.val
                i2 = i2.next
            curr.next = ListNode(carry%10)
            curr = curr.next
            carry = carry/10
        if carry>0:
            curr.next = ListNode(carry)
        return head.next
