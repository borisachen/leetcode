220. Contains Duplicate III 

<<<<<<< HEAD
Given an array of integers, find out whether there are two distinct indices i and j in the array 
such that the absolute difference between nums[i] and nums[j] is at most t 
and the absolute difference between i and j is at most k.
=======
Given an array of integers, find out whether there are two distinct indices 
i and j in the array such that 
the absolute difference between nums[i] and nums[j] is at most t and 
the absolute difference between i and j is at most k.
>>>>>>> 099b20a305ed9701c9f56592c90323dbc5cb4ae2

class Solution(object):
	def containsNearbyAlmostDuplicate(self, nums, k, t):
		"""
		:type nums: List[int]
		:type k: int
		:type t: int
		:rtype: bool
		"""
<<<<<<< HEAD
=======
		if t < 0: return False
		n = len(nums)
		d = {}
		w = t+1
		for i in range(n):
			m = nums[i] / w
			if m in d:
				return True
			if m - 1 in d and abs(nums[i] - d[m-1]) < w:
				return True
			if m + 1 in d and abs(nums[i] - d[m+1]) < w:
				return True
			d[m] = nums[i]
			if i >= k:
				del d[nums[i-k]/w]
		return False
>>>>>>> 099b20a305ed9701c9f56592c90323dbc5cb4ae2
