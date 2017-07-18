215. Kth Largest Element in an Array

DescriptionHintsSubmissionsSolutions
Total Accepted: 126664
Total Submissions: 328664
Difficulty: Medium
Contributor: LeetCode
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note: 
You may assume k is always valid, 1 ≤ k ≤ arrays length.


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        lo = 0
        hi = len(nums)-1
        while lo < hi:
            p = paritition(nums, lo, hi)

    def paritition(self, nums, lo, hi):
        pivot = nums[hi]
        i = lo
        for j in range(lo, hi):
            if nums[j] < pivot:
                























class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        lo = 0
        hi = len(nums)-1
        while lo < hi:
            p = self.partition(nums, lo, hi)
            if p == k-1: return nums[p]
            if p > k-1: lo = p + 1
            else: hi = p-1
        return nums[0]
    def partition(self, nums, lo, hi):
        pivot = nums[hi]
        l = lo
        r = hi-1
        i = lo
        for j in range(l, r):
            if nums[j] > pivot:
                nums[i], nums[j] = nums[j], nums[i] 
                i += 1
        nums[i], nums[r] = nums[r], nums[i]
        return i





class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
         l         h
        [3,2,1,5,6,4]
        """
        lo = 0
        hi = len(nums)-1
        while lo < hi:
            p = self.partition(nums, lo, hi)
            if p == k-1:
                return nums[p]
            if p > k-1:
                lo = p+1
            else:
                hi = p-1
        return nums[0]
        
    def partition(self, nums, lo, hi): 
        pivot = nums[hi]
        l = lo
        r = hi-1
        i = lo
        for j in range(l, r):
            if nums[j] > pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[r] = nums[r], nums[i]
        return i
            
        
        