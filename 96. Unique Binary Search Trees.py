96. Unique Binary Search Trees

Given n, how many structurally unique BSTs (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BSTs.
"""
   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""

class Solution(object):
	def numTrees(self, n):
		"""
		:type n: int
		:rtype: int
		"""
