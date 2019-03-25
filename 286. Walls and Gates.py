286. Walls and Gates
(locked)

You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

For example, given the 2D grid:
INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
After running your function, the 2D grid should be:
  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4

------------------------------------
We could find each 0 (starting point), then round robin through them and
take one breadth first search step at a time.
We label each open slot with the depth.
Since we are doing BFS, the first time we label a point, it is guaranteed to be the smallest number from any starting point.
Alternatively we could BFS search one 0 at a time, but that is less efficient.
During the BFS, we ignore points that are -1 (walls) or ones that have already been filled.
We can use a queue for the gates.

Complexity:
Each space should only be searched once. there are O(n^2) spaces

There is also a backtracking solution.

------------------------------------



def walls_and_gates(grid):
	import sys
	INF = sys.maxint
	queue = []
	nrow = len(grid)
	ncol = len(grid[0])
	# first build up the queue with all the 0's
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j] == 0:
				queue.append((i,j))
	while queue:
		x, y = queue.pop(0)
		next_depth = grid[x][y] + 1
		if y > 0 and grid[x][y-1] == INF:
			grid[x][y-1] = next_depth
			queue.append((x,y-1))
		if x < ncol - 1 and grid[x+1][y] == INF:
			grid[x+1][y] = next_depth
			queue.append((x+1,y))
		if y < nrow - 1 and grid[x][y+1] == INF:
			grid[x][y+1] = next_depth
			queue.append((x,y+1))
		if x > 0 and grid[x-1][y] == INF:
			grid[x-1][y] = next_depth
			queue.append((x-1,y))
	return grid


grid = [[INF,  -1,  0,  INF],
		[INF, INF, INF,  -1],
		[INF,  -1, INF,  -1],
		[0,  -1, INF, INF]]

walls_and_gates(grid)

## Backtracking solution
for i in range(len(grid)):
	for j in range(len(grid[0])):
		if grid[i][j] == 0:
			backtrack(grid, i, j, depth=0)

def backtrack(grid, i, j, depth):
	if i < 0 or i > len(grid) or j < 0 or j > len(grid[0]) or grid[i][j] < depth:
		return
	grid[i][j] = depth
	backtrack(grid, i-1, j, depth + 1)
	backtrack(grid, i+1, j, depth + 1)
	backtrack(grid, i, j-1, depth + 1)
	backtrack(grid, i, j+1, depth + 1)
