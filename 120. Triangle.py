120. Triangle

Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

1. create a binary tree out of it, then do the usual search, however this requires O(m) space.
2. basically need a DFS search, since it is not sorted
keep track of the minimum so far. 
if at any path the sum so far is bigger than the minimum so far, then we can cut off all paths going thru that path
how do we navigate the paths?
	use j to keep track of the current depth
	if we are at position i for the previous level
	current level we can go to i or i+1

3. DP, bottom up
	dp[k][i] = min(dp[k+1][i], dp[k+1][i+1]) + triangle[k][i]
however, dp[k+1] is useless after we compute dp[k], 
so use a 1-d array and update itself iteratively:
	init: dp[i] = triangle[n][i]
	dp[i] = min(dp[i], dp[i+1]) + triangle[k][i]

time: o(n)
space: o(n)

class Solution(object):
	def minimumTotal(self, triangle):
		"""
		:type triangle: List[List[int]]
		:rtype: int
		"""
		n = len(triangle)
		dp = triangle[n-1]
		for j in range(0,n-1)[::-1]:
			for i in range(0,j+1):
				dp[i] = min(dp[i], dp[i+1]) + triangle[j][i]
		return dp[0]


Solution().minimumTotal([[1],[2,3]])