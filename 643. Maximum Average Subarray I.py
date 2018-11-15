643. Maximum Average Subarray I

Given an array consisting of n integers, 
find the contiguous subarray of given length k that has the maximum average value. 
And you need to output the maximum average value.

Example 1:
Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
Note:
1 <= k <= n <= 30,000.
Elements of the given array will be in the range [-10,000, 10,000].

-----
two pointers, k distance apart.
running sum
-----


def maxavgsub(x, k):
	cursum = 0
	for i in range(k):
		cursum += x[i]
	maxsofar = cursum
	i = 0
	j = k
	while j < len(x):
		print(i,j,cursum)
		cursum -= x[i]
		cursum += x[j]
		if cursum > maxsofar:
			maxsofar = cursum
		i+=1
		j+=1
	return maxsofar*1.0 / k


maxavgsub(x=[1,12,-5,-6,50,3], k = 4)


