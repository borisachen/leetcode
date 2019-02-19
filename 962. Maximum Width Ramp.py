962. Maximum Width Ramp
Medium

170

7

Favorite

Share
Given an array A of integers, a ramp is a tuple (i, j) for which i < j and A[i] <= A[j].  The width of such a ramp is j - i.

Find the maximum width of a ramp in A.  If one doesn't exist, return 0.



Example 1:

Input: [6,0,8,2,1,5]
Output: 4
Explanation:
The maximum width ramp is achieved at (i, j) = (1, 5): A[1] = 0 and A[5] = 5.
Example 2:

Input: [9,8,1,0,1,9,4,0,4,1]
Output: 7
Explanation:
The maximum width ramp is achieved at (i, j) = (2, 9): A[2] = 1 and A[9] = 1.


Note:

2 <= A.length <= 50000
0 <= A[i] <= 50000

'''
first we build a decreasing stack
this is because if there are two 1's, we don't care about the second one
since it is always going to result in a smaller width
e.g. [9,8,1,0]
then we iterate from the right, j--.
suppose we see a 5. since we want the ramp to be 'increasing',
we can pop off the 0 and the 1, but 8 doesn't work so we stop there.
and move to the next j.
'''

class Solution(object):
    def maxWidthRamp(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        s = []
        res = 0
        for i in range(len(A)):
            if not s or A[s[-1]] > A[i]:
                s.append(i)
        print(s)
        for j in range(len(A))[::-1]:
            while s and A[j] >= A[s[-1]]:
                temp = s.pop()
                res = max(res, j - temp)
        return res
