1011. Capacity To Ship Packages Within D Days
Medium/245/9

A conveyor belt has packages that must be shipped from one port to another
within D days.

The i-th package on the conveyor belt has a weight of weights[i].  Each day, we
load the ship with packages on the conveyor belt (in the order given by weights).
We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages
on the conveyor belt being shipped within D days.

Example 1:
Input: weights = [1,2,3,4,5,6,7,8,9,10], D = 5
Output: 15
Explanation:
A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10
Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.

Example 2:
Input: weights = [3,2,2,4,1,4], D = 3
Output: 6
Explanation:
A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:
1st day: 3, 2
2nd day: 2, 4
3rd day: 1, 4

Example 3:
Input: weights = [1,2,3,1,1], D = 4
Output: 3
Explanation:
1st day: 1
2nd day: 2
3rd day: 3
4th day: 1, 1

Note:
1 <= D <= weights.length <= 50000
1 <= weights[i] <= 500

'''
Brute force : try all asignments from
W=max(weights) (each gets its own buckets) to
W=sum(weights) (everything in 1 bucket)
buckets=1 - trivial
buckets=2 ==> O(n)
buckets=3 ==> O(n^2)
...
keep track of the smallest weight bucket we encountered.
so in general this is O(n^d)

Notice:
we know the minimum possible (max of weights)
as well as the maximum possible (sum of all the weights)
We can evaluate whether a single guess of W is possible in O(n) by doing
a greedy one pass search -- fill buckets from the left until they are full,
then add a bucket.
So do a binary search on possible values.
This gives a O(log(sum_W - maxW) * n) time algo
'''

def ship(weights, d):
    l = max(weights) # left
    r = sum(weights) # right
    while l < r:
        mid = (l + r) / 2 # mid is the hypothesis maximum weight
        bins_needed = 1
        cur_weight = 0
        for w in weights:
            if cur_weight + w > mid:
                bins_needed += 1
                cur_weight = 0
            cur_weight += w
        if bins_needed > D:
            l = mid+1
        else:
            r = mid
    return l
