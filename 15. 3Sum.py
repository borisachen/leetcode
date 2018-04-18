15. 3Sum

Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
1. naive: 3x for loop, check sum. o(n^3)
2. sort, then fix one and bidirectional search.
nlogn to sort
n^2 for search
"""

class Solution(object):
	def threeSum(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		nums.sort()
		n = len(nums)
		ans = []
		for i in range(n):
			lo, hi = i+1, n-1
			while lo < hi:
				cursum = nums[i]+nums[lo]+nums[hi]
				if cursum == 0:
					ans.append([i, lo, hi])
				elif cursum > 0:
					hi -= 1
				else:
					lo += 1
		return ans

Solution().threeSum([-1, 0, 1, 2, -1, -4])
