179. Largest Number
Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.


1. convert to strings, then define comparator on a+b > b+a

class Solution():
	# @param {integer[]} nums
	# @return {string}
	def largestNumber(self, nums):
		comp = lambda a,b: 1 if a+b>b+a else -1 if a+b<b+a else 0
		nums = map(str, nums)
		nums.sort(reverse=True, cmp=comp)
		

Solution().largestNumber([3, 30, 34, 5, 9])