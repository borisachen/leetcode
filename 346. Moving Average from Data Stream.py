346. Moving Average from Data Stream

Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

For example,
MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3

--------------------------------------------------
Naively:
- if we just kept a queue and push new items on and pop items off the back,
- we can insert in O(1) add add to a internal sum
- When we pop off, we subtract that value from the internal sum
--------------------------------------------------

class moving_avg(object):
	
	def init(size):
		self.size = size
		self.q = []
		self.internalsum = 0

	def next(self, n):
		if len(q) > size:
			internalsum -= self.q.pop(0)
		self.q.append(n)
		internalsum += n
		return internalsum / len(q)