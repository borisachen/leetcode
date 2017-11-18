647. Palindromic Substrings

Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
Note:
The input string length wont exceed 1000.


class Solution(object):
	def countSubstrings(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		self.count = 0
		if not s: return 0
		for i in range(0,len(s)):
			self.extendPalindrome(s, i, i)
			self.extendPalindrome(s, i, i+1)
		return self.count

	def extendPalindrome(self, s, l, r):
		while l >= 0 and r < len(s) and s[l] == s[r]:
			self.count += 1
			l -= 1
			r += 1
