1020. Number of Enclaves
Medium/260/17

"""
Given a 2D array A, each cell is 0 (representing sea) or 1 (representing land)

A move consists of walking from one land square 4-directionally to another land square, or off the boundary of the grid.

Return the number of land squares in the grid for which we cannot walk off the boundary of the grid in any number of moves.

Example 1:
Input: [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
Output: 3
Explanation:
There are three 1s that are enclosed by 0s, and one 1 that isn't enclosed because its on the boundary.

Example 2:
Input: [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
Output: 0
Explanation:
All 1s are either on the boundary or can reach the boundary.

Note:
1 <= A.length <= 500
1 <= A[i].length <= 500
0 <= A[i][j] <= 1
All rows have the same size.
"""

"""
recursive dfs
if we fell off the edge anywhere, then we just sink this island as normally.
if we did not fall off anywhere, we add the total number of land squares to res.

top level function will be a 2x for loop.
dfs will return 0 if we fell off the edge, N if we didnt
"""
class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
        res = 0
        nrow = len(A)
        ncol = len(A[0])
        for r in range(nrow):
            for c in range(ncol):
                if A[r][c] == 1:
                    y = self.dfs(A, r, c, nrow, ncol)
                    if y > 0: res += y
        return res

    def dfs(self, A, r, c, nrow, ncol):
        found_exit = False
        # if we are at an edge and are on land, then we found an exit
        if (r == 0 or r == nrow - 1 or c == 0 or c == ncol - 1) and A[r][c] == 1:
            found_exit = True
        # Sink the current land
        A[r][c] = 0
        # Sink the neighbors
        temp = 1 # count 1 for the land we are currently on.
        steps = [[1,0], [0,1], [-1,0], [0,-1]]
        for dx, dy in steps:
            nr, nc = r + dy, c + dx
            if nr >= 0 and nr < nrow and nc >= 0 and nc < ncol and A[nr][nc] == 1:
                x = self.dfs(A, nr, nc, nrow, ncol)
                # if we stepped off the island, then we contribute nothing for this island.
                if x == -1: found_exit = True
                temp += x
        return -1 if found_exit else temp

"""
Solution 2:
start from the edges, sink the lands that are connected to anything on the edge.
then count the number if land spots remaining
"""
class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
        nrow = len(A)
        ncol = len(A)
        def sink(r, c):
            A[r][c] = 0
            for i, j in [[r-1,c], [r+1,c], [r,c-1], [r,c+1]]:
                if 0 <= i < nrow and 0 <= j < ncol and A[i][j]:
                    sink(i,j)
        for r in range(nrow):
            for c in range(ncol):
                if (r == 0 or r == nrow-1 or c==0 or c==ncol-1) and A[r][c]:
                    sink(r, c)
        return sum([sum(row) for row in A])
