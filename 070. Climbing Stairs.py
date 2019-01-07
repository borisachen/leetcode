70. Climbing Stairs
Easy
1613/62

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
-----

-----
# Standard DP
class Solution:
    def climbStairs(self, n):
        if n <= 2: return n
        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]

# O(1) memory
class Solution:
    def climbStairs(self, n):
        if n <= 2: return n
        a = 1
        b = 2
        for i in range(3,n+1):
            c = a + b
            a = b
            b = c
        return c


class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0: return 0
        if n == 1: return 1
        if n == 2: return 2
        else: return self.climbStairs(n-1) + self.climbStairs(n-2)
