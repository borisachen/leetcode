1012. Numbers With Repeated Digits
Hard/80/27

Given a positive integer N, return the number of positive integers less than or equal to N that have at least 1 repeated digit.


Example 1:

Input: 20
Output: 1
Explanation: The only positive number (<= 20) with at least 1 repeated digit is 11.
Example 2:

Input: 100
Output: 10
Explanation: The positive numbers (<= 100) with atleast 1 repeated digit are 11, 22, 33, 44, 55, 66, 77, 88, 99, and 100.
Example 3:

Input: 1000
Output: 262

'''
1. iterate from 1 to N. naively check each candidate with a set.
Time: N items. each check is log(n) O(nlogn)
Space: log(n) to check each item.

2. backtracking/DFS
11 -> 111, 211, 311... 110, 112, 113,... 101, 111, 121,...
22 -> 122, 222, 322... 220, 221, 222, 223... 202, 212, 222,...
'''
