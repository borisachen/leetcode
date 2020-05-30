1013. Partition Array Into Three Parts With Equal Sum
Easy/350/55

Given an array A of integers, return true if and only if we can partition the array into three non-empty parts with equal sums.

Formally, we can partition the array if we can find indexes i+1 < j with
(A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1])



Example 1:

Input: A = [0,2,1,-6,6,-7,9,1,2,0,1]
Output: true
Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
Example 2:

Input: A = [0,2,1,-6,6,7,9,-1,2,0,1]
Output: false
Example 3:

Input: A = [3,3,6,5,-2,2,5,1,-9,4]
Output: true
Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4


Constraints:

3 <= A.length <= 50000
-10^4 <= A[i] <= 10^4


"""
1. precompute the sum, and 1/3 of the sum. call this target.
if we iterate through the array, we should be able to hit target.
reset, then do it again, 3 times total.

computing sum is n, iterating is n. so time is O(n)
space is o(1)

2. use 2 pointers starting from each end.
increment i and j by one each time.
if we can find target on the left and on the right before i and j meet,
that means the middle must be target too
"""

class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        s = sum(A)
        target = s / 3
        remain = s % 3
        temp = 0
        count = 0
        for i in range(len(A)):
            temp += A[i]
            if temp == target:
                count += 1
                temp = 0
        return count >= 3 and remain == 0


class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        s = sum(A)
        remainder = s % 3
        target = s / 3
        i, j = 1, len(A)-2
        l, r = A[0], A[-1]
        left_done = False
        right_done = False
        while i <= j:
            if i < j and l != target:
                l += A[i]
                i += 1
            if i < j and r != target:
                r += A[j]
                j -= 1
            if l == r == target and remainder == 0:
                return True
            if i == j:
                break
        return False
