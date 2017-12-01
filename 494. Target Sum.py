494. Target Sum

You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. 
Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:
Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
Explanation: 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
Note:
The length of the given array is positive and will not exceed 20.
The sum of elements in the given array will not exceed 1000.
Your output answer is guaranteed to be fitted in a 32-bit integer.

"""
naive:
"""

class Solution(object):
	def findTargetSumWays(self, nums, S):
		"""
		:type nums: List[int]
		:type S: int
		:rtype: int
		brute force: try all n! ways
		"""
		# count the total sum first
		total = 0
		for num in nums:
			total += num
		# if the sum is unatailable or odd, then return 0
		if S > total or total % 2 == 1:
			return 0
		return self.subsetSum(nums, (total+S)/2)
	def subsetSum(self, nums, S):
		dp = [0]*(len(nums)+1)
		dp[0] = 1
		for i in range(len(nums)):
			for j in range(S, nums[i])[::-1]:
				dp[j] += dp[j - nums[i]]
		return dp[S]


Solution().subsetSum([1, 1, 1, 1, 1], 3)
