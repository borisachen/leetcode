class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        flip top-bottom
		swap symmetry along diagonal
        """
        i=0
        j=len(matrix)-1
        while i < j:
        	matrix[i], matrix[j] = matrix[j], matrix[i]
        	i+=1
        	j-=1
        for i in range(0, len(matrix)):
        	for j in range(i, len(matrix[0])):
        		matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]