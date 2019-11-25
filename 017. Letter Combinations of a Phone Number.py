17. Letter Combinations of a Phone Number
Medium
2792/349

Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.

""""""
use an array to store the mappings
iteratively loop through each char
"""

class Solution(object):
	def letterCombinations(self, digits):
		"""
		:type digits: str
		:rtype: List[str]
		"""
		res = []
		dic = ["0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
		for i, d in enumerate(digits):
			if not res:
				for char in dic[int(d)]:
					res.append(char)
			else:
				nextlevel = []
				for char in dic[int(d)]:
					for item in res:
						nextlevel.append(str(item) + str(char))
				res = nextlevel
		return res


def doit(digits):
	res = []
	dic = ["0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
	dfs()
	return

def dfs(temp, i, digits, res):
	if i >= len(digits):
		res.append(temp)
		return
	letters = dic[digits[i]]

def dfs(prefix, digits, offset, res):
	if offset >= len(digits):
		res.append(prefix)
		return
	letters = dic[digits[offset] - '0']
	for i in len(letters):
		dfs(prefix + letters[i], digits, offset + 1, res)
	return
