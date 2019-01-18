198. House Robber
Easy/1986/65

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
-----
approach 1: dp[i] = max up to house i
dp[0] = nums[0]
dp[1] = max(nums[0], nums[1])
dp[i] = max(dp[i-2]+nums[i], dp[i-1])
Time O(n) for one pass, Space O(n)

Approach 2: space optimized, since we only need dp i-1, i-2


-----
class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        n = len(nums)
        if n == 1: return nums[0]
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(nums[i]+dp[i-2], dp[i-1])
        return dp[-1]

class Solution(object):
	def rob(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		a = b = 0
		for i in range(len(nums)):
			if i%2==0:
				a = max(a+nums[i], b)
			else:
				b = max(b+nums[i], a)
		return max(a,b)


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = b = 0
        for i in range(len(nums)):
        	a, b = max(a+nums[i], b), a
        return a


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last, now = 0, 0
        for i in range(0,len(nums)):
            last, now = now, max(last+nums[i], now)
        return now
