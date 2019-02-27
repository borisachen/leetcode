718. Maximum Length of Repeated Subarray

Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.

Example 1:
Input:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
Output: 3
Explanation:
The repeated subarray with maximum length is [3, 2, 1].
Note:
1 <= len(A), len(B) <= 1000
0 <= A[i], B[i] < 100
'''
---------------------------------
Naive:
make all subarrays in A
check all in B
O(n^2), O(n^3) to check all n^2

dp[ij[j] = longest common substring ending with a[i] and b[j]

transition function
dp[i][j] = dp[i-1][j-1]+1 if a[i]==b[j] else 0
---------------------------------
'''
class Solution(object):
	def findLength(self, A, B):
		"""
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
		n = len(A)
		m = len(B)
		dp = [[0 for x in range(n+1)] for y in range(m+1)]
		res = 0
		for i in range(1, n+1):
			for j in range(1, m+1):
				dp[i][j] = dp[i-1][j-1]+1 if A[i-1]==B[j-1] else 0
				res = max(res, dp[i][j])
		return res


A = [1,2,3,2,1]
B = [3,2,1,4,7]
Solution().findLength(A, B)
