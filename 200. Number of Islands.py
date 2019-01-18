200. Number of Islands
Medium/1941/77

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example 1:

11110
11010
11000
00000
Answer: 1

Example 2:

11000
11000
00100
00011
Answer: 3

-----
1. DFS.
when we find a 1, increment counter and DFS flip them to 0.
note: in SINK, we have to check the bad cases that we quit/return under.
	if we dont, then well just sink the entire board.
-----
class Solution(object):
	def numIslands(self, grid):
		"""
		:type grid: List[List[str]]
		:rtype: int
		"""
		n, m = len(grid), len(grid[0])
		n_islands = 0
		for i in range(n):
			for j in range(m):
				if grid[i][j] == 1:
					n_islands += 1
					self.sink(i, j, grid, n, m)
		return n_islands

	def sink(i,j,grid, n, m):
		if i < 0 or j < 0 or i >= n or j >= m:
			return
		grid[i][j] = 0
		self.sink(i-1, j, grid, n, m)
		self.sink(i+1, j, grid, n, m)
		self.sink(i, j-1, grid, n, m)
		self.sink(i, j+1, grid, n, m)
