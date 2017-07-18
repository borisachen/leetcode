238. Product of Array Except Self 

Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose of space complexity analysis.)

1. Use tmp to store temporary multiply result by two directions. Then fill it into result. Bingo!

right:
num 1 2 3 4
res 1 1 2 6
tmp 1 2 6 24

left:
num 1  2  3 4
res 24 12 8 6
tmp 24 12 4 1 


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [None]*len(nums)
        tmp = 1
        for i in range(len(nums)):
        	res[i] = tmp
        	tmp *= nums[i]
        tmp = 1
        for i in range(len(nums))[::-1]:
        	res[i] *= tmp
        	tmp *= nums[i]
        return res