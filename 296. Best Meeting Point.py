296. Best Meeting Point
(locked)

A group of two or more people wants to meet and minimize the total travel distance.
You are given a 2D grid of values 0 or 1, where each 1 marks the home of someone in the group.
The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

For example, given three people living at (0,0), (0,4), and (2,2):

1 - 0 - 0 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0
The point (0,2) is an ideal meeting point, as the total travel distance of 2+2+2=6 is minimal. So return 6.

1. naive:
compute N grids of costs, overlay them, iterate to find the lowest one.

2.
observation 1 -- each dimesion is independent, since L1 distance is the independent sum.
observation 2 -- in the 1d case, the median is the minimum point.

this gives us the strategy:
for each dimension, sort, find the median. then compute the distance to that point.
rather than sorting, we can scan over the points in order.


grid = [[1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]]

edge case:
[11011]
  x, 1+2+3=6
   x, 1+2+1+2
    x, 3+2,1

def best_meeting_point(grid):
	n_rows = len(grid)
	n_cols = len(grid[0])
	rows = []
	cols = []
	for row in range(n_rows):
		for col in range(n_cols):
			if grid[row][col] == 1:
				rows.append(row)
	for col in range(n_cols):
		for row in range(n_rows):
			if grid[row][col] == 1:
				cols.append(col)
	# now that we've collected all the rows and cols in order, find the median
	median_row = rows[len(rows)/2]
	median_col = cols[len(cols)/2]
	total_dist = 0
	for r in rows:
		total_dist += abs(r-median_row)
	for c in cols:
		total_dist += abs(c-median_col)
	return total_dist

best_meeting_point([[1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]])

Complexity:
time: r*c
