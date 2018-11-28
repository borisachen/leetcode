281. Zigzag Iterator

Given two 1d vectors, implement an iterator to return their elements alternately.

For example, given two 1d vectors:

v1 = [1, 2]
v2 = [3, 4, 5, 6]
By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1, 3, 2, 4, 5, 6].

Follow up: What if you are given k 1d vectors? How well can your code be extended to such cases?

Clarification for the follow up question - Update (2015-09-18):
The "Zigzag" order is not clearly defined and is ambiguous for k > 2 cases. If "Zigzag" does not look right to you, replace "Zigzag" with "Cyclic". For example, given the following input:

[1,2,3]
[4,5,6,7]
[8,9]
It should return [1,4,8,2,5,9,3,6,7].

--------------------------------------------------
We will keep 4 strorage bins: curr/next vector/index.
When we ask for the next,
we can increase the current index counter then,
if the next index is valid in the next vector, we swap both
- vector <-> vector
- index <-> index
the result of this is that if the next/next is not valid, we keep the current vector and increase the current index.
--------------------------------------------------
class zigzag(object):
	def __iter__(self, v1, v2):
		if len(v1) == 0:
			v1, v2 = v2, v1
			self.currVec = v1
			self.nextVec = v2
			self.currIdx = 0
			self.nextIdx = 0
	def next(self):
		ret = self.currVec[currIdx]
		self.currIdx += 1
		if self.nextIdx < len(self.nextVec):
			self.currVec, self.nextVec = self.nextVec, self.currVec
			self.currIdx, self.nextIdx = self.nextIdx, self.currIdx
		return ret
	def hasNext(self):
		return self.currIdx < len(self.currVec)

# generalize to k: 
class zigzag(object):
	def __iter__(self, v1,v2):
		self.list = []
		if v1: self.list.append(v1)
		if v2: self.list.append(v2)
	def next(self):
		poll = self.list.pop(0)
		res = poll.pop(0)
		if poll:
			self.list.append(poll)
		return res
	def hasNext():
		return self.list != None


