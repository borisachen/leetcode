131. Palindrome Partitioning

Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

[
  ["aa","b"],
  ["a","a","b"]
]

1. backtracking?
'aab'
check if each of the following is a palindrome:
[0,0] 'a'
[0,1] 'aa'
[0,2] 'aab'
in each case we will make a recursive call w/the rest of the string

complexity:
n items; n-1 intervals between items; 2^(n-1) ways to cut/not cut the string
for each permunation, we need to check palindrome, which is O(n)
so total is O(n * 2^n)

2. If we can precompute the palindrome information, reducing that part to O(1). total of O(n^2) + cost.

How do we precompute? DP approach.
dp[i][j] = true if the substring s[i:j] is a palindrome
init: dp[i][i] = true for all i
dp[i][j] = true if 
	(1) s[i]=s[j] and 
	(1) dp[i+1][j-1] is true or i-j <= 2 (3 or less total characters)



# Second faster take

class Solution(object):
	def partition(self, s):
		"""
		:type s: str
		:rtype: List[List[str]]
		"""
		res = []
		dp = self.precompute(s)
		print dp
		self.backtrack(s, 0, 0, [], res, dp)
		return res
	def backtrack(self, s, start, n, temp, res, dp):
		if n == len(s):
			res.append(list(temp))
			return
		for i in range(start+1, len(s)+1):
			newword = s[start:i]
			if self.ispali(start, i-1, dp):
				self.backtrack(s, i, n+len(newword), temp + [newword], res, dp)
	def ispali(self, start, end, dp):
		return dp[start][end]
	def precompute(self,s):
		n = len(s)
		dp = [[False]*n for i in range(0,n)]
		for x in range(n):
			dp[x][x] = True
		for i in range(n):
			for j in range(i+1):
				if i>0 and j<n-1 and s[i] == s[j] and (dp[j+1][i-1] or i-j <= 2):
					dp[i][j] = True
		return dp

Solution().partition("aab")






# First, slow solution

class Solution(object):
	def partition(self, s):
		"""
		:type s: str
		:rtype: List[List[str]]
		"""
		res = []
		self.backtrack(s, 0, 0, [], res)
		return res
	def backtrack(self, s, start, n, temp, res):
		if n == len(s):
			print temp
			res.append(list(temp))
			return
		for i in range(start+1, len(s)+1):
			newword = s[start:i]
			if self.ispali(newword):
				self.backtrack(s, i, n+len(newword), temp + [newword], res)
	def ispali(self, word):
		for i in range(len(word)/2):
			if word[i] != word[len(word)-i-1]:
				return False
		return True


Solution().partition("aab")
