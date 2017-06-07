540. Single Element in a Sorted Array

Given a sorted array consisting of only integers where every element appears twice 
except for one element which appears once. Find this single element that appears only once.

Example 1:
		0 1 2 3 4 5 6 7 8 
Input: [1,1,2,3,3,4,4,8,8]
                m
		0 1 2 3 4 5 6 7 8 
       [1,1,3,3,4,4,7,8,8]
Output: 2
Example 2:
Input: [3,3,7,7,10,11,11]
Output: 10
Note: Your solution should run in O(log n) time and O(1) space.

mid = len/2

class Solution(object):
	def singleNonDuplicate(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		lo = 0
		hi = len(nums)/2
		while lo < hi:
			mid = (lo+hi)/2
			if nums[lo*2] == nums[lo*2+1]:
				lo = hi+1
			else:
				hi = mid
		return nums[lo*2]

Solution().singleNonDuplicate([1,1,2,3,3,4,4,8,8])
Solution().singleNonDuplicate([3,3,7,7,10,11,11])

