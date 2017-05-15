152. Maximum Product Subarray

Find the contiguous subarray within an array (containing at least one number) 
which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.

1. keep track of 

class Solution(object):
	def maxProduct(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		if not nums: return 0
		maxsofar = nums[0]
		maxhere = minhere = 0
		minpre = maxpre = nums[0]
		for i in range(1, len(nums)):
			maxhere = max(max(minpre * nums[i], maxpre * nums[i]), nums[i])
			minhere = min(max(minpre * nums[i], maxpre * nums[i]), nums[i])
			maxsofar = max(maxhere, maxsofar)
			maxpre = maxhere
			minpre = minhere
		return maxsofar
