228. Summary Ranges 

Given a sorted integer array without duplicates, return the summary of its ranges.

For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].

class Solution(object):
	def summaryRanges(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[str]
		"""
		ranges = []
		for n in nums:
			if not ranges or n > ranges[-1][-1]:
				ranges.append([])
			ranges[-1][1:] = [n]
			return ['->'.join(map(str, r)) for r in ranges]