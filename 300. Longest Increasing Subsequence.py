300. Longest Increasing Subsequence 

Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?

1. DP approach
d[0] = 1
for each i = 0, ..., n
	iterate j = 0, ..., i
		if nums[j] < nums[i], then j contributes to i. 
		dp[i] = max(dp[j]+1, dp[i])

time complexity: O(n^2)
space: O(n)

class Solution(object):
	def lengthOfLIS(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		n = len(nums)
		if n <= 1: return n
		T = [1]*n
		for i in range(n):
			for j in range(i):
				if nums[j] < nums[i]:
					T[i] = max(T[i], T[j] + 1)
		return max(T)

2. O(nlogn)?

class Solution(object):
	def lengthOfLIS(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		tails = [0]*len(nums)
		size = 0
		for x in nums:
			i = 0
			j = size
			while i != j:
				m = (i+j)/2
				if tails[m] < x:
					i = m+1
				else:
					j = m
			tails[i] = x
			size = max(i+1, size)
		return size



