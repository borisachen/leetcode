240. Search a 2D Matrix II  

Write an efficient algorithm that searches for a value in an m x n matrix. 
This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
For example,

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.

1. start at top right. 

class Solution(object):
		def searchMatrix(self, matrix, target):
		"""
		:type matrix: List[List[int]]
		:type target: int
		:rtype: bool
		"""
		if len(matrix)<1:
		    return False
		n = len(matrix) # n rows
		m = len(matrix[0]) # n cols
		i = 0
		j = m-1
		while i < n and j > 0:
			if matrix[i][j] == target:
				return True
			elif matrix[i][j] > target:
				j -= 1
			else: 
				i += 1
		return False