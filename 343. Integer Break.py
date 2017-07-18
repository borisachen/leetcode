343. Integer Break

Given a positive integer n, 
break it into the sum of at least two positive integers 
and maximize the product of those integers. 
Return the maximum product you can get.

For example, given n = 2, return 1 (2 = 1 + 1); given n = 10, return 36 (10 = 3 + 3 + 4).

1. DP
dp[i] = max product?
dp[i] = ? max of:
dp[i-1]*1
dp[i-2]*2
dp[i-3]*3

class Solution(object):
	def integerBreak(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		dp = [0]*(n+1)
		dp[1] = 1
		for i in range(2, n+1):
			for j in range(1, i):
				dp[i] = max(dp[i], max(j, dp[j]) * max(i-j,dp[i-j]))
		print dp
		return dp[-1]

Solution().integerBreak(2)
Solution().integerBreak(10)
