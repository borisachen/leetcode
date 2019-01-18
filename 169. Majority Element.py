169. Majority Element
Easy/1329/124

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
-----
1) Store in dictionary. Find largest at the end
Time O(n) to iterate through. Space O(n) for the dictionary.

2) Sort and take the median.
Time O(nlogn), Space O(1)

3) ?
-----
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for item in nums:
            if item in d:
                d[item] += 1
            else:
                d[item] = 1
        maxcount = 0
        res = 0
        for key in d:
            if d[key] > maxcount:
                maxcount = d[key]
                res = key
        return res
