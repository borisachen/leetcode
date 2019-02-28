480. Sliding Window Median
Hard/331/37

Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

Examples:
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Your job is to output the median array for each window in the original array.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Median
---------------               -----
[1  3  -1] -3  5  3  6  7       1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7       3
 1  3  -1  -3 [5  3  6] 7       5
 1  3  -1  -3  5 [3  6  7]      6
Therefore, return the median sliding window as [1,-1,-1,3,5,6].

'''
for any winddow, ideally we can access the lowest index item and median in O(1)

if we store two versions of the window. one as a normal list,
one as a sorted list.

the normal list tells us which item to pop off.
the sorted list tell us which is the median.

now the question is how to pop from the median list.
'''
Array based solution:
the window is an array maintained in sorted order
the mid of the array is used to calculate the median
every iteration, the incoming number is added in sorted order in the array using insert - O(log K) ?
every iteration, the outgoing number is removed from the array using bisect O(log K) ?
O(N logK) beats 100%


# 132 ms
class SolutionSortedArrayFast(object):
    def medianSlidingWindow(self, nums, k):
        win, rv = nums[:k], []
        win.sort()
        odd = k%2
        for i,n in enumerate(nums[k:],k):
            rv.append((win[k/2]+win[k/2-1])/2. if not odd else win[(k-1)/2]*1.)
            win.pop(bisect(win, nums[i-k])-1) # <<< bisect is faster than .remove()
            insort(win, nums[i])
        rv.append((win[k/2]+win[k/2-1])/2. if not odd else win[(k-1)/2]*1.)
        return rv
