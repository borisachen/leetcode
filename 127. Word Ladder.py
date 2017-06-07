127. Word Ladder
DescriptionHintsSubmissionsSolutions
Total Accepted: 120599
Total Submissions: 624623
Difficulty: Medium
Contributor: LeetCode
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.

front = hit
try all 1-away permutations: 
ait, bit, ... 
...
aog, bog, ...
back = cog

keep the ones that are in wordList.
front_depth, back_depth
check if front and back have any intersection. if yes, return 


class Solution(object):
	def ladderLength(self, beginWord, endWord, wordList):
		"""
		:type beginWord: str
		:type endWord: str
		:type wordList: List[str]
		:rtype: int
		"""
		front = [beginWord]
		back = [endWord]
		depth = 1
		while front and back:
			seen = []
			next_front = self.getNextLayer(front, wordList, seen)
			depth += 1
			if self.inters(next_front, back):
				return depth
			front = next_front
			front, back = back, front
		return 0
	def getNextLayer(self, curr_layer, wordList, seen):
		next_front = []
		for word in curr_layer:
			for i in range(len(word)):
				for c in 'abcdefghijklmnopqrstuvwxyz':
					next_word = word[:i] + c + word[i+1:]
					if next_word in wordList:
						#seen.append(next_word)
						wordList.remove(next_word)
						next_front.append(next_word)
		return next_front
	def inters(self, list_a, list_b):
		for a in list_a:
			for b in list_b:
				if a == b:
					return True
		return False


Solution().ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"])















class Solution(object):
	def ladderLength(self, beginWord, endWord, wordList):
		"""
		:type beginWord: str
		:type endWord: str
		:type wordList: List[str]
		:rtype: int
		"""
		wordList.append(endWord)
		queue = collections.deque([[beginWord,1]])
		while queue:
			word, length = queue.popleft()
			if word == endWord:
				return length
			for i in range(len(word)):
				for c in 'abcdefghijklmnopqrstuvwxyz':
					next_word = word[:i] + c + word[i+1:]
					if next_word in wordList:
						wordList.remove(next_word)
						queue.append([next_word, length+1])
		return 0



class Solution(object):
	def ladderLength(self, beginWord, endWord, wordList):
		"""
		:type beginWord: str
		:type endWord: str
		:type wordList: List[str]
		:rtype: int
		"""
		front = set(beginWord)
		back = set(endWord)
		length = 2
		width = len(beginWord)
		charSet='abcdefghijklmnopqrstuvwxyz'
		wordList.remove(endWord)
		while front:
			front = wordList & (set(word[:i] + ch + word[i+1:] for word in front
								for i in range(len(beginWord)
									for ch in charSet)))
			if front & back:
				return length
			length += 1
			if len(front) > len(back):
				front, back = back, front
			wordDict -= front
		return 0