375. Guess Number Higher or Lower II

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, Ill tell you whether the number I picked is higher or lower.

However, when you guess a particular number x, and you guess wrong, you pay $x. You win the game when you guess the number I picked.

Example:

n = 10, I pick 8.

First round:  You guess 5, I tell you that its higher. You pay $5.
Second round: You guess 7, I tell you that its higher. You pay $7.
Third round:  You guess 9, I tell you that its lower. You pay $9.

Game over. 8 is the number I picked.

You end up paying $5 + $7 + $9 = $21.
Given a particular n ≥ 1, find out how much money you need to have to guarantee a win.

class Solution(object):
	import sys
	def getMoneyAmount(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		table = [[0]*(n+1) for x in range(n+1)]
		return DP(table, 1, n)

	def DP(t, s, e):
		if s >= e: return 0
		if t[s][e] != 0: return t[s][e]
		res = sys.maxint
		for x in range(s, e+1):
			temp = x + max(DP(t, s, x-1), DP(t, x+1, e))
			res = min(res, temp)
		t[s][e] = res
		return res

import sys
class Solution(object):
	def getMoneyAmount(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		table = [[0]*(n+1) for _ in range(n+1)]
		for j in range(2, n+1):
			for i in range(j-1, 0, -1):
				globalMin = sys.maxint
				for k in range(i+1, j):
					localMax = k + max(table[i][k-1], table[k+1][j])
					globalMin = min(globalMin, localMax)
				table[i][j] = i if i + 1 == j else globalMin
		return table[1][n]














