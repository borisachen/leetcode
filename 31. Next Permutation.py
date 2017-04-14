"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

My idea is for an array:

Start from its last element, traverse backward to find the first one with index i that satisfy num[i-1] < num[i]. 
 
 1 2 3 2 1 
     i
So, elements from num[i] to num[n-1] is reversely sorted.

To find the next permutation, we have to swap some numbers at different positions, to minimize the increased amount, 
we have to make the highest changed position as high as possible. Notice that index larger than or equal to i is not 
possible as num[i,n-1] is reversely sorted. So, we want to increase the number at index i-1, clearly, swap it with 

the smallest number between num[i,n-1] that is larger than num[i-1]. For example, original number is 
012345678
121543321, 
122543311, 
we want to swap the '1' at position 2 with '2' at position 7.

The last step is to make the remaining higher position part as small as possible, we just have to reversely sort the num[i,n-1]

"""

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = len(nums)-1
        while nums[i] < nums[i-1] and i >= 0:
        	i -= 1
        if i==0:
        	pass
        