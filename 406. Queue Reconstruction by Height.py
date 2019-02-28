406. Queue Reconstruction by Height
Medium/1368/158

Suppose you have a random list of people standing in a queue.
Each person is described by a pair of integers (h, k),
where h is the height of the person and k is the number of people in
front of this person who have a height greater than or equal to h.
Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.


Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

"""
Strategy will be to start with the tallest people,
put them in order by 2nd index.
The repeat for 2nd tallest group, etc.
This works because as we iterate, it is clear where to place each person
from the next lower height group, since we know how many taller
people are before him.

We'll use:
- dictionary to keep trach of people keyed by height
- height array to keep track of all the heights
- result array

runtime: O(nlogn) to sort, but O(n^2) worst case for placement
insert is O(n), we have to do n insertions
"""


class Solution(object):
	def reconstructQueue(self, people):
		"""
		:type people: List[List[int]]
		:rtype: List[List[int]]
		"""
		d = {}
		heights = []
		res = []
		for person in people:
			if person[0] in d:
				d[person[0]] += (person[0], person[1]),
			else:
				heights.append(person[0])
				d[person[0]] = [(person[0], person[1])]
		heights.sort()
		for h in heights[::-1]:
			d[h].sort()
			for p in d[h]:
				res.insert(p[1], [p[0],p[1]])
		return res

Solution().reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]])
