72. Edit Distance
DescriptionHintsSubmissionsSolutions
Total Accepted: 85749
Total Submissions: 274301
Difficulty: Hard
Contributor: LeetCode
Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character

1. dp
f[i][j] = shortest edit b/t word1[0,i] and word2[0,j]
then compare last character of each word. call them c and d.
if c == d then f[i][j] = f[i-1][j-1]
otherwise:
if we replace c with d: f[i][j] = f[i-1][j-1] + 1
if we added d after c: f[i][j] = f[i][j-1] + 1
if we added c after d: f[i][j] = f[i-1][j] + 1

further, f[i][j] only depends on i-1 and j-1,
so we only need to keep (i-1)th array and the previous element, f[i][j-1] 

class Solution(object):
	def minDistance(self, word1, word2):
		"""
		:type word1: str
		:type word2: str
		:rtype: int
		"""
		if not word1 and not word2: return 0
		if word1 and not word2: return len(word1)
		if not word1 and word2: return len(word2)
		l1 = len(word1) + 1
		l2 = len(word2) + 1
		dp = [[0]*l2 for _ in range(l1)]
		for x in range(1, l1):
		    dp[x][0] = x
		for x in range(1, l2):
		    dp[0][x] = x
		for i in range(1, l1):
			for j in range(1, l2):
				if word1[i-1] == word2[j-1]:
					dp[i][j] = dp[i-1][j-1]
				else:
					dp[i][j] = min(min(dp[i-1][j-1], dp[i-1][j]), dp[i][j-1]) + 1
		print dp
		return dp[l1-1][l2-1]

Solution().minDistance("ab", "bc")



class Solution(object):
	def minDistance(self, word1, word2):
		"""
		:type word1: str
		:type word2: str
		:rtype: int
		"""
		if not word1 and not word2: return 0
		if word1 and not word2: return len(word1)
		if not word1 and word2: return len(word2)
		prev_row = range(0, len(word2)+1)
		for i in range(1, len(word1)+1):
			curr_row = [0]*(len(word2)+1)
			curr_row[0] = i
			for j in range(1, len(word2)+1):
				if word1[i-1] == word2[j-1]:
					curr_row[i] = prev_row[j-1]
				else:
					curr_row[i] = min(min())+1
			prev_row = curr_row
		return prev_row[-1]














