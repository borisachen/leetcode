213. House Robber II
Medium/686/21

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.
Example 2:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.

-----
1. we will always rob either the 1st or 2nd house, then having to omit the last house, or not omit it.
thus the solution is the maximum of the two sub problems:
max of rob[0:-1] and rob[1:]
-----

class Solution(object):
	def rob(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		if not nums: return 0
		n = len(nums)
		if n==1: return nums[0]
		a = self.rob_helper(nums,0,n-2)
		b = self.rob_helper(nums,1,n-1)
		return max(a,b)
		
	def rob_helper(self, nums, lo, hi):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		a = b = 0
		for i in range(lo, hi+1):
			if i%2==0:
				a = max(a+nums[i], b)
			else:
				b = max(b+nums[i], a)
		return max(a,b)
