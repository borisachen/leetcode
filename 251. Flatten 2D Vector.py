251. Flatten 2D Vector

Implement an iterator to flatten a 2d vector.

For example,
Given 2d vector =

[
  [1,2],
  [3],
  [4,5,6]
]
By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,2,3,4,5,6].

Follow up:
As an added challenge, try to code it using only iterators in C++ or iterators in Java.

--------------------------------------------------
We can use two iterators
- one for the rows
- one for the columns
--------------------------------------------------

def flatten(object):
	self.column = iter()
	def __iter__(self, v):
		self.row = iter(v)
	def next(self):
		self.hasNext()
		return self.column.next()
	def hasNext(self):
		while (column==None or not column.hasNext()) and row.hasNext():
			column = iter(row.next())
		return column != None and column.hasNext()
		