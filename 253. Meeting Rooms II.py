253. Meeting Rooms II

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), 
find the minimum number of conference rooms required.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return 2.

0123456789
[ ] 
[      ]
    [  ]
      [  ]
0,2
0,7
4,7
6,7
scan from left to right
count the maximum number of meetings that overlap
in this case its at 7, i need 3 rooms.
so how do we do this algorithmicly ?

Naive:
iterate from 1 to E.
for each i, scan through the entire list and count the number of meetings.
keep track of the max, and reutrn it when done. O(E*n) 

Savings: 
- once i is past a certain meetings endtime, we can throw that meeting away
- if we sort up front, this should allow us to not scan through every meeting every i
- we should only have to check on the end points (?)

use a container
- min heap/priority queue, priority=end time
- whenever we look at a new 

'''
sort by e, then s

find the largest end time, E.
iterate from 0-E

'''
from queue import PriorityQueue

q = PriorityQueue()
q.put(1, 'foo')
q.put(2, 'bar')
q.qsize()
a = q.get()

x = [[0, 30],[5, 10],[15, 20]]

def meetingrooms2(x):
from queue import PriorityQueue
x = sorted(x)
q = PriorityQueue()
q.put(x[0], x[0][1])
for mtg in x[1:]:
	popped = q.get()
	if popped[1] < mtg[0]:
		q.put(mtg, mtg[1])
	else:
		q.put(popped, popped[1])
return q.qsize()

meetingrooms2([[0, 30],[5, 10],[15, 20]])

















