"""Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].
You need to return the number of important reverse pairs in the given array.
Example1:
Input: [1,3,2,3,1]
Output: 2
Example2:
Input: [2,4,3,5,1]
Output: 3
j=1
mid=0
lo=0
1-0
"""
class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def countwhilemergesort(lo, hi):
        	if lo >= hi: return 0
        	mid = (lo+hi)/2
        	count = countwhilemergesort(lo, mid) + countwhilemergesort(mid+1, hi)
        	for i in range(lo, mid+1):
        		j = mid+1
        		while (j <= hi) and (nums[i] > 2*nums[j]):
        			j+=1
        		count += j-(mid+1)
        	nums[lo:hi] = sorted(nums[lo:hi])
        	return count
        return countwhilemergesort(0, len(nums)-1)


s = Solution()
s.reversePairs([1,3,2,3,1])
s.reversePairs([5,1])
