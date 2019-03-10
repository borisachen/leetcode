368. Largest Divisible Subset
Medium/476/22

Given a set of distinct positive integers,
find the largest subset such that every pair (Si, Sj) of elements
 in this subset satisfies: Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:

nums: [1,2,3]

Result: [1,2] (of course, [1,3] will also be ok)
Example 2:

nums: [1,2,4,8]

Result: [1,2,4,8]

---------------
'''
1. dp
S[i] = largest subset with i as largest element
key (i) is the largest int of the set.
for each new int x, only need to check if x%d==0,
'''
---------------

class Solution(object):
	def largestDivisibleSubset(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[int]
		"""
		S = {-1:set()}
		for x in sorted(nums):
			a = [S[d] for d in S if x % d == 0]
			print a
			S[x] = max(a, key=len) | {x}
		print S
		return list(max(S.values(), key=len))

Solution().largestDivisibleSubset([1,2,4,8])
