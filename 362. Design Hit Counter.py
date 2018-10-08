362. Design Hit Counter

Design a hit counter which counts the number of hits received in the past 5 minutes.

Each function accepts a timestamp parameter (in seconds granularity) and you may assume that calls are being made to the system in chronological order (ie, the timestamp is monotonically increasing). You may assume that the earliest timestamp starts at 1.

It is possible that several hits arrive roughly at the same time.

Example:
HitCounter counter = new HitCounter();

// hit at timestamp 1.
counter.hit(1);

// hit at timestamp 2.
counter.hit(2);

// hit at timestamp 3.
counter.hit(3);

// get hits at timestamp 4, should return 3.
counter.getHits(4);

// hit at timestamp 300.
counter.hit(300);

// get hits at timestamp 300, should return 4.
counter.getHits(300);

// get hits at timestamp 301, should return 3.
counter.getHits(301); 
Follow up:
What if the number of hits per second could be very large? Does your design scale?

Credits:
Special thanks to @elmirap for adding this problem and creating all test cases.

-----------------------------------
Solution 1:
we can use a simple queue or a priority queue
when we query for the gethits, we pop off until the time is under current time - 300.

Solution 2:
store all of the incoming timestamps in a list. 
we dont delete any of them
upon query for counter, for loop through the list and count until the ts i > 300.

-----------------------------------

class hitcounter(object):
	def __init__(self):
		self.q = []
	def hit(self, ts):
		self.q.append(ts)
	def getHits(self, ts):
		while q and ts - q[0] > 300:
			q.pop(0)
		return len(q)
