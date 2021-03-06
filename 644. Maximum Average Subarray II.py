644. Maximum Average Subarray II ???
Medium

Given an array consisting of n integers, find the contiguous subarray
whose length is greater than or equal to k that has the maximum average value.
And you need to output the maximum average value.

Example 1:
Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation:
when length is 5, maximum average value is 10.8,
when length is 6, maximum average value is 9.16667.
Thus return 12.75.
Note:
1 <= k <= n <= 10,000.
Elements of the given array will be in range [-10,000, 10,000].
The answer with the calculation error less than 10-5 will be accepted.

----
'''
Approach 1: Naive
Compute all i,j. combinations.
Throw out the ones that are less than k.
Take the maximum.
O(n^2)

TODO: Approach 2: O(n log(max-min))??
https://leetfree.com/problems/maximum-average-subarray-ii.html?tab=solution
'''
----


def doit(nums, k):
	n = len(nums)
	sums = []
	left = ?
	right = ?
	while right - left > 1e-5:
		minsum = 0
		mid = left + (right-left)/2
		check = False
		for i in range(1, n):
			sums[i] = sums[i-1] + nums[i-1] - mid
			if i >= k:
				minsum = min(minsum, sums[i-k])
			if i >= k and sums[i] > minsum:
				check = True
				break
		if check:
			left = mid
		else:
			right = mid
	return left
