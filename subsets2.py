class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(nums, temp, res, start):
            if True:
                #print temp
                res.append(temp)
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                #print type(temp), type(nums[i])
                #print temp, nums[i]
                temp = list(temp) + [nums[i]]
                backtrack(nums, temp, res, i+1)
                temp = temp[:-1]
            
        res = []
        backtrack(nums, [], res, 0)
        return res

s = Solution()
s.subsetsWithDup([4,4,4,1,4])
