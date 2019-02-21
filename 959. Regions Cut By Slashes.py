959. Regions Cut By Slashes
Medium/154/42
In a N x N grid composed of 1 x 1 squares, each 1 x 1 square consists of a /, \, or blank space.  These characters divide the square into contiguous regions.

(Note that backslash characters are escaped, so a \ is represented as "\\".)

Return the number of regions.

Example 1:

Input:
[
  " /",
  "/ "
]
Output: 2
Explanation: The 2x2 grid is as follows:

Example 2:

Input:
[
  " /",
  "  "
]
Output: 1
Explanation: The 2x2 grid is as follows:

Example 3:
Input:
[
  "\\/",
  "/\\"
]
Output: 4
Explanation: (Recall that because \ characters are escaped, "\\/" refers to \/, and "/\\" refers to /\.)
The 2x2 grid is as follows:

Example 4:
Input:
[
  "/\\",
  "\\/"
]
Output: 5
Explanation: (Recall that because \ characters are escaped, "/\\" refers to /\, and "\\/" refers to \/.)
The 2x2 grid is as follows:

Example 5:
Input:
[
  "//",
  "/ "
]
Output: 3
Explanation: The 2x2 grid is as follows:

Note:

1 <= grid.length == grid[0].length <= 30
grid[i][j] is either '/', '\', or ' '.


class Solution(object):
    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        #grid = ["\\/","/\\"]
        n = len(grid)
        N = n*3
        big = [[0]*N for _ in range(N)]
        for i in range(n):
            for j in range(n):
                if grid[i][j] == '\\':
                    big[i*3][j*3] = 1
                    big[i*3+1][j*3+1] = 1
                    big[i*3+2][j*3+2] = 1
                if grid[i][j] == '/':
                    big[i*3][j*3+2] = 1
                    big[i*3+1][j*3+1] = 1
                    big[i*3+2][j*3] = 1

        def sink(big, i, j, N):
            if i <0 or j <0 or i >= N or j>=N or big[i][j]!=0:
                return
            big[i][j] = 2
            sink(big, i-1, j, N)
            sink(big, i+1, j, N)
            sink(big, i, j-1, N)
            sink(big, i, j+1, N)
            return

        res = 0
        for i in range(N):
            for j in range(N):
                if big[i][j] == 0:
                    res += 1
                    sink(big, i, j, N)
        return res
