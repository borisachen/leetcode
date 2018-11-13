351. Android Unlock Patterns

Given an Android 3x3 key lock screen and two integers m and n, where 1 ≤ m ≤ n ≤ 9, count the total number of unlock patterns of the Android lock screen, which consist of minimum of m keys and maximum n keys.

Rules for a valid pattern:
Each pattern must connect at least m keys and at most n keys.
All the keys must be distinct.
If the line connecting two consecutive keys in the pattern passes through any other keys, the other keys must have previously selected in the pattern. No jumps through non selected key is allowed.
The order of keys used matters.

Explanation:
| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |
Invalid move: 4 - 1 - 3 - 6 
Line 1 - 3 passes through key 2 which had not been selected in the pattern.

Invalid move: 4 - 1 - 9 - 2
Line 1 - 9 passes through key 5 which had not been selected in the pattern.

Valid move: 2 - 4 - 1 - 3 - 6
Line 1 - 3 is valid because it passes through key 2, which had been selected in the pattern

Valid move: 6 - 5 - 4 - 1 - 9 - 2
Line 1 - 9 is valid because it passes through key 5, which had been selected in the pattern.

Example:
Given m = 1, n = 1, return 9.

------------------------------
We will take a backtracking/dfs search approach.
In the dfs function, we want to mark the current node visited,
then loop through all the other possibilities.
We determine if a next node is a valid transition by checking:
1. it hasnt been visited
2. it has no skip requirement, or weve visited the skip requirement
We will need a skip matrix to mark the ones that require a skip.
the unmark current node as visited before moving on.
return the sum of all the 1 counts.
------------------------------

def numberOfPatterns(m, n):
	skip = [[0]*n for i in range(m)]
	skip[1][3] = skip[3][1] = 2;
	skip[1][7] = skip[7][1] = 4;
	skip[3][9] = skip[9][3] = 6;
	skip[7][9] = skip[9][7] = 8;
	skip[1][9] = skip[9][1] = skip[2][8] = skip[8][2] = skip[3][7] = skip[7][3] = skip[4][6] = skip[6][4] = 5;
	visited = [0]*10
	res = 0
	for i in range(m, n):
		res += dfs(visited, skip, 1, i-1) * 4
		res += dfs(visited, skip, 2, i-1) * 4
		res += dfs(visited, skip, 5, i-1) 
	return res

def dfs(visited, skip, cur, remain):
	if remain < 0: return 0
	if remain == 0: return 1
	visited[cur] = True
	res = 0
	for i in range(1, 10):
		if not visited[i] and ((skip[cur][i]==0) or (visited[skip[cur[i]]])):
			res += DFS(visited, skip, i, remain - 1)
	visited[cur] = False
	return res
