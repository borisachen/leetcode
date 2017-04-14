81. Search in Rotated Sorted Array II

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Write a function to determine if a given target is in the array.

The array may contain duplicates.

1) everytime check if target == nums[mid], if so, we find it.
2) otherwise, we check if the first half is in order (i.e. nums[left]<=nums[mid]) 
  and if so, go to step 3), otherwise, the second half is in order,   go to step 4)
3) check if target in the range of [left, mid-1] (i.e. nums[left]<=target < nums[mid]), 
if so, do search in the first half, i.e. right = mid-1; otherwise, search in the second half left = mid+1;
4)  check if target in the range of [mid+1, right] (i.e. nums[mid]<target <= nums[right]), 
if so, do search in the second half, i.e. left = mid+1; otherwise search in the first half right = mid-1;

class Solution(object):
	def search(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: bool
		"""
		if len(nums)==0: return False
		lo, hi = 0, len(nums)-1
		while lo <= hi:
			mid = (lo+hi)/2
			# everytime check if mid is the target
			if nums[mid]==target:
				return True
			# if the first half is in order
			if nums[lo] <= nums[mid]:
				# and if target is in the first half
				if nums[lo] <= target and target < nums[mid]:
					# then search the first half
					hi = mid-1
				# otherwise search the right half
				else:
					lo = mid+1
			# otherwise, the second half is in order
			else:
				# if target is in the second half
				if nums[mid] < target and target <= nums[hi]:
					# search the second half
					lo = mid + 1
				else:
					# otherwise search the left half
					hi = mid-1
		return False