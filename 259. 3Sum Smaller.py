259. 3Sum Smaller

Given an array of n integers nums and a target, 
find the number of index triplets i, j, k with 0 <= i < j < k < n 
that satisfy the condition nums[i] + nums[j] + nums[k] < target.

For example, given nums = [-2, 0, 1, 3], and target = 2.

Return 2. Because there are two triplets which sums are less than 2:

[-2, 0, 1]
[-2, 0, 3]
Follow up:
Could you solve it in O(n2) runtime?

------------------------
Naive solution is 3 for loops. O(n^3)

Key intution: re sorting doesnt affect the solution.
This is because a 3 tuple that works will still work after being sorted.
The order effectively doesnt matter:

0 1 2 3 --- index
3 1 0 -2
-2 0 1 3

1,0,-2 and -2,0,1 still work for both i<j<k

Therefore: fix i, then use two pointer from each end.
Whenever nums[i] + nums[lo] + nums[hi] < target:
all the solutions in between lo and hi work, soo add hi - lo 
------------------------

class Solution(object):
	def threesumsmaller(self, numbs, target):
		if not nums: return 0
		count = 0
		n = len(nums)
		nums = sorted(nums)
		for i in range(n-2):
			lo = i + 1
			hi = n - 1
			while lo < hi:
				if nums[i] + nums[lo] + nums[hi] < target:
					count += hi - lo
					lo += 1
				else:
					hi -= 1
			return count