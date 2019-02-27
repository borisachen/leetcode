945. Minimum Increment to Make Array Unique
Medium/113/5

Given an array of integers A, a move consists of choosing any A[i], and incrementing it by 1.

Return the least number of moves to make every value in A unique.



Example 1:

Input: [1,2,2]
Output: 1
Explanation:  After 1 move, the array could be [1, 2, 3].
Example 2:

Input: [3,2,1,2,1,7]
Output: 6
Explanation:  After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
It can be shown with 5 or less moves that it is impossible for the array to have all unique values.


Note:

0 <= A.length <= 40000
0 <= A[i] < 40000

'''
If we sort then iterate from the left, we can find the minimum that A[i] needs to be
given A[i-1]. A[i] >= A[i-1]+1
Time: O(nlogn) for sorting, then one pass through, but worst case all 1's, just add the difference so O(1).

Can we do O(n)?
start with the minimum value (say 1)
remove one of them, and increase all others by 1
go to next lowest value, (2), and repeat.
n, n-1, n-2... loop n times. For each loop we must scan each elmeent so this is n^2 naively.

Can we store something to make one of these steps O(1)?
Counter of occurances?
{1:2, 2:2, 3:1, 7:1}
start at minimum, 1. take one away, add the rest to 2
look up 2, take one away, add the rest to 3.
if 3 does not exist, move on to 4. etc.
O(n) to build the counter. then O(m) steps where m is the highest value.
Time: O(m)
'''

class Solution(object):
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A = sorted(A)
        res = 0
        for i in range(1, len(A)):
            if A[i-1] >= A[i]:
                amt_to_add = A[i-1] - A[i] + 1
                res += amt_to_add
                A[i] += amt_to_add
        return res

class Solution(object):
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        from collections import Counter
        map = Counter(A)
        lo, hi = min(map), max(map)
