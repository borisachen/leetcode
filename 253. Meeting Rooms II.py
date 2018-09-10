253. Meeting Rooms II

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), 
find the minimum number of conference rooms required.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return 2.

<<<<<<< HEAD
greedy approach?

[       ]
  []
     []

we need something that stores the current state of rooms that are occupied
if all rooms are occupied, then we need to add a new one
once a room becomes vacant, we should take note of that.

first sort, twice
(then step through by time?)
init largestsofar
init PriorityQueue/minheap -- this will track all the meetings currently being used
or step though by meeting
- for each meeting, look at the start time
	- we want to pop off everything in queue that has already ended
	- add the current item (end time only should suffice)
	- keep track of the largest queue size that we have seen so far
=======
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




>>>>>>> 5a9546d853067ebbd2f94166186ba4346db3935e






<<<<<<< HEAD
def meeting_rooms_2(meeting_list):
	from Queue import PriorityQueue
	queue = PriorityQueue()
	largest_so_far = 0
	meeting_list = sorted(meeting_list)
	for mtg in meeting_list:
		# want to pop off everything in current_rooms that has ended
		while queue:
			popped = queue.get()
			if popped > mtg[0]:
				break
		queue.put(popped, popped)
		#add current item
		queue.put(mtg[1], mtg[1])
		#update largest
		if queue.size() > largest_so_far:
			largest_so_far = queue.size()
	return largest_so_far



x = [[0, 30],[5, 10],[15, 20]]
meeting_rooms_2(x)
=======



>>>>>>> 5a9546d853067ebbd2f94166186ba4346db3935e




<<<<<<< HEAD
from Queue import PriorityQueue
queue = PriorityQueue()
queue.put(1,2)
queue.get()
=======
>>>>>>> 5a9546d853067ebbd2f94166186ba4346db3935e
