547. Friend Circles
Medium/897/65

There are N students in a class. Some of them are friends, while some are not.
Their friendship is transitive in nature.
For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C.
And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class.
If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not.
And you have to output the total number of friend circles among all the students.

Example 1:
Input:
[[1,1,0],
 [1,1,0],
 [0,0,1]]
Output: 2
Explanation:The 0th and 1st students are direct friends, so they are in a friend circle.
The 2nd student himself is in a friend circle. So return 2.
Example 2:
Input:
[[1,1,0],
 [1,1,1],
 [0,1,1]]
Output: 1
Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends,
so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.
Note:
N is in range [1,200].
M[i][i] = 1 for all students.
If M[i][j] = 1, then M[j][i] = 1.

"""
We'll use a DFS approach.
Use an array "visited" to keep track of which students have been visited.

iterate through each student.
if the students hasn't been visited, DFS on that student.

in each dfs call, iterate through the list and whenever
we see a student that is friends (1) and hasn't been visited,
make a recursive DFS call.
once we're done with each top level DFS call, increment the counter by 1.
"""

class Solution(object):
	def findCircleNum(self, M):
		"""
		:type M: List[List[int]]
		:rtype: int
		"""
		visited = [0]*len(M)
		count = 0
		for i in range(len(M)):
			if visited[i] == 0:
				self.dfs(M, visited, i)
				count += 1
		return count
	def dfs(self, M, visited, i):
		for j in range(len(M)):
			if M[i][j] == 1 and visited[j] == 0:
				visited[j] = 1
				self.dfs(M, visited, j)
