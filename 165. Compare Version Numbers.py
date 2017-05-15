165. Compare Version Numbers
Compare two version numbers version1 and version2.
If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 13.37

1. split each number by period
if left 

class Solution(object):
	def compareVersion(self, version1, version2):
		"""
		:type version1: str
		:type version2: str
		:rtype: int
		"""
		v1a, v1b = version1.split(".")
		v2a, v2b = version2.split(".")
		if v1a > v2a: return 1
		if v1a < v2a: return -1
		if v1a == v2a:
			if v1b > v2b: return 1
			if v1b < v2b: return 1
		return 0