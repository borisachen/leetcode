953. Verifying an Alien Dictionary
Easy/1174/473

In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. 
The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, 
return true if and only if the given words are sorted lexicographicaly in this alien language.

Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.

Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).

class Solution(object):
	def isAlienSorted(self, words, order):
		"""
		:type words: List[str]
		:type order: str
		:rtype: bool
		"""
		ind = {c: i for i, c in enumerate(order)}
		for i in range(len(words)-1):
			w1 = words[i]
			w2 = words[i+1]
			if len(w1) > len(w2) and w1[:len(w2)] == w2:
				return False
			for s1, s2 in zip(w1, w2):
				if ind[s1] < ind[s2]:
					break
				elif ind[s1] > ind[s2]:
					return False
		return True

class Solution(object):
	def isAlienSorted(self, words, order):
		"""
		:type words: List[str]
		:type order: str
		:rtype: bool
		"""
		ind = {c: i for i, c in enumerate(order)}
		for i in range(len(words)-1):
			w1 = words[i]
			w2 = words[i+1]
			if len(w1) > len(w2) and w1[:len(w2)] == w2:
				return False
			for i in range(len(w1)):
				if ind[w1[i]] < ind[w2[i]]:
					break
				elif ind[w1[i]] > ind[w2[i]]:
					return False
		return True

Time: O(m*n) where m=numer of words, n = avg lenth of word
Space O(1) = only 26 characters