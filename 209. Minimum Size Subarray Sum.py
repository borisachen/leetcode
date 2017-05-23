209. Minimum Size Subarray Sum

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.

1. two pointers
right move one at a time
each step, try to move left up as mmuch as possible while keeping current sum under s
	check if current length is better than current leader

class Solution(object):
	def minSubArrayLen(self, s, nums):
		"""
		:type s: int
		:type nums: List[int]
		:rtype: int
		"""
		left = 0
		curr_sum = 0
		res = len(nums)+1
		for right in range(len(nums)):
			curr_sum += nums[right]
			while curr_sum >= s:
				res = min(res, right-left+1)
				curr_sum -= nums[left]
				left += 1
		return result if result <= len(nums) else 0