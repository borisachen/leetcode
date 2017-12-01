416. Partition Equal Subset Sum

Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:
Each of the array element will not exceed 100.
The array size will not exceed 200.
Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.

"""
Rephrase the problem to:
select a subset of elements s.t. the sum of the subset is equal to half the total sum.
dp[i][j] = whether or not the first i elements can make the specific sum j

Base case:
dp[0][0] = True
transition function:
For each number, if we don't pick it, then
	dp[i][j] = dp[i-1][j] b/c we can ignore element i
If we pick nums[i],
	dp[i][j] = dp[i-1][j-nums[i]]
Therefore the transition function is:
	dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]

"""


class Solution(object):
	def canPartition(self, nums):
		"""
		:type nums: List[int]
		:rtype: bool
		"""
		s = 0
		for num in nums:
			s += num
		if s % 2 == 1:
			return False
		s /= 2
		n = len(nums)
		dp = [[False for x in range(s+1)] for x in range(n+1)]
		# can always make 0 from the first 0 elements
		dp[0][0] = True 
		# can always make 0 from the first i elements, for all i
		for i in range(n+1):
			dp[i][0] = True
		# can never make j (for j > 0) from the first i elements
		for j in range(s+1):
			dp[0][j] = False
		# iterate and update transition function
		for i in range(n+1):
			for j in range(s+1):
				if j >= nums[i-1]:
					dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
				else:
					dp[i][j] = dp[i-1][j]
		return dp[n][s]


Solution().canPartition([1, 5, 11, 5])
Solution().canPartition([1, 2, 3, 5])



class Solution(object):
	def canPartition(self, nums):
		"""
		:type nums: List[int]
		:rtype: bool
		"""
		s = 0
		for n in nums:
			s += n
		if s % 2 == 1:
			return False
		s /= 2
		m = len(nums)
		dp = [[False for x in range(s+1)] for x in range(m+1)]
		dp[0][0] = True
		for i in range(1, m+1):
			dp[i][0] = True
		for j in range(1, s+1):
			dp[0][j] = False
		for i in range(m+1):
			for j in range(s+1):
				dp[i][j] = dp[i-1][j]
				if j >= nums[i-1]:
					dp[i][j] = dp[i][j] or dp[i-1][j-nums[i-1]]
		return dp[m][s]

Solution().canPartition([1, 5, 11, 5])
Solution().canPartition([1, 2, 3, 5])
