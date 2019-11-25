11. Container With Most Water
Medium
4274/490

Given n non-negative integers a1, a2, ..., an, where each represents a point at
coordinate (i, ai). n vertical lines are drawn such that the two endpoints of
line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis
forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

"""
Naive solution considers all pairs of points, O(n^2) time, O(1) space.
It can be implemented with a double for loop.

We can do a two pointer, outside-in sweep.
If the left is shorter than the right, then there is no point moving the right pointer in.
If the heights are equal, then it doesn't matter which one we move.
    if the inside one is taller, we can't use it anyway.
Track the best so far seen as we search.

Time: O(n)
Space: O(1)
"""

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        lo, hi = 0, len(height)-1
        res = 0
        while lo < hi:
            area = (hi - lo) * min(height[lo], height[hi])
            if area > res:
                res = area
            if height[lo] < height[hi]:
                lo += 1
            else:
                hi -= 1
        return res
