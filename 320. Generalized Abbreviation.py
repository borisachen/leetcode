320. Generalized Abbreviation

Write a function to generate the generalized abbreviations of a word.

Example:
Given word = "word", return the following list (order does not matter):
["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]

-----------------------------------
Standard backtracking approach to generate all permutations

approach 2:
0000 word
0001 wor1
0010 wo1d
0011 wo2
0100 w1rd
0101 w1r1
0110 w2d
0111 w3
1000 1ord
1001 1or1
1010 1o1d
1011 1o2
1100 2rd
1101 2r1
1110 3d
1111 4

Time: There are 2^n solutions. For each solution, we need to build the string which requires O(n),
so time complexity is O(n * 2^n)
Space: Not counting the output storage, we need temp which is O(n).
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