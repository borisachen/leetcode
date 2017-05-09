139. Word Break

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, 
determine if s can be segmented into a space-separated sequence of one or more dictionary words. 
You may assume the dictionary does not contain duplicate words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".

UPDATE (2017/1/4):
The wordDict parameter had been changed to a list of strings (instead of a set of strings). 
Please reload the code definition to get the latest changes.

1. DP. init dp[i] = False for all i
dp[i] = True if any word in the dict ends here (word has length j), and dp[i-j]==True
time: O(n*m)
space: O(n)

c o w; j=3
0 1 2

class Solution(object):
	def wordBreak(self, s, wordDict):
		"""
		:type s: str
		:type wordDict: List[str]
		:rtype: bool
		"""
		dp = [False]*len(s)
		for i in xrange(len(s)):
			for word in wordDict:
				j = len(word)
				if s[i-j+1:i+1] == word and (i-j < 0 or dp[i-j] == True):
					dp[i] = True
		return dp[-1]


Solution().wordBreak("leetcode", ["leet","code"])











old solutions:
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        0 1 2 3 4 
        j x x i x x x x x x 
        f = [False]*len(s)
        f[0] = True
        for i in range(1, len(s)):
            for j in range(0, i):
                if ((f[j]==True) & (s[j:i] in wordDict)):
                    f[i] = True
                    break
        return f[-1]
        """
        # init array to false
     	d = [False] * len(s) 
     	# for each letter in s
     	for i in range(len(s)):
     	    # for each word in dict
     		for w in wordDict:
     		    # if word is a match and the ith spot back is true or we are at the beginning
     			if w == s[i-len(w)+1:i+1] and (d[i-len(w)] or i-len(w) == -1):
     				d[i] = True
     	return d[-1]