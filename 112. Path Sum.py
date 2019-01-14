112. Path Sum

Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
-----
Recurisve top down
-----
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        def help(node, s):
            if not node:
                return False
            if not node.left and not node.right:
                if s + node.val == sum:
                    return True
                else:
                    return False
            l = help(node.left, s+node.val)
            r = help(node.right, s+node.val)
            if l or r:
                return True
            return False

        return help(root, 0)
