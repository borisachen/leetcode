583. Delete Operation for Two Strings

Given two words word1 and word2, find the minimum number of steps required to make word1 and word2 the same, where in each step you can delete one character in either string.

Example 1:
Input: "sea", "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
Note:
The length of given words wont exceed 500.
Characters in given words can only be lower-case letters.
'''
- bidirectional BFS?
for each starting word:
	we'll search multiple branches
sea:
drop s - ea
drop e - sa
drop a - se

eat
drop e - at
drop a - 
drop t
they should meet in the middle

depth1, depht2 = 0
current_word = 1 or 2
while:
	create all child nodes of word 1
	check if word1 set and word 2 set overlap
	if yes, return sum of depths
	else:
	increment word 1 depth
	swap words to look at
return depth1+depth2

dp:
dp[i][j] = lenght of longest common sub sequence
dp[i][j] = 
	if word1[i] == word2[j]: dp[i-1][j-1] + 1
	else: max(dp[i][j-1], dp[0-1][j])
'''
class Solution(object):
	def minDistance(self, word1, word2):
		"""
		:type word1: str
		:type word2: str
		:rtype: int
		"""
		depth1, depth2 = 0, 0
		cur = 1
		while word1 or word2:
