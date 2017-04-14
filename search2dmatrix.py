"""
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
"""
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
		n = len(matrix) # n rows
		m = len(matrix[0]) # n cols
		i = 0
		j = m-1
		while i < n and j > 0:
			if matrix[i][j] == target:
				return True
			elif matrix[i][j] > target:
				j -= 1
			else: #elif matrix[i][j] < target:
				i += 1
		return False