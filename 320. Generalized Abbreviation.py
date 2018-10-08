320. Generalized Abbreviation

Write a function to generate the generalized abbreviations of a word.

Example:
Given word = "word", return the following list (order does not matter):
["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]

-----------------------------------
Standard backtracking approach to generate all permutations
-----------------------------------

import pdb

def backtrack(temp, i, res, word):
	if i == len(word):
		res.append(temp); 
		return
	for j in range(i, len(word)):
		num = str(j-i) if j-i>0 else ''
		backtrack(temp + num + word[j], j+1, res, word) # backtracks 0...n-1 + word[n]
	backtrack(temp + str(len(word)-i), len(word), res, word) # appends the largest possible digit at the end

res = []
backtrack('', 0, res, 'word')
print(res)


class Solution(object):
    def generateAbbreviations(self, word):
        def backTrack(word, i, seq, res):
            if i == len(word): res.append(seq); return
            for j in range(i, len(word)):
                num = str(j - i) if j - i > 0 else ''
                backTrack(word, j + 1, seq + num + word[j], res)
            backTrack(word, len(word), seq + str(len(word) - i), res)
        res = []
        backTrack(word, 0, '', res)
        return res

Solution().generateAbbreviations('word')