213. House Robber II

Note: This is an extension of House Robber.

After robbing those houses on that street, the thief has found himself a new place 
for his thievery so that he will not get too much attention. 
This time, all houses at this place are arranged in a circle. 
That means the first house is the neighbor of the last one. 
Meanwhile, the security system for these houses remain the same as for those in the previous street.

Given a list of non-negative integers representing the amount of money of each house, 
determine the maximum amount of money you can rob tonight without alerting the police.

1. we will always rob either the 1st or 2nd house, then having to omit the last house, or not omit it.
thus the solution is the maximum of the two sub problems:
max of rob[0:-1] and rob[1:]


class Solution(object):
	def rob(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		return max(self.rob_helper(nums[:-1]), self.rob_helper(nums[1:]))

	def rob_helper(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		a = b = 0
		for i in range(len(nums)):
			if i%2==0:
				a = max(a+nums[i], b)
			else:
				b = max(b+nums[i], a)
		return max(a,b)
