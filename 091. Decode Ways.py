91. Decode Ways

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.

I used a dp array of size n + 1 to save subproblem solutions. 
dp[0] means an empty string will have one way to decode, 
dp[1] means the way to decode a string of size 1. 
I then check one digit and two digit combination and save the results along the way. 
In the end, dp[n] will be the end result.
dp[0] = 1
dp[1] = 1
dp[i] depends on last 2 spots:
	if last 2 chars are b/t 10 and 26,
		then increment by dp[i-2]
	if last 1 char is b/t 1-9,
		then add dp[i-1]

 "1 1 1 2 9"
1 1 2 3
 "5 5 5"
1 1 1 1




class Solution(object):
	def numDecodings(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		if len(s)==0: return 0
		if len(s)==1: return 1 if s[0]!='0' else 0
		dp = [0]*(len(s)+1)
		dp[0] = 1
		dp[1] = 0 if s[0]=='0' else 1
		for i in range(2, len(s)+1):
			if s[i-1:i] >= '1' and s[i-1:i] <='9':
				dp[i] += dp[i-1]
			if s[i-2:i] >= '10' and s[i-2:i] <= '26':
				dp[i] += dp[i-2]
		return dp[len(s)]

