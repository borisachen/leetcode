317. Shortest Distance from All Buildings

You want to build a house on an empty land which reaches all buildings in the shortest amount of distance.
You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:

Each 0 marks an empty land which you can pass by freely.
Each 1 marks a building which you cannot pass through.
Each 2 marks an obstacle which you cannot pass through.
For example, given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2):

1 - 0 - 2 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0
The point (1,2) is an ideal empty land to build a house, as the total travel distance of 3+3+1=7 is minimal. So return 7.

Note:
There will be at least one building. If it is not possible to build such house according to the above rules, return -1.

---------------------------
Approach 1: Brute Force
Try every (i,j) slot. Compute the distance from each building to each possible slot.

We can improve this by precomputing the distance from each building to every other slot.
BFS to find cost grid for each building.
Add them all up, find the minimum and return it.
We need a second grid to track how many from each is reachable.

Complexity:
Time: double for loop, BFS across the entire grid -> O(n^2)
---------------------------

def shortest(grid):
	if not grid: return 0
	m = len(grid) # num rows
	n = len(grid[0]) # num cols
	numReach = [[0]*n for _ in range(m)]
	distance = [[0]*n for _ in range(m)]
	numBuilding = 0
	for i in range(m):
		for j in range(n):
			if grid[i][j] == 1:
				visited = [[0]*n for _ in range(m)]
				queue = []
				dfs(grid, i, j, i, j, 0, visited, queue)
				numBuilding += 1
	result = sys.maxint
	for i in range(m):
		for j in range(n):
			if grid[i][j] == 0 and numReach[i][j] == numBuilding:
				result = min(result, distance[i][j])
	return -1 if result == sys.maxint else 0

def dfs(grid, ox, oy, i, j, distanceSoFar, queue):
	visit(grid, i, j, i, j, distanceSoFar, visited, queue)
	n = len(grid[0])
	while queue:
		size = len(queue):
		distanceSoFar += 1
		for k in range(size):
			top = queue.pop()
			i = top/n
			j = top % n
			visit(grid, ox, oy, i-1, j, distanceSoFar, visited, queue)
			visit(grid, ox, oy, i+1, j, distanceSoFar, visited, queue)
			visit(grid, ox, oy, i, j-1, distanceSoFar, visited, queue)
			visit(grid, ox, oy, i, j-1, distanceSoFar, visited, queue)

def visit(grid, ox, oy, i, j, distanceSoFar, queue):
	m = len(grid)
	n = len(grid[0])
	if i<0 or j<0 or i>=m or j >= n: return
	if ((i!=ox or j!=oy) and grid[i][j]!=0): return # if building/impassible and its not the original
	visited[i][j] = True
	numReach[i][j] += 1
	distance[i][j] += distanceSoFar
	queue.append(i*n+j)
