677. Map Sum Pairs
DescriptionHintsSubmissionsDiscussSolution
Implement a MapSum class with insert, and sum methods.

For the method insert, you'll be given a pair of (string, integer). The string represents the key and the integer represents the value. If the key already existed, then the original key-value pair will be overridden to the new one.

For the method sum, you'll be given a string representing the prefix, and you need to return the sum of all the pairs' value whose key starts with the prefix.

Example 1:
Input: insert("apple", 3), Output: Null
Input: sum("ap"), Output: 3
Input: insert("app", 2), Output: Null
Input: sum("ap"), Output: 5

class TrieNode():
	def __init__(self, count=0):
		self.count = count
		self.children = {}

class MapSum(object):

	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.root = TrieNode()
		self.keys = {}

	def insert(self, key, val):
		"""
		:type key: str
		:type val: int
		:rtype: void
		"""
		curr = self.root
		delta = val - self.keys.get(key, 0)
		self.keys[key] = val
		for char in key:
			if char not in curr.children:
				curr.children[char] = TrieNode()
			curr = curr.children[char]
			curr.count += val


	def sum(self, prefix):
		"""
		:type prefix: str
		:rtype: int
		"""
		curr = self.root
		for char in prefix:
			if char not in curr.keys:
				return 0
			curr = curr.children[char]
		return curr.count



# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)