154. Find Minimum in Rotated Sorted Array II

Follow up for "Find Minimum in Rotated Sorted Array:
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

The array may contain duplicates.

1. binary search
if lo < hi, then return lo
if lo < mid, then look right
if lo > mid, then look left
if lo == mid, then move left up

class Solution(object):
	def findMin(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		lo = 0
		hi = len(nums)-1
		while lo < hi:
			if nums[lo] < nums[hi]:
				return nums[lo]
			mid = lo + (hi-lo)/2
			if nums[lo] < nums[mid]:
				lo = mid+1
			elif nums[lo] > nums[mid]
				hi = mid
			else:
				lo += 1
		return nums[lo]