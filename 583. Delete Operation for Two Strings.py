583. Delete Operation for Two Strings
Medium/627/17

Given two words word1 and word2, find the minimum number of steps required to
make word1 and word2 the same, where in each step you can delete one character
in either string.

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

Approach 2: dp
dp[i][j] = lenght of longest common sub sequence
dp[i][j] =
	if word1[i] == word2[j]: dp[i-1][j-1] + 1
	else: max(dp[i][j-1], dp[0-1][j])
// dp[i][j] stands for distance of first i chars of word1 and first j chars of word2

To make them identical, just find the longest common subsequence. T
he rest of the characters have to be deleted from the both the strings,
which does not belong to longest common subsequence.

public int minDistance(String word1, String word2) {
    int dp[][] = new int[word1.length()+1][word2.length()+1];
    for(int i = 0; i <= word1.length(); i++) {
        for(int j = 0; j <= word2.length(); j++) {
            if(i == 0 || j == 0) dp[i][j] = 0;
            else dp[i][j] = (word1.charAt(i-1) == word2.charAt(j-1)) ? dp[i-1][j-1] + 1
                    : Math.max(dp[i-1][j], dp[i][j-1]);
        }
    }
    int val =  dp[word1.length()][word2.length()];
    return word1.length() - val + word2.length() - val;
}

'''
class Solution(object):
	def minDistance(self, word1, word2):
		"""
		:type word1: str
		:type word2: str
		:rtype: int
		"""
        m, n = len(w1), len(w2)
        dp = [[0] * (n + 1) for i in range(m + 1)]
        for i in range(m):
            for j in range(n):
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j], dp[i][j] + (w1[i] == w2[j]))
        return m + n - 2 * dp[m][n]
