63. Unique Paths II
DescriptionHintsSubmissionsDiscussSolution
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.

Note: m and n will be at most 100.
'''
dp
dp[i][j] = number of unique ways to get to matrix[i][j]
transition function:
dp[i][j] = 
	dp[i-1][j] + dp[i][j-1] if matrix[i][j]==0
	else 0
init:
dp[i][0] = 1 for all i
dp[0][j] = 1 for all j
return d
'''
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        