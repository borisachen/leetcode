5. Longest Palindromic Substring
DescriptionHintsSubmissionsSolutions
Discuss   Editorial Solution Pick One
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.
Example:

Input: "cbbd"

Output: "bb"
 0123
 babad
 l h
l   h


class Solution(object):
	def longestPalindrome(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		start = 0
		maxlen = 0
		n = len(s)
		for i in range(n):
			self.extend(s, i, i, start, maxlen)
			self.extend(s, i-1, i, start, maxlen)
		return s[start:start+maxlen]
	def extend(self, s, lo, hi, start, maxlen):
		while lo >= 0 and hi < len(s) and s[lo] == s[hi]:
			lo -= 1
			hi += 1
		if hi - lo - 1 > maxlen:
			start = lo + 1
			maxlen = hi - lo - 1
		return


Solution().longestPalindrome("cbbd")
Solution().longestPalindrome("babad")
