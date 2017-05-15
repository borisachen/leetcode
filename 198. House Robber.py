198. House Robber

You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed, 
the only constraint stopping you from robbing each of them is that adjacent houses have security system connected 
and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, 
determine the maximum amount of money you can rob tonight without alerting the police.

dp[0] = nums[0]
dp[1] = max(nums[0], nums[1])
dp[i] = max(dp[i-2]+nums[i], dp[i-1])

0 10 2 3 40 5

a b  a

class Solution(object):
	def rob(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		dp = [0]*len(nums)
		dp[0] = nums[0]
		dp[1] = max(nums[0], nums[1])
		for i in range():
			dp[i] = max(dp[i-2]+nums[i], dp[i-1])


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