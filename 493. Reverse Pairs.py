493. Reverse Pairs

Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].

You need to return the number of important reverse pairs in the given array.

Example1:

Input: [1,3,2,3,1]
Output: 2
Example2:

Input: [2,4,3,5,1]
Output: 3
Note:
The length of the given array will not exceed 50,000.
All the numbers in the input array are in the range of 32-bit integer.

1. d/c. merge sort, count reverse pairs while merging.

class Solution(object):
	def reversePairs(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		x, ans = self.mergeSort(nums)
		return ans
	def mergeSort(self, x):
		if len(x) <= 1: return x, 0
		mid = len(x) / 2
		left, left_count = self.mergeSort(x[:mid])
		right, right_count = self.mergeSort(x[mid:])
		y, ans = self.myMerge(left, right)
		return y, ans + left_count +right_count
	def myMerge(self, a, b):
		ans = 0
		mergedlist = []
		while a and b:
			if a[0] <= b[0]:
				mergedlist.append(a[0])
				a = a[1:]
			else:
				mergedlist.append(b[0])
				for item in list(a):
					if item > b[0]*2.0:
						ans += 1
				b = b[1:]
		if a: 
			for item in a:
				mergedlist.append(item)
		elif b:
			for item in b:
				mergedlist.append(item)
		return mergedlist, ans

Solution().reversePairs([5,4,3,2,1]) # 4






"""
class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def countwhilemergesort(lo, hi):
        	mid = (lo+hi)/2
        	if lo >= mid: return 0
        	count = countwhilemergesort(lo, mid) + countwhilemergesort(mid+1, hi)
        	i = lo
        	j = mid+1
        	while i <= mid:
        		while j <= hi and nums[i]/2.0 > nums[j]: 
        			j+=1
        		count += j-mid-1
        		i += 1
        	nums[lo:hi] = sorted(nums[lo:hi])
        	return count
        return countwhilemergesort(0, len(nums)-1)
        """