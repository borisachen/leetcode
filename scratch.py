20. Valid Parentheses
Easy
2356/115

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true


def isvalid(s):
	stack = []
	d = {'}':'{', ']':'[', ')':'('}
	for char in s:
		if char in d.values():
			stack.append(char)
		elif char in d.keys():
			if stack == [] or d[char] != stack.pop():
				return False
		else:
			return False
	return stack == []

isvalid("()")
isvalid(s="()[]{}")
isvalid(s="(]")
isvalid(s="([)]")
isvalid(s="{[]}")

