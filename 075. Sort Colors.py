75. Sort Colors

Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, 
with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the librarys sort function for this problem.


class Solution(object):
	def sortColors(self, nums):
		"""
		:type nums: List[int]
		:rtype: void Do not return anything, modify nums in-place instead.
		iterate: 
			if 0, put it on left, go to next from left
			if 2, put it on right, go to next from right
			if 1, 
		"""
		lo = 0
		hi = len(nums)-1
		i = 0
		while i < hi:
			if nums[i]==0:
				nums[i], nums[lo] = nums[lo], nums[i]
				i+=1
				lo+=1
			elif nums[i]==2:
				nums[i], nums[hi] = nums[hi], nums[i]
				hi-=1
			else:
				i+=1