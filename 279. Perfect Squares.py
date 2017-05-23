279. Perfect Squares

Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.

1. DP approach
j = 1
dp[1] = 1
2 2
3 3
j=2
4 1
5 2
6 3
7 4
8 2

class Solution(object):
	def numSquares(self, n):
		"""
		:type n: int
		:rtype: int
		"""
