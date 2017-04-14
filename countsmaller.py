class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        naive -- o(n^2)
        """

##  StefanPochmann  solution #2
def countSmaller(self, nums):
    def sort(enum):
        half = len(enum) / 2
        if half:
            left  = sort(enum[:half])
            right = sort(enum[half:])
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

## StefanPochmann   solution #1
def countSmaller(self, nums):
    def sort(enum):
        half = len(enum) / 2
        if half:
            left, right = sort(enum[:half]), sort(enum[half:])
            m, n = len(left), len(right)
            i = j = 0
            while i < m or j < n:
                if j == n or i < m and left[i][1] <= right[j][1]:
                    enum[i+j] = left[i]
                    smaller[left[i][0]] += j
                    i += 1
                else:
                    enum[i+j] = right[j]
                    j += 1
        return enum
    smaller = [0] * len(nums)
    sort(list(enumerate(nums)))
    return smaller

"""
a = [2,4,6] 
b = [1,3,5]
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

def merge(a, b):
    res = []
    i,j = 0,0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            res.append(a[i])
            i += 1
        else: 
            res.append(b[j])
            ###
            j += 1
    if i < len(a):
        res += a[i:]
    elif j < len(b):
        res += b[j:]
    return res



merge([2,4,6], [1,3,5], [0,0,0], [0,0,0])

mergesort([5, 2, 6, 1])

"""

base merge sort:
"""

def mergesort(x):
    if len(x)==0 or len(x)==1:
        return x
    else:
        mid = len(x)/2
        a = mergesort(x[:mid])
        b = mergesort(x[mid:])
        return merge(a,b)

def merge(a,b, left, right): # left, right will keep track of inversions so far
    res = []
    while len(a)>0 and len(b)>0:
        if a[0] < b[0]:
            res += [a[0]]
            a = a[1:]
        else:
            res += [b[0]]
            b = b[1:]
    if len(a) > 0:
        res += a
    if len(b) > 0:
        res += b
    return res
