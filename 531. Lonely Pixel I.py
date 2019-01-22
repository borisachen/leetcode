531. Lonely Pixel I
Medium ?/?
https://leetfree.com/problems/lonely-pixel-i.html

Given a picture consisting of black and white pixels, find the number of black lonely pixels.

The picture is represented by a 2D char array consisting of 'B' and 'W', which means black and white pixels respectively.

A black lonely pixel is character 'B' that located at a specific position where the same row and same column don't have any other black pixels.

Example:
Input:
[['W', 'W', 'B'],
 ['W', 'B', 'W'],
 ['B', 'W', 'W']]

Output: 3
Explanation: All the three 'B's are black lonely pixels.
Note:
The range of width and height of the input 2D array is [1,500].

-----
Scan once, count the number of B's in each row and columns
On the second scan, check if grid[i][j] == B and row[i] == 1 and col[j] == 1.
-----

def lonelypixeli(grid):
    if not grid: return 0
    res = 0
    n = len(grid)
    m = len(grid[0])
    rowcnt = [0] * n
    colcnt = [0] * m
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'B':
                rowcnt[i] += 1
                colcnt[j] += 1
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'B' and rowcnt[i] == 1 and colcnt[j]==1:
                res += 1
    return res


grid =[['W', 'W', 'B'],
 ['W', 'B', 'W'],
 ['B', 'W', 'W']]

lonelypixeli(grid)
