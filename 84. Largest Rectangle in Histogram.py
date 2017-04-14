84. Largest Rectangle in Histogram

Given n non-negative integers representing the histograms bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

The stack maintains the indexes of buildings with ascending height. 
Before adding a new building, pop the building who is taller than the new one. 
The building popped out represent the height of a rectangle with 
	the new building as the right boundary and 
	the current stack top as the left boundary. 
Calculate its area and update ans of maximum area.
Boundary is handled using dummy buildings.
"""
- iterate, add new index to stack as long as new height is greater than peek'd height
- if we add one that is going to be shorter
	- pop until the top of stack is less than the curr height
	- for each popped, computer maxarea = max(maxarea, h*w)
	- where h = curr height, w = i-poppedindex-1

"""
class Solution(object):
	def largestRectangleArea(self, heights):
		"""
		:type heights: List[int]
		:rtype: int
		"""
		heights.append(0)
		stack = [-1]
		res = 0
		for i in xrange(len(heights)):
			while heights[i] < heights[stack[-1]]:
				h = heights[stack.pop()]
				w = i-stack[-1]-1
				res = max(res, h*w)
			stack.append(i)
		return res



class Solution(object):
	def largestRectangleArea(self, heights):
		"""
		:type heights: List[int]
		:rtype: int
		"""
		heights.append(0)
		stack = [-1]
		maxarea = 0
		for i in xrange(len(heights)):
			while heights[i] < heights[stack[-1]]:
				h = heights[stack.pop()]
				w = i - stack[-1] - 1
				maxarea = max(maxarea, h*w)
			stack.append(i)
		heights.pop()
		return maxarea