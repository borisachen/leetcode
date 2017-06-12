315. Count of Smaller Numbers After Self

You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example:

Given nums = [5, 2, 6, 1]

To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
Return the array [2, 1, 1, 0].

idea: divide/conquer with merge sort type solution, count inversions during merge step

class Solution(object):
	def countSmaller(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[int]
		"""
		ans = [0]*len(nums)
		index_nums = list(enumerate(nums)) # (index, number)
		def msort(x):
			if not x: return x
			if len(x) == 1: return x
			half = len(x) / 2
			left, right = msort(x[:half]), msort(x[half:])
			for i in range(x)[::-1]:
				if not right or left and left[-1][1] > right[-1][1]:
					ans[left[-1][0]] += len(right)
					x[i] = left.pop()
				else:
					x[i] = right.pop()
			return x
		msort(index_nums)
		return ans













class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        naive -- o(n^2)
        """
        """
        def mergesort(x):
            if len(x)==0: 
                return x, []
            if len(x)==1:
                return x, [0]
            mid = len(x)/2
            a, A = mergesort(x[:mid])
            b, B = mergesort(x[mid:])
            y, Y = merge(a, b, A, B)
            return y,Y
        
        def merge(a, b, left, right):
            res = []
            i,j = 0,0
            while i < len(a) and j < len(b):
                if a[i] <= b[j]:
                    res.append(a[i])
                    i += 1
                else: 
                    res.append(b[j])
                    for k in range(i, len(left)):
                        left[k] += 1
                    j += 1
            if i < len(a):
                res += a[i:]
            elif j < len(b):
                res += b[j:]
            return res, left + right
        
        return mergesort(nums)[1]
        """
        def sort(enum):
            half = len(enum) / 2
            if half:
                left, right = sort(enum[:half]), sort(enum[half:])
                for i in range(len(enum))[::-1]:
                    if not right or left and left[-1][1] > right[-1][1]:
                        smaller[left[-1][0]] += len(right)
                        enum[i] = left.pop()
                    else:
                        enum[i] = right.pop()
            return enum
        smaller = [0] * len(nums)
        sort(list(enumerate(nums)))
        return smaller
        