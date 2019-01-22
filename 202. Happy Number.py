202. Happy Number
Easy/716/166

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example:

Input: 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
-----
Approach 1:
Store each seen number in a set or hashmap, check for membership.
Time O(n), Space O(n)

Approach 2:
This is just cycle detection, so we can use tortoise and hare,
fast pointer will eventually catch up to slow if there is a loop.
Time O(n), Space O(1)
-----

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==1: return True
        slow = n
        fast = self.breakdown(n)
        while fast != slow:
            slow = self.breakdown(slow)
            fast = self.breakdown(fast)
            fast = self.breakdown(fast)
            if fast == 1 or slow == 1:
                return True
        return False
    def breakdown(self, n):
        res = 0
        while n > 0:
            res += (n % 10) ** 2
            n /= 10
        return res



class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        num= n
        if n==1: return True
        seen = set()
        seen.add(n)
        while True:
            n = len(str(num))
            x = [str(num)[i] for i in range(n)]
            y = [int(x[i])*int(x[i]) for i in range(n)]
            num = sum(y)
            if num == 1:
                return True
            if num in seen:
                return False
            seen.add(num)
        return True
