1262. Greatest Sum Divisible by Three
Medium 71/0

Given an array nums of integers, we need to find the maximum possible sum of
elements of the array such that it is divisible by three.
'''
Example 1:

Input: nums = [3,6,5,1,8]
Output: 18
Explanation: Pick numbers 3, 6, 1 and 8 their sum is 18 (maximum sum divisible by 3).
Example 2:

Input: nums = [4]
Output: 0
Explanation: Since 4 is not divisible by 3, do not pick any number.
Example 3:

Input: nums = [1,2,3,4,4]
Output: 12
Explanation: Pick numbers 1, 3, 4 and 4 their sum is 12 (maximum sum divisible by 3).
'''
'''
Divide the whole list into 3 parts based on each elements remainder when divded by 3: mod0, mod1, mod2
compute the sum of the list.
if total % 3 == 0, then just return total.
if total % 3 == 1, then remove the smallest element from mod1, or the two smallest ones from mod2.
if total % 3 == 2, then remove the smallest element from mod2, or the two smallest ones from mod1.
'''

def doit(nums):
    mod0 = 0
    mod1 = []
    mod2 = []
    remove = float('inf')
    for i in nums:
        if i % 3 == 0: mod0 += i
        if i % 3 == 1: mod1 += [i]
        if i % 3 == 2: mod2 += [i]
    mod1.sort(reverse = True)
    mod2.sort(reverse = True)
    tmp = sum(mod1) + sum(mod2)
    if tmp % 3 == 0:
        return mod0 + tmp
    elif tmp % 3 == 1:
        if len(mod1): remove = min(remove, mod1[-1])
        if len(mod2) > 1: remove = min(mod2[-1]+mod2[-2], remove)
    elif tmp % 3 == 2:
        if len(mod2): remove = min(remove, mod2[-1])
        if len(mod1) > 1: remove = min(mod1[-1]+mod1[-2], remove)
    return mod0 + tmp - remove

'''
Improved:
- the sorting can be improved. we only need to track the lowest two values in
each list, we can do this in one pass.

Add all together, if sum%3==0, return sum.
if sum%3==1, remove the smallest number which has n%3==1.
if sum%3==2, remove the smallest number which has n%3==2.

one pass, and we need to keep the smallest two numbers that have n1%3==1 and n2%3==2.
'''

def doit(nums):
    res = 0
    leftone = 20000
    lefttwo = 20000
    for n in nums:
        res += n
        if n % 3 == 1:
            lefttwo = min(lefttwo, leftone + n)
            leftone = min(leftone, n)
        if n % 3 == 2:
            leftone = min(leftone, lefttwo + n)
            lefttwo = min(lefttwo, n)
    if res % 3 == 0: return res
    if res % 3 == 1: return res - leftone
    return res - lefttwo
