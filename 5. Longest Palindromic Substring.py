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

1. iterate, for each i, consider [i-j,i+j].
o(n^2)


class Solution(object):
	def longestPalindrome(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		n = len(s)
		for i in range()