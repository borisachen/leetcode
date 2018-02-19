85. Maximal Rectangle

Given a 2D binary matrix filled with 0's and 1's, 
find the largest rectangle containing only 1s and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 6.

class Solution(object):
	def maximalRectangle(self, matrix):
		"""
		:type matrix: List[List[str]]
		:rtype: int
		"""
		if not matrix: return 0
		maxarea = 0
		n, m = len(matrix), len(matrix[0])
		height = [0]*m
		left = [0]*m
		right = [m]*m
		for i in range(n):
			# update height
			curleft = 0
			curright = m
			for j in range(m):
				if matrix[i][j] == '1':
					height[j] = height[j] + 1
				else:
					height[j] = 0
			# update left
			for j in range(m):
				if matrix[i][j] == '1':
					left[j] = max(curleft, left[j])
				else:
					left[j] = 0
					curleft = j + 1
			# update right
			for j in range(m)[::-1]:
				if matrix[i][j] == '1':
					right[j] = min(curright, right[j])
				else:
					right[j] = m
					curright = j
			#print height
			#print left
			#print right
			for j in range(m):
				maxarea = max(maxarea, height[j]*(right[j]-left[j]))
		return maxarea

#Solution().maximalRectangle(["10100","10111","11111","10010"])
Solution().maximalRectangle(["1"])

