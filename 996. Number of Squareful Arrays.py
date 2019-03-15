996. Number of Squareful Arrays
Hard/85/6

Given an array A of non-negative integers, the array is squareful if for every pair of adjacent elements, their sum is a perfect square.

Return the number of permutations of A that are squareful.  Two permutations A1 and A2 differ if and only if there is some index i such that A1[i] != A2[i].

Example 1:
Input: [1,17,8]
Output: 2
Explanation:
[1,8,17] and [17,8,1] are the valid permutations.

Example 2:
Input: [2,2,2]
Output: 1

Note:

1 <= A.length <= 12
0 <= A[i] <= 1e9


class Solution(object):
    def numSquarefulPerms(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        ps = self.genValid(A)
        res = []
        used = set()
        self.backtrack([], used, A, ps, res)
        return len(res)
    def genValid(self, A):
        A = sorted(A)
        big = A[-1] + A[-2]
        ps = set()
        for i in range(int(math.sqrt(big))+1):
            ps.add(i*i)
        return ps
    def backtrack(self, temp, used, A, ps, res):
        if len(temp)==len(A):
            if temp not in res:
                res.append(temp)
            return
        for i in range(len(A)):
            if i not in used and ((temp and temp[-1] + A[i] in ps) or (not temp)):
                used.add(i)
                self.backtrack(temp + [A[i]], used, A, ps, res)
                used.remove(i)


Solution().numSquarefulPerms(A=[2,2,2,2,2,2,2])

A=[2,2,2,2,2,2,2,2]
A=[1,8,17]

c = collections.Counter(A)
cand = {i: {j for j in c if int((i + j)**0.5) ** 2 == i + j} for i in c}
res = 0
def dfs(x, left=len(A) - 1):
    c[x] -= 1
    if left == 0:
            res += 1
    for y in cand[x]:
        if c[y]:
            dfs(y, left - 1)
    c[x] += 1

for x in c: dfs(x)
