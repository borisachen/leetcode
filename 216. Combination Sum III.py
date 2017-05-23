216. Combination Sum III 

Find all possible combinations of k numbers that add up to a number n, 
given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Example 1:
Input: k = 3, n = 7
Output:
[[1,2,4]]

Example 2:
Input: k = 3, n = 9
Output:
[[1,2,6], [1,3,5], [2,3,4]]

1. backtracking 

class Solution(object):
	def combinationSum3(self, k, n):
		"""
		:type k: int
		:type n: int
		:rtype: List[List[int]]
		"""
		res = []
		self.backtrack(res, k, n, temp=[], start=1)
		return res
	def backtrack(self, res, k, n, temp, start):
		if len(temp) == k and sum(temp) == n:
			res.append(temp)
		for i in range(start, 10):
			if len(temp) < k and sum(temp) < n:
				temp = temp + [i]
				self.backtrack(res, k, n, temp, i+1)
				temp = temp[:-1]

Solution().combinationSum3(3,7)