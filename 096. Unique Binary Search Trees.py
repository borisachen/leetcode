96. Unique Binary Search Trees
Medium/1514/63

Given n, how many structurally unique BSTs (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BSTs.
"""
   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""

1.
dp[0] = 1
dp[1] = 1
dp[2] = 2
dp[3] = 5
dp[4] (1,2,3,4)

dp[0]*dp[3] +
dp[1]*dp[2] +
dp[2]*dp[1] +
dp[3]*dp[0]

dp[2]: for each dp[i-1] solution, add the new one to any open leaf node


class Solution(object):
	def numTrees(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		dp = [0] * (n+1)
		dp[0] = 1
		dp[1] = 1
		for i in range(2, n+1):
			for j in range(1, i+1):
				dp[i] += dp[j-1] * dp[i-j]
		return dp[n]


Solution().numTrees(3)
