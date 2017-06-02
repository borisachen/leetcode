153. Find Minimum in Rotated Sorted Array
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.

1. binary search
base case is if everything is in order, then return the first/lowest element
if n[lo] < n[hi], return lo
if n[lo] <  n[mid], then look in right half
if n[mid] < n[hi], then look in left half

7 0 1x
l m h -

7 0
l
m

class Solution(object):
	def findMin(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		if not nums: return nums
		lo = 0
		hi = len(nums)-1
		while lo < hi:
			if nums[lo] < nums[hi]:
				return nums[lo]
			mid = (lo+hi)/2
			if nums[lo] <= nums[mid]:
				lo = mid + 1
			else: # nums[lo] > nums[mid]
				hi = mid
		return nums[lo]



class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = len(nums)-1
        while start < end:
            if nums[start] < nums[end]:
                return nums[start]
            mid = (start+end)/2
            if nums[start] <= nums[mid]:
                start = mid+1
            else:
                end = mid
        return nums[start]