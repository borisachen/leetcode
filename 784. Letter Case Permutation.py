784. Letter Case Permutation

Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  
Return a list of all possible strings we could create.

Examples:
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]
Note:

S will be a string with length at most 12.
S will consist only of letters or digits.

---------------------------
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
