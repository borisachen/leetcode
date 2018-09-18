161. One Edit Distance

Given two strings S and T, determine if they are both one edit distance apart.

------------------------------------

We could compute the full edit distance and check if it is one.
Can be done with dynamic programming in O(n^2).

Can we modify the full edit distance algo?
The transition function is
dp[i,j] = min( dp[i-1,j], dp[i-1,j-1], dp[i,j-1]) + 1
If we fill out the DP matrix row by row, then we can define an early stopping condition.
If we see a row that does not have a 0 in it at all, then we can return False.
Otherwise we can continue to the end and check if the last spot is 1 and if so, we return True.

------------------------------------

a = 'saturday'
b = 'sunday'

def edit_distance(a,b):
	n = len(a)
	m = len(b)
	dp = [[0] * (m+1) for i in range(n+1)]
	# m+1(7) columns, n+1 (9) rows
	# initialize the rows and columns
	for i in range(n+1):
		dp[i][0] = i
	for j in range(m+1):
		dp[0][j] = j
	# populate main dp matrix
	for i in range(1, n+1): # i over rows
		for j in range(1, m+1):
			if a[i-1] == b[j-1]:
				dp[i][j] = dp[i-1][j-1]
			else:
				dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
	return dp[n][m]==1

edit_distance(a,b)