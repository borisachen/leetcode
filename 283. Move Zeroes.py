283. Move Zeroes
Easy/1681/65

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
-----
one pass O(n)
-----
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums: return []
        f = b = -1
        i=0
        n = len(nums)
        while i < n and b < n:
            if nums[i]==0 and f==-1:
                f,b=i,i
            elif nums[i]==0:
                b+=1
            elif nums[i] != 0 and f >= 0:
                nums[i],nums[f]=nums[f],nums[i]
                f+=1
                b+=1
            i+=1
