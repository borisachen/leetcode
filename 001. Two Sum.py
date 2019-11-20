1. Two Sum
Easy
12507/434

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
"""
Naive:
Search all possible pairs, O(n^2)

If we sort first, then for each x we can stop searching the second point when the sum exceeds target.
However in the worst case, this is still O(n^2)

Hash map:
As we iterate x through the list, Store target - x. Check membership for each x.
O(n) time, o(n) space.
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i,x in enumerate(nums):
            if x in d:
                return [d[x], i]
            else:
                d[target - x] = i
