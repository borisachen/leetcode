691. Stickers to Spell Word

We are given N different types of stickers. Each sticker has a lowercase English word on it.

You would like to spell out the given target string by cutting individual letters from your collection of stickers 
and rearranging them.

You can use each sticker more than once if you want, and you have infinite quantities of each sticker.

What is the minimum number of stickers that you need to spell out the target? If the task is impossible, return -1.

Example 1:

Input:

["with", "example", "science"], "thehat"
Output:

3
Explanation:

We can use 2 "with" stickers, and 1 "example" sticker.
After cutting and rearrange the letters of those stickers, we can form the target "thehat".
Also, this is the minimum number of stickers necessary to form the target string.
Example 2:

Input:

["notice", "possible"], "basicbasic"
Output:

-1
Explanation:

We cant form the target "basicbasic" from cutting letters from the given stickers.
Note:

stickers has length in the range [1, 50].
stickers consists of lowercase English words (without apostrophes).
target has length in the range [1, 15], and consists of lowercase English letters.
In all test cases, all words were chosen randomly from the 1000 most common US English words, and the target was chosen as a concatenation of two random words.
The time limit may be more challenging than usual. It is expected that a 50 sticker test case can be solved within 35ms on average.
'''
note:
- order of target doesn't matter, can store it as dictionary counter
backtrack
'''

# with help
class Solution(object):
	def minStickers(self, stickers, target):
		"""
		:type stickers: List[str]
		:type target: str
		:rtype: int
		"""
		m = len(stickers)
		mp = [[0]*26 for _ in range(m)] # 26 x m
		for i in range(m):
			for c in stickers[i]:
				mp[i][ord(c) - ord('a')] += 1
		dp = {}
		dp[""] = 0


# On my own:
class Solution(object):
	def minStickers(self, stickers, target):
		"""
		:type stickers: List[str]
		:type target: str
		:rtype: int
		"""
		import sys
		from collections import Counter
		res = sys.maxint
		d = Counter(target)
		print(d)
		print(d.values())
		self.backtrack(stickers, target, [], d, res)
	def backtrack(self, stickers, target, path, d, res):
		# win condition
		if d.values() == [0] * len(d):
			res = min(res, len(path))
		# lose condition
		if path:
			d_cand = Counter(path[-1])
			new_word_letters = d_cand.keys()

		for cand_word in stickers:
			pass

Solution().minStickers(["with", "example", "science"], "thehat")


foo = {'a':0, 'b':0}
foo.values() == [0] * len(foo)
[x in ['c','d'] for x in ['a', 'b']]












