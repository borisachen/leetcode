class Solution2(object):
    def subsets(self, nums):
        def backtrack(res, temp, nums, start):
            if temp not in res:
                print temp
                res.append(list(temp))
            for i in range(start, n):
                temp = temp + [nums[i]]
                backtrack(res, temp, nums, i+1)
                temp = temp[:-1]
        res = []
        n = len(nums)
        backtrack(res, [], nums, 0)
        return res


s = Solution2()
s.subsets([1,2,3,3])
