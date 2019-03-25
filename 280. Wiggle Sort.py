280. Wiggle Sort
Medium (locked)

Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

For example, given nums = [3, 5, 2, 1, 6, 4], one possible answer is [1, 6, 2, 5, 3, 4].

3<5>2<1
3<5>1<2>6
3<5>1<6>2<4
'''
naive: sort, then wiggle.
Time: nlogn for sorting
space: o(1) extra space if heapsort is used

one pass solution: O(n)
local swap words because if there is a violation, swapping it is guaranteed to keep the last inequality true
'''

def doit(x):
	less = True
	for i in range(len(x)-1):
		if less:
			if x[i] > x[i+1]:
				x[i], x[i+1] = x[i+1], x[i]
		if not less:
			if x[i] < x[i+1]:
				x[i], x[i+1] = x[i+1], x[i]
		less = not less
	return x


def doit(x):
	for i in range(len(x)-1):
		if (i%2==0 and x[i] > x[i+1]) or (i%2==1 and x[i] < x[i+1]):
			x[i], x[i+1] = x[i+1], x[i]
	return x


def doit(x):
	for i in range(len(x)-1):
		if ((i%2==0) == x[i] > x[i+1]):
			x[i], x[i+1] = x[i+1], x[i]
	return x


doit([3, 5, 2, 1, 6, 4])
