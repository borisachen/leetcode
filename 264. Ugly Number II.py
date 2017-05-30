264. Ugly Number II

Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

Note that 1 is typically treated as an ugly number, and n does not exceed 1690.

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.

class Solution(object):
	def nthUglyNumber(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		if n < 0: return False
		if n == 1: return True
		t2 = t3 = t5 = 0
		dp = [0]*n
		for i in range(n):
			dp[i] = min(dp[t2]*2, dp[t3]*3, dp[t5]*5)
			if dp[i] == dp[t2]*2: t2 += 1
			if dp[i] == dp[t3]*3: t3 += 1
			if dp[i] == dp[t2]*5: t5 += 1
		return dp[-1]