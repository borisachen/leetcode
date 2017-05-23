210. Course Schedule II 

There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, 
which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, 
return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1]

4, [[1,0],[2,0],[3,1],[3,2]]
There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. So one correct course order is [0,1,2,3]. Another correct ordering is[0,2,1,3].

Note:
The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.

class Solution(object):
	def findOrder(self, numCourses, prerequisites):
		"""
		:type numCourses: int
		:type prerequisites: List[List[int]]
		:rtype: List[int]
		"""
		dic = collections.defaultdict(set)
		neigh = collections.defaultdict(set)
		for i, j in prerequisites:
			dic[i].add(j)
			neigh[j].add(i)
		stack = [i for i in range(numCourses) if not dic[i]]
		res = []
		while stack:
			node = stack.pop()
			res.append(node)
			for i in neigh[node]:
				dic[i].remove(node)
				if not dic[i]:
					stack.append(i)
			dic.pop(node)
		return res if not dic else []