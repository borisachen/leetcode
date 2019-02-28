560. Subarray Sum Equals K
Medium/1602/40
Given an array of integers and an integer k, you need to find the total number
of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2

"""
brute force: n^2
"""
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        res = 0
        for i in range(n):
        	for j in range(i+1, n):
        		print(nums[i:j+1])
        		if sum(nums[i:j+1]) == k:
        			res += 1
        return res

Solution().subarraySum([1,1,1], 2)

"""
Note that: sum(i,j) = sum(0,j) - sum(0, i-1)
So we go through array,
calculate current sum, sum(0,j), save the number seen in presum
if (current sum - target) is in presum,
	increase result by the the presum[s-k]

presum[i] = # of times we've seen current sum
"""
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        s = 0
        res = 0
        presum = {0:1}
        for j in range(len(nums)):
        	s += nums[j]
        	if (s-k) in presum:
        		res += presum[s-k]
        	if s in presum:
        		presum[s] += 1
        	else:
        		presum[s] = 1
        return res

Solution().subarraySum([1,1,1], 2)
