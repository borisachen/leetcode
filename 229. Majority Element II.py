229. Majority Element II 

DescriptionHintsSubmissionsSolutions
Total Accepted: 52485
Total Submissions: 185815
Difficulty: Medium
Contributor: LeetCode
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times. The algorithm should run in linear time and in O(1) space.

class Solution(object):
	def majorityElement(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[int]
		"""
		if not nums: return []
		count1 = 0
		count2 = 0
		candidate1 = 0
		candidate2 = 1
		for n in nums:
			if n == candidate1: count1 += 1
			elif n == candidate2: count2 += 1
			elif count1 == 0:
				candidate1 = n
				count1 = 1
			elif count2 == 0:
				candidate2 = n
				count2 = 1
			else:
				count1 -= 1
				count2 -= 1

		return [n for n in (candidate1, candidate2) if nums.count(n) > len(nums) // 3]
