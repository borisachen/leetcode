678. Valid Parenthesis String

Given a string containing only three types of characters: '(', ')' and '*', 
write a function to check whether this string is valid. We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.

Example 1:
Input: "()"
Output: True
Example 2:
Input: "(*)"
Output: True
Example 3:
Input: "(*))"
Output: True

"""
1. everytime we see a star, create 3 branching paths, and check all 3.
((
( 
()
DFS; backtrack

at any point, check the remaining strings.

we can truncate searches where 
1) L + * < R.  everything else is valid 
2) more R and L+* at any point so far (we are unable to close;) track this in a stack

variables to pass:
s = original string
path = path so far, with no stars, they've been replaced
index = current index to evalutate
stack = the current stack so far; we'll pop off matched parenthesis

remaing_left
remaing_right
remaing_star

"""

class Solution(object):
	def checkValidString(self, s):
		"""
		:type s: str
		:rtype: bool
		"""
		return self.backtrack(s, path=[], stack=[], i=0)
	def backtrack(self, s, path, stack, i):
		if len(path) == len(s) and not stack:
			return True
		if i == len(s) and stack:
			return False
		options = ['(', '_', ')'] if s[i] == '*' else s[i]
		for char in options:
			if char == ')' and stack:
				if self.backtrack(s, path + [char], stack[:-1], i + 1):
					return True
			if char == '(':
				if self.backtrack(s, path + [char], stack + [char], i + 1):
					return True
			if char == '_':
				if self.backtrack(s, path + [char], stack, i + 1):
					return True
		return False


Solution().checkValidString("(*)")


