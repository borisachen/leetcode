329. Longest Increasing Path in a Matrix

Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

nums = [
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
Return 4
The longest increasing path is [1, 2, 6, 9].

Example 2:

nums = [
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
Return 4
The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.


class Solution(object):
	def longestIncreasingPath(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: int
		"""
		res = 0
		for i in range(len(matrix[0])):
			for j in range(len(matrix)):
				backtrack(matrix, res, path=[], x=i, y=j)

	def backtrack(self, matrix, res, path, x, y):
		if x < 0 or y < 0 or x >= len(matrix[0]) or y >= len(matrix):
			return
		if path:
			prev_x, prev_y = path[-1]
			if matrix[x][y] <= matrix[prev_x][prev_y]:
				return
		if (x,y) in path:
			return
		# otherwise, (x,y) is valid!
		if len(path) > res:
			res = len(path)
		backtrack(matrix, res, path+(x+1,y), x+1, y)
		backtrack(matrix, res, path+(x-1,y), x-1, y)
		backtrack(matrix, res, path+(x,y+1), x, y+1)
		backtrack(matrix, res, path+(x,y-1), x, y-1)