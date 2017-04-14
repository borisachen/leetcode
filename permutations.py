"""Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(res, temp, nums, start):
            if len(temp)==len(nums):
                res.append(temp)
            for i in range(start, len(nums)):
                if nums[i] in temp: continue
                temp = temp + [nums[i]]
                backtrack(res, temp, nums, 0)
                temp = temp[:-1]
        res = []
        backtrack(res, [], nums, 0)
        return res

s = Solution()
a = [1,2,3]
s.permute(a)


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        perms = [[]]
        for n in nums:
            new_perms=[]
            for perm in perms:
                for i in range(len(perm)+1):
                    new_perms.append(perm[:i] + [n] + perm[i:])
            perms = new_perms
        return perms