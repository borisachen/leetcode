221. Maximal Square

Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1s and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 4.

dp[0][0] = 1 if its 1, else 0
init top row to 0 or 1
init first column to 0 or 1


class Solution(object):
	def maximalSquare(self, matrix):
		"""
		:type matrix: List[List[str]]
		:rtype: int
		"""
		n = len(matrix) # n rows
		m = len(matrix[0]) # m cols
		dp = [[0]*m for i in range(n)]
		# set the first row
		dp[0] = matrix[0]
		# set the first column
		for i in range(1,n):
			dp[i][0] = matrix[i][0]
		res = 0
		# iterate through 
		for i in range(1,n):
			for j in range(1, m):
				if matrix[i][j] == 1:
					dp[i][j] = min(min(dp[i-1][j-1], dp[i-1][j]), dp[i][j-1]) + 1
					res = max(res, dp[i][j])
		return res