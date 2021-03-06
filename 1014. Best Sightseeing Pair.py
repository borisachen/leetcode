1014. Best Sightseeing Pair
Medium/243/11

Given an array A of positive integers, A[i] represents the value of the i-th
sightseeing spot, and two sightseeing spots i and j have distance j - i between them.

The score of a pair (i < j) of sightseeing spots is (A[i] + A[j] + i - j) :
the sum of the values of the sightseeing spots, minus the distance between them.

Return the maximum score of a pair of sightseeing spots.

Example 1:

Input: [8,1,5,2,6]
Output: 11
Explanation: i = 0, j = 2, A[i] + A[j] + i - j = 8 + 5 + 0 - 2 = 11

'''
1. Naive:
double for loop, store all best so far. O(n^2)

2. DP
we want the maximum value of a[i]+i+a[j]-j for i < j.
so we need to keep the previous best index which can make the max a[i]+i
time o(n)
space o(1)
'''

class Solution(object):
    def maxScoreSightseeingPair(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        ans = A[0]
        prevBestIdx = 0
        for j in range(1, len(A)):
            ans = max(ans, A[prevBestIdx] + prevBestIdx + A[j] - j)
            if A[prevBestIdx] + prevBestIdx < A[j] + j:
                prevBestIdx = j
        return ans
