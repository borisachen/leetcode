992. Subarrays with K Different Integers
Hard/193/2

Given an array A of positive integers, call a (contiguous, not necessarily
distinct) subarray of A good if the number of different integers in that
subarray is exactly K.

(For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.)

Return the number of good subarrays of A.

Example 1:

Input: A = [1,2,1,2,3], K = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers:
[1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].

Example 2:
Input: A = [1,2,1,3,4], K = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers:
[1,2,1,3], [2,1,3], [1,3,4].

Note:

1 <= A.length <= 20000
1 <= A[i] <= A.length
1 <= K <= A.length

'''
We can use a sliding window to solve subarrays with at most K.
then we can reduce the problem of exactly K to f(k) - f(k-1)
'''

class Solution(object):
    def subarraysWithKDistinct(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        return self.atmostk(A,K) - self.atmostk(A,K-1)

    def atmostk(self, a, k):
        if k==0: return 0
        res = 0
        i=m=0
        d = {}
        for j in range(len(a)):
            if a[j] in d:
                d[a[j]] += 1
            else:
                d[a[j]] = 1
                m += 1
            while m > k:
                d[a[i]] -= 1
                if d[a[i]] == 0:
                    m -= 1
                    del d[a[i]]
                i += 1
            res += (j-i+1)
        return res



def atmostk(a, k):
    res = 0
    i=m=0
    d = {}
    for j in range(len(a)):
        if a[j] in d:
            d[a[j]] += 1
        else:
            d[a[j]] = 1
            m += 1
        while m > k:
                i += 1
                d[a[i]] -= 1
                if d[a[i]] == 0:
                    m -= 1
                    del d[a[i]]
        res += (j-i+1)
    return res

atmostk([1,2,1,2,3], 2)
