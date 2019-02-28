494. Target Sum
Medium/1175/62

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
------------------------------------
"""
dp[i][j] = whether the specific sum j can be gotten from the first i numbers

The recursive solution is very slow, because its runtime is exponential

The original problem statement is equivalent to:
Find a subset of nums that need to be positive, and the rest of them negative, such that the sum is equal to target

Let P be the positive subset and N be the negative subset
For example:
Given nums = [1, 2, 3, 4, 5] and target = 3 then one possible solution is +1-2+3-4+5 = 3
Here positive subset is P = [1, 3, 5] and negative subset is N = [2, 4]

Then let's see how this can be converted to a subset sum problem:

                  sum(P) - sum(N) = target
sum(P) + sum(N) + sum(P) - sum(N) = target + sum(P) + sum(N)
                       2 * sum(P) = target + sum(nums)
So the original problem has been converted to a subset sum problem as follows:
Find a subset P of nums such that sum(P) = (target + sum(nums)) / 2

Note that the above formula has proved that target + sum(nums) must be even
We can use that fact to quickly identify inputs that do not have a solution (Thanks to @BrunoDeNadaiSarnaglia for the suggestion)
For detailed explanation on how to solve subset sum problem, you may refer to Partition Equal Subset Sum
"""
------------------------------------

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


class Solution(object):
	def findTargetSumWays(self, nums, S):
		"""
		:type nums: List[int]
		:type S: int
		:rtype: int
		"""
		if not nums:
			return 0
		# dic stores the numbers of ways to get each sum so far.
		dic = {nums[0]:1, -nums[0]:1} if nums[0] != 0 else {nums[0]:2}
		for i in range(1, len(nums)):
			tdic = {}
			for d in dic:
				tdic[d + nums[i]] = tdic.get(d + nums[i], 0) + dic.get(d, 0)
				tdic[d - nums[i]] = tdic.get(d - nums[i], 0) + dic.get(d, 0)
			dic = tdic
		return dic.get(S, 0)
