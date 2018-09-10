239. Sliding Window Maximum
DescriptionHintsSubmissionsDiscussSolution
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Therefore, return the max sliding window as [3,3,5,5,6,7].

Note: 
You may assume k is always valid, ie: 1 ≤ k ≤ input arrays size for non-empty array.

Follow up:
Could you solve it in linear time?
'''
naively we can compute the max of the sliding window at each step.

obviously, we can improve. how?
keep the current sliding window in a list.
we want the first element to be the largest in the list at all times
this means the list should always be decreasing.
so whenever we expand the sliding window, we preserve the decreasing rule.
	- remove all elements in the list that are smaller than [candidate]
then read the first element off.
what do we actually store in the list?
	the index, since we can recover the value with a o(1) lookup
'''


class Solution(object):
	def maxSlidingWindow(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: List[int]
		"""
		n = len(nums)
		if not nums or k <= 0:
			return []
		res = [0]*(n-k+1) # 3-2 ==> 2
		ri = 0
		q = []
		for i in range(n):
			while q and q[0] < i-k+1: # while the first index is out of the left bound
				q = q[1:] # pop it off
			while q and q[-1] < nums[i]: # while the last element is smaller than the current cnadidate, pop it off
				_ = q.pop()
			q.append(i) # add the new candidate
			if i >= k-1: # check if i is valid, 1 >= 2-1
				res[ri] = nums[q[0]]
				ri +=1 
		return res



