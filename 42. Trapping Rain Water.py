42. Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it is able to trap after raining.

For example, 
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.


if next height is smaller or equal than the peek() value,
	add the index to the stack,
	increase the index
if next height is larger than the peek value(),
	then its time to add to the pool.  how much?
	bottom = pop the top off
	if there are still items on the stack, that means we can add more water, 
		take the smaller of:
			height[i]
			height[top of stack] ... to be the top water level
		bottom water level is the popped value before (bottom)
		multiply by width
			width = i - topofstack - 1


class Solution(object):
	def trap(self, height):
		"""
		:type height: List[int]
		:rtype: int
		"""
		if not height: return 0
		s = []
		i = 0
		water = 0
		while i < len(height):
			if not s or height[i] <= height[s[-1]]:
				s.append(i)
				i += 1
			else:
				bot_level = height[s.pop()]
				if s:
					top_level = min(height[i], height[s[-1]])
					#print top_level, bot_level
					width = i - s[-1] - 1
					#print width
					water += (top_level - bot_level) * width
		return water

Solution().trap([2,0,2])
















class Solution(object):
	def trap(self, height):
		"""
		:type height: List[int]
		:rtype: int
		"""
		if not height: return 0
		stack = []
		i = 0 
		water = 0
		while i < len(height):
			if not stack or height[i] <= height[stack.peek()]:
				i += 1
				stack.append(i)
			else:
				bottom = stack.pop()
				if len(stack) != 0:
					water += (min(height[stack[-1]], height[i]) - height[bottom]) * (i - stack[-1] - 1)
		return water