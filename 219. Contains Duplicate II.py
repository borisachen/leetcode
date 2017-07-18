219. Contains Duplicate II
Given an array of integers and an integer k, find out whether there are two distinct 
indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

1. maintain sliding window of size k
use a set to keep track of all items in the window
when we move the window up, remove the tail value from the set
when we add value and its already there, then return True

class Solution(object):
	def containsNearbyDuplicate(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: bool
		"""
		myset = set()
		for i in range(len(nums)):
			if i > k:
				myset.remove(nums[i-k-1])
			if not myset.add(nums[i]):
				return True
		return False