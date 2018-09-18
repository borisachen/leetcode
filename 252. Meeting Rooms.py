252. Meeting Rooms

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), 
determine if a person could attend all meetings.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return false.

------------------------------------

Sort first by start time.
Examine one meeting at time.
If the current end time is after the next start time, return false.
If we make it to the end with no violations, return true.

------------------------------------

mtgs = [[0, 30],[5, 10],[15, 20]]

def meeting_rooms(mtgs):
	s = sorted(mtgs)
	for i in range(len(s)-1):
		if s[i][1] > s[i+1][0]:
			return False
	return True


meeting_rooms(mtgs)
