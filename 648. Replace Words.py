648. Replace Words
Medium/392/99

In English, we have a concept called root, which can be followed by some other words to form another longer word -
lets call this word successor. For example, the root an, followed by other, which can form another word another.

Now, given a dictionary consisting of many roots and a sentence.
You need to replace all the successor in the sentence with the root forming it.
If a successor has many roots can form it, replace it with the root with the shortest length.

You need to output the sentence after the replacement.

Example 1:
Input: dict = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"
Note:
The input will only have lower-case letters.
1 <= dict words number <= 1000
1 <= sentence words number <= 1000
1 <= root length <= 100
1 <= sentence words length <= 1000


"""
use a trie to store the dict
iterate for each word
	check for existence in the trie
		if yes, replace
		if no, do nothing
"""


d = ["cat", "bat", "rat", "rar", "card"]
trie = {}
for word in d:
	curr = trie
	for i, char in enumerate(word):
		if char not in curr:
			curr[char] = {}
		curr = curr[char]

print trie


class Solution(object):
	def replaceWords(self, dict, sentence):
		"""
		:type dict: List[str]
		:type sentence: str
		:rtype: str
		"""
		trie = self.get_trie(dict)
		print trie
	def get_trie(self, dict):
		trie = {}
		for word in dict:
			curr = trie
			for i, char in enumerate(word):
				if char not in curr:
					curr[char] = {}
				curr = curr[char]
		return trie

Solution().replaceWords(["cat", "bat", "rat"], "the cattle was rattled by the battery")
