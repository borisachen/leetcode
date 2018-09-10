253. Meeting Rooms II

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), 
find the minimum number of conference rooms required.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return 2.

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




from Queue import PriorityQueue
queue = PriorityQueue()
queue.put(1,2)
queue.get()