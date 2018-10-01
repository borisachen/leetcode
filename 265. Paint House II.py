265. Paint House II

There are a row of n houses, each house can be painted with one of the k colors. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x k cost matrix. For example, costs[0][0] is the cost of painting house 0 with color 0; costs[1][2] is the cost of painting house 1 with color 2, and so on... Find the minimum cost to paint all houses.

Note:
All costs are positive integers.

Follow up:
Could you solve it in O(nk) runtime?

------------------------------------------
Standard 2D dynamic programming
dp[i][j] = best up to house i given its color is j
dp[i][j] = min(dp[i-1][k] ... for all k!=j) + cost(i,j)

Time: O(k*k*n)
Space: O(k*n)

We can reduce the space complexity to O(k) since we only need the previous column.
------------------------------------------



def paint_house_2(cost):
	n = len(cost[0])
	k = len(cost)
	dp = [[0]*n for i in range(k)]
	# intialize fist column
	for i in range(k):
		dp[i][0] = cost[i][0]
	# now iterate
	for j in range(1, n):
		for i in range(k):
			cand = []
			for l in range(k):
				if l != i: cand.append(dp[l][j-1])
			dp[i][j] = min(cand) + cost[i][j]
	return min([x[-1] for x in dp])

paint_house_2(cost = [[3,3,3,3],[2,2,2,2],[1,1,1,1]])


def paint_house_2b(cost):

n = len(cost[0])
k = len(cost)
prev = [0]*k
for i in range(k):
	prev[i] = cost[i][0]
for j in range(1, n):
	for i in range(k):
		
