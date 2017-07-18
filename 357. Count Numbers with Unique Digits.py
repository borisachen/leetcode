357. Count Numbers with Unique Digits

Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10^n.

Example:
Given n = 2, return 91. (The answer should be the total numbers in the range of 0 ≤ x < 100, excluding [11,22,33,44,55,66,77,88,99])

1. 
dp[0] = 1
dp[1] = 10

class Solution(object):
	def countNumbersWithUniqueDigits(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		if n == 0: return 1
		ans = 10
		base = 9
		i = 2
		while i <= n and i <= 10:
			base = base * (9-i+2)
			ans += base
			i += 1
		return ans
		