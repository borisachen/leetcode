127. Word Ladder

Given two words (beginWord and endWord), and a dictionarys word list, 
find the length of shortest transformation sequence from beginWord to endWord, such that:

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
UPDATE (2017/1/20):
The wordList parameter had been changed to a list of strings (instead of a set of strings). 
Please reload the code definition to get the latest changes.

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