967. Numbers With Same Consecutive Differences
Medium/62/14

Return all non-negative integers of length N such that the absolute difference between every two consecutive digits is K.

Note that every number in the answer must not have leading zeros except for the number 0 itself. For example, 01 has one leading zero and is invalid, but 0 is valid.

You may return the answer in any order.

Example 1:
Input: N = 3, K = 7
Output: [181,292,707,818,929]
Explanation: Note that 070 is not a valid number, because it has leading zeroes.

Example 2:
Input: N = 2, K = 1
Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]

Note:

1 <= N <= 9
0 <= K <= 9

'''
edge cases:
N=0 - return empty list
N=1 - include 0
K=0 - don't double count 11, 22, 33, etc. due to +/- K

time: O(10*2*N) = O(N)
space: O(N) for output, but O(1) extra storage. O(N) for recurrsion
'''

class Solution(object):
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        res = set()
        if N == 0: return []
        if N == 1: res.add(0)
        for i in range(1, 10):
            self.backtrack(1, N, res, str(i), K)
        return list(res)
    def backtrack(self, i, N, res, temp, K):
        if i == N:
            res.add(int(temp))
            return
        for j in (int(temp[-1])-K, int(temp[-1])+K):
            if j >= 0 and j <= 9:
                self.backtrack(i+1, N, res, temp+str(j), K)
        return
