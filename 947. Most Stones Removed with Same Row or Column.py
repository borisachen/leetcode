947. Most Stones Removed with Same Row or Column
Medium/243/66

On a 2D plane, we place stones at some integer coordinate points.  Each coordinate point may have at most one stone.

Now, a move consists of removing a stone that shares a column or row with another stone on the grid.

What is the largest possible number of moves we can make?

Example 1:

Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output: 5
Example 2:

Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
Output: 3
Example 3:

Input: stones = [[0,0]]
Output: 0

Note:

1 <= stones.length <= 1000
0 <= stones[i][j] < 10000

'''
Like count number of islands, but an island/neighbor is defined by
any point that shares a col/row with another point.

since we dont want to recreate "grid", we can iterate over the points.
keep an inverse of a visited set, aka, "still need to visit points" and
remove from them as we dfs.
'''

class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        import collections
        points = {(i,j) for i,j in stones}
        islands = 0
        rows = collections.defaultdict(list)
        cols = collections.defaultdict(list)
        for i,j in stones:
            rows[i].append(j)
            cols[j].append(i)
        def dfs(i,j, points):
            points.discard((i,j))
            for y in rows[i]:
                if (i,y) in points:
                    dfs(i,y,points)
            for x in cols[j]:
                if (x,j) in points:
                    dfs(x,j,points)
            return
        for i,j in stones:
            if (i,j) in points:
                dfs(i,j,points)
                islands += 1
        return len(stones) - islands
