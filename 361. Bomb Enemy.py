361. Bomb Enemy

Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero), return the maximum enemies you can kill using one bomb.
The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since the wall is too strong to be destroyed.
Note that you can only put the bomb at an empty cell.

Example:
For the given grid

0 E 0 0
E 0 W E
0 E 0 0

return 3. (Placing a bomb at (1,1) kills 3 enemies)

---
Approach 1:
Store two matrix, one for enemy count in the current row (within walls)
one for enemy count in the current columns.
Sum the two and take the max.
iterate each row twice, O(n*m)
iterate each column twice O(n*m)
Then a third pass to get the max. O(n*m)

Approach 1a:
Rather than doubling back, we can have to row matricies.
count once from the left, reset if we hit a wall
count once from the right, reset if we hit a wall
E E 0 E E 
1 2 2 3 4
4 3 2 2 1
---------
5 5 4 5 5
This works because for the 0s, we have the number of Es to the left and right.
IT doesnt matter that we doulbe count on the Es since we cant plant a bomb there.
This means we track 4 matricies, and sum them all together.

Approach 2:
https://medium.com/@rebeccahezhang/361-bomb-enemy-1b4b36d5a47a
---

def bomb_enemy(grid):
	n = len(grid)
	m = len(grid[0])
	rows = [[0]*m for _ in range(n)]
	cols = [[0]*m for _ in range(n)]
	for r in range(n):	
		i, j, temp_enemy_count = 0, 0, 0
		while j < n:
			if grid[r][j] == 'W':
				for k in range(i,j):
					rows[r][k] = temp_enemy_count
				temp_enemy_count = 0
				i = j + 1
			if grid[r][j] == 'E'
				temp_enemy_count += 1
			j += 1
	for c in range(m):
		# repeat for columns
	mymax = 0
	for r in range(n):
		for c in range(m):
			if rows[r][c] + cols[r][c] > mymax:
				mymax = rows[r][c] + cols[r][c]
	return mymax


def bomb_enemy(grid):
	m = len(grid)
	n = len(grid[0])
	mymax = 0
	rowcount = 0
	colcount = [0] * n
	for i in range(m):
		for j in range(n):
			if j==0 or grid[i][j-1]=='W':
				for k in range(j, n):
					if grid[i][k] == 'W': break
					if grid[i][k] == 'E': rowcount += 1
			if i==0 or grid[i-1][j]=='W':
				for k in range(i, m):
					if grid[k][j] == 'W': break
					if grid[k][j] == 'E': colcount[j] += 1
			if grid[i][j]=='0':
				mymax = max(mymax, rowcount+colcount[j])
	return mymax
