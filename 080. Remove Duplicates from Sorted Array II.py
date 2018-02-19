80. Remove Duplicates from Sorted Array II

Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. 
It doesnt matter what you leave beyond the new length.


class Solution(object):
	def removeDuplicates(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		1 pointer at front.
		for each element, try to add it to a dictionary. 
		if key exists and current count >= 2, 
			"remove": leave front pointer
		if key does not eixst or count < 2:
			swap with the current front
			increment front
		"""
		seen = {}
		front = 0
		count = 0
		for i in range(0, len(nums)):
			if nums[i] in seen and seen[nums[i]] >= 2:
				seen[nums[i]] += 1
			elif nums[i] not in seen:
				nums[front], nums[i] = nums[i], nums[front]
				seen[nums[i]] = 1
				front += 1
				count += 1
			elif seen[nums[i]] < 2:
				nums[front], nums[i] = nums[i], nums[front]
				seen[nums[i]] += 1
				front += 1
				count += 1
		print nums[:5]
		return count

Solution().removeDuplicates([1,1,1,2,2,2,3])



def removeDuplicates(nums):
    i = 0
    for n in nums:
        if i < 2 or n > nums[i-2]:
            nums[i] = n
            i += 1
    print nums
    return i


removeDuplicates([1,1,1,2,2,2,3])
