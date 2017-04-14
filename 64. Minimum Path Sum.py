64. Minimum Path Sum
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        n row, m cols
        """
        n = len(grid)
        m = len(grid[0])
        dp = [[0]*m for i in [0]*n]
        dp[0][0] = grid[0][0]
        for i in range(n):
        	for j in range(m):
        		if i == 0 and j>0: dp[i][j] = grid[i][j] + dp[i][j-1]
        		elif j == 0 and i>0: dp[i][j] = grid[i][j] + dp[i-1][j]
        		else: 
        			dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[n-1][m-1]
        