71. Simplify Path
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"

class Solution(object):
	def simplifyPath(self, path):
		"""
		:type path: str
		:rtype: str
		"""
		a = [p for p in path.split("/") if p!="." and p!=""]
		stack = []
		for val in a:
			if val=='.':
				continue
			elif val=='..' and len(stack)>0:
				stack.pop()
			else:
				stack.append(val)
		res = "/".join(stack)
		return res

Solution().simplifyPath("/a/./b/../../c/")