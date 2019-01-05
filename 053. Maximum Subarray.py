53. Maximum Subarray
Easy
3306/119

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
-----
Approach 1: dynamic programming
dp[i] = largest sub array ending at posiition i
dp[i] = max(dp[i-1], 0) + nums[i]
track and return max so far

-----

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        maxsofar = nums[0]
        dp = -float("inf")
        for i in range(len(nums)):
            dp = max(dp, 0) + nums[i]
            maxsofar = max(maxsofar, dp)
        return maxsofar
