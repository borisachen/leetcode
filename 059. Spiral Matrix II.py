class Solution(object):
	def generateMatrix(self, n):
		top = left = d = 0
		right = bot = n
		temp = [0]*n
		res = []
		for i in range(n):
			res.append(list(temp))
		i = 1
		while i <= n*n:
			print d, top, right, bot, left, res
			if d == 0:
				for k in range(left, right):
					res[top][k] = i
					i += 1
				top += 1
			elif d == 1:
				for k in range(top, bot):
					res[k][right-1] = i
					i += 1
				right -= 1
			elif d == 2:
				for k in range(left, right)[::-1]:
					res[bot-1][k] = i
					i += 1
				bot -= 1
			elif d == 3:
				for k in range(top, bot)[::-1]:
					res[k][left] = i
					i += 1
				left += 1
			d = (d+1)%4
		return res

s = Solution()
s.generateMatrix(3)
s.generateMatrix(5)

"""
59. Spiral Matrix II

Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
0/top->right
1/right->down
2/bot->left
3/left->up
"""

		"""
		:type n: int
		:rtype: List[List[int]]
		"""

