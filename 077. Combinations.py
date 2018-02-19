77. Combinations

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

class Solution(object):
	def combine(self, n, k):
		"""
		:type n: int
		:type k: int
		:rtype: List[List[int]]
		"""
		res = []
		nums = range(1, n+1)
		def backtrack(temp, start):
			if len(temp)==k:
				res.append(temp)
				return
			for i in range(start, n):
				if len(temp) < k:
					temp = temp + [nums[i]]
					backtrack(temp, i+1)
					temp = temp[:-1]
		backtrack([], 0)
		return res

Solution().combine(4,2)
