673. Number of Longest Increasing Subsequence
Medium
647/45
-------------------------
Given an unsorted array of integers, find the number of longest increasing subsequence.

Example 1:
Input: [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequence are [1, 3, 4, 7] and [1, 3, 5, 7].
Example 2:
Input: [2,2,2,2,2]
Output: 5
Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.
Note: Length of the given array will be not exceed 2000 and the answer is guaranteed to be fit in 32-bit signed int.
-------------------------
Approach 1: Naively, check every possibility using two pointers, i,j.
There are n^2 possibilities and it takes O(n) to check each one, so O(n^3)

Approach 2: two pointers, i, j
keep track of max length
if the new j is increasing,
    if it is the new outright best,
        then delete old solutions, update new max, and store this result
    if tied for the best,
        then we should store/append this result.
if the new j leads is decreasing,
    then move i up to the current j

{len:[sequence(i,j)]}
-------------------------