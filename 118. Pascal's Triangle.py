118. Pascal's Triangle
Easy 552/66

Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        prev = [1]
        cur = []
        res = [prev]
        for i in range(1, numRows):
            cur.append(1)
            for j in range(len(prev)-1):
                cur.append(prev[j] + prev[j+1])
            cur.append(1)
            prev = cur
            res.append(prev)
            cur = []
        return res
