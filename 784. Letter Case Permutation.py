784. Letter Case Permutation
Easy/486/61

Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.

Examples:
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]
Note:

S will be a string with length between 1 and 12.
S will consist only of letters or digits.

We want to generate all possible sequences, so well do a recursive search.
Number dont need another branch.
Alphabet characters require to searches
Time: Worst case ever character is a letter, so 2*2*...*2 n times = O(2^n) combinations
Space: Also O(2^n)
---------------------------


def dfs(temp, n, res, i, S):
	if len(temp) == n:
		res.append(temp)
		return
	if S[i] in 'abcdefghijklmnopqrstuvwxyz':
		dfs(temp + str.lower(S[i]), n, res, i+1, S)
		dfs(temp + str.upper(S[i]), n, res, i+1, S)
	else:
		dfs(temp + S[i], n, res, i+1, S)

def letter_case_permutation(S):
	n = len(S)
	res = []
	dfs('', n, res, 0, S)
	return(res)

letter_case_permutation(S='a1b2')

letter_case_permutation(S='3z4')

letter_case_permutation(S='12345')

class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        res = []
        self.back(S, '', 0, res)
        return res

    def back(self, S, temp, i, res):
        if len(temp) == len(S):
            res.append(temp)
            return
        if S[i].isdigit():
            self.back(S, temp+S[i], i+1, res)
        else:
            self.back(S, temp+S[i].lower(), i+1, res)
            self.back(S, temp+S[i].upper(), i+1, res)
        return
