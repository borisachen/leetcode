279. Perfect Squares

Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.

1. DP

class Solution(object):
	def numSquares(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		dp = [0]
		eligible_squares = [x*x for x in range(1,n) if x*x < n]
		while len(dp) <= n+1:
			i = len(dp)
			smallest = 999999
			for s in eligible_squares:
				if i-s >= 0:
					smallest = min(smallest, dp[i-s]+1)
			dp.append(smallest)
		return dp[-1]



2. BFS

class Solution(object):
	def numSquares(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		currLevel = [0]
		nextLevel = []
		eligible_squares = [x*x for x in range(1,n) if x*x < n]
		depth = 0
		seen = {}
		while currLevel:
			depth += 1
			for v in currLevel:
				for e in eligible_squares:
					nextVal = v + e
					if nextVal == n: 
						return depth
					elif nextVal > n: 
						continue
					elif nextVal not in seen:
						seen[nextVal] = 1
						nextLevel.append(nextVal)
		return -1