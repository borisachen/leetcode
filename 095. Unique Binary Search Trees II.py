95. Unique Binary Search Trees II
Medium/1060/98

Given an integer n, generate all structurally unique BSTs (binary search trees)
that store values 1...n.

For example,
Given n = 3, your program should return all 5 unique BSTs shown below.
Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]

"""
   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
    def dfs(self, start, end):
        if start == end:
            return None
        for i in range(start, end):
            for l in dfs(start, i):
                for r in dfs(i+1, end):
                    node = TreeNode(i)
                    node.left = l
                    node.right = r
                    res.append(node)
        return res
