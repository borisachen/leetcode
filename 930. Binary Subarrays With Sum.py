930. Binary Subarrays With Sum
Medium/144/9

In an array A of 0s and 1s, how many non-empty subarrays have sum S?

Example 1:

Input: A = [1,0,1,0,1], S = 2
Output: 4
Explanation:
The 4 subarrays are bolded below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]

Note:

A.length <= 30000
0 <= S <= A.length
A[i] is either 0 or 1.
-----
Approach 1: Naively check all O(n^2) subarrays.

Approach 2:
Note that if we precompute a vector presum where
presum[i] = A[0] + ... + A[i],
then we can note that we want to find how many i, j satisfy
presum[j] - presum[i-1] = target, or
presum[j] - target = presum[i-1]

-----
class Solution(object):
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        presum = {}
        cursum = 0
        res = 0
        for i in range(len(A)):
            cursum += A[i]
            if cursum - S in presum:
                res += presum[cursum - S]
            if cursum - S == 0:
                res += 1
            if cursum in presum:
                presum[cursum] += 1
            else:
                presum[cursum] = 1
        return res
