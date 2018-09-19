325. Maximum Size Subarray Sum Equals k

Given an array nums and a target value k, find the maximum length of a subarray that nums to k. If there isnt one, return 0 instead.

Note:
The sum of the entire nums array is guaranteed to fit within the 32-bit signed integer range.

Example 1:
Given nums = [1, -1, 5, -2, 3], k = 3,
return 4. (because the subarray [1, -1, 5, -2] nums to 3 and is the longest)

Example 2:
Given nums = [-2, -1, 2, 1], k = 1,
return 2. (because the subarray [-1, 2] nums to 1 and is the longest)

Follow Up:
Can you do it in O(n) time?

------------------------------------

Naive solution is to check all combinations, O(n^2)

Is there some type of sliding window approach? 
Say we have two pointers.
The array isnt ordered, so there is no guarantee of increasing or decreasing the current sum. 
So this approach wont work.

Hints:
We can build sum[i] array where sum[i] is the sum of all elements from 0 to i.
sum[i,j] = sum[i] - sum[j]
Use a hashmap
In the map, we still store nums and indicies that we have seen so far,
so that when we look at the next item, we can see if using the current value will get us to K.
key = sum[i]
value = smallest index of this sum

------------------------------------


def max_size_subarray(nums, k):
	best = 0
	maps = {0:-1} # key : nums we've seen, value: index
	n = len(nums)
	# first we build the cumulative sum
	for i in range(1, n):
		nums[i] += nums[i-1]
	for i in range(n):
		if nums[i] - k in maps:   
			best = max(i - maps[nums[i]-k], best)
		if nums[i] not in maps:
			maps[nums[i]] = i
	return best

max_size_subarray(nums = [1, -1, 5, -2, 3], k=3)
max_size_subarray(nums = [-2, -1, 2, 1], k = 1)







