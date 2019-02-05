974. Subarray Sums Divisible by K
Medium/126/7

Given an array A of integers, return the number of (contiguous, non-empty)
subarrays that have a sum divisible by K.

Example 1:

Input: A = [4,5,0,-2,-3,1], K = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by K = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]


Note:

1 <= A.length <= 30000
-10000 <= A[i] <= 10000
2 <= K <= 10000
-----
The naive solution is to check all possible subarrays. There are O(n^2) of them.
Sorting doesn't help here since subarrays require order to be preserved,
which means we are looking for an O(n) algorithm.

Can we preprocess anything?
presum[i] = sum( A[0] + ... + A[i])

Then sum(i,j) = presum[j] - presum[i]
Is there something we can store in a hashmap as we preprocess?
presum = [4, 9, 9,  7,  4, 5]
A =      [4, 5, 0, -2, -3, 1]
remainder(1, 1, 1, 3, 2, 0)
-----
class Solution(object):
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        res = 0
        prefix = 0
        count = [1] + [0] * K
        for a in A:
            prefix = (prefix + a) % K
            res += count[prefix]
            count[prefix] += 1
        return res
